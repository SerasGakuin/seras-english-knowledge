#!/bin/bash
# 構造化作業中の自動停止を防止する
# remaining > 0 の参考書がある場合、停止をブロックして作業継続を指示する
#
# バイパス: 連続3回ブロックされたら停止を許可（非構造化セッション用）
cd "$CLAUDE_PROJECT_DIR" || exit 0

COUNTER_FILE="$CLAUDE_PROJECT_DIR/.claude/.stop_block_count"
COUNT=0
if [ -f "$COUNTER_FILE" ]; then
    COUNT=$(cat "$COUNTER_FILE" 2>/dev/null || echo 0)
    # 前回のブロックから2分以上経過 → カウンタリセット（作業した証拠）
    AGE=$(( $(date +%s) - $(stat -c %Y "$COUNTER_FILE" 2>/dev/null || echo 0) ))
    if [ "$AGE" -gt 120 ]; then
        COUNT=0
    fi
fi

if [ "$COUNT" -ge 3 ]; then
    rm -f "$COUNTER_FILE"
    exit 0  # 3回連続ブロック → 停止許可（無限ループ防止）
fi

python3 -c "
import yaml, glob, os, sys

checkpoints = sorted(glob.glob('scripts/supabase/*_data/checkpoint.yaml'))
if not checkpoints:
    sys.exit(0)  # checkpoint なし → 停止許可

books_with_work = []
for cp_path in checkpoints:
    with open(cp_path) as f:
        cp = yaml.safe_load(f) or {}

    remaining = (cp.get('progress', {}) or {}).get('remaining', 0)
    if remaining > 0:
        book = cp.get('book', '?')
        slug = os.path.basename(os.path.dirname(cp_path)).replace('_data', '')
        next_actions = cp.get('next_actions', [])
        books_with_work.append({
            'book': book, 'slug': slug, 'remaining': remaining,
            'next_actions': next_actions, 'path': cp_path,
        })

if not books_with_work:
    sys.exit(0)  # 全参考書完了 → 停止許可

# --- 停止をブロックし、継続を指示（stderr に出力）---
def err(msg=''):
    print(msg, file=sys.stderr)

err()
err('停止しないでください。構造化作業がまだ完了していません。')
err('CLAUDE.md ルール:「バッチ間で止まらない — 全セクション完了まで自律的に継続すること」')
err()
for b in books_with_work:
    err(f'■ {b[\"book\"]}（{b[\"slug\"]}）: 残 {b[\"remaining\"]} セクション')
    if b['next_actions']:
        for a in b['next_actions']:
            err(f'  → {a}')
    err(f'  checkpoint: {b[\"path\"]}')
    err()

err('自分の担当参考書の checkpoint.yaml を Read で読み、next_actions に従って次のバッチを開始すること。')
err('担当参考書が不明な場合は、全 checkpoint を読んで直近の作業内容から判断すること。')
sys.exit(1)  # has remaining work
"

PYTHON_EXIT=$?

if [ $PYTHON_EXIT -eq 1 ]; then
    echo $((COUNT + 1)) > "$COUNTER_FILE"
    exit 2  # ブロック: Claude Code に停止させない
fi

rm -f "$COUNTER_FILE"
exit 0  # 全完了: 停止を許可
