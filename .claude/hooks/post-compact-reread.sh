#!/bin/bash
# コンパクション後に作業中の参考書の指示書を確実に読み込ませる
cd "$CLAUDE_PROJECT_DIR" || exit 0

python3 -c "
import yaml, glob, os, sys

checkpoints = sorted(glob.glob('scripts/supabase/*_data/checkpoint.yaml'))
if not checkpoints:
    print('(checkpoint.yaml が見つかりませんでした)')
    sys.exit(0)

# 全 checkpoint を読み込み、作業中かどうかを判定
active = []
completed = []

for cp_path in checkpoints:
    with open(cp_path) as f:
        cp = yaml.safe_load(f) or {}

    slug = os.path.basename(os.path.dirname(cp_path)).replace('_data', '')
    book = cp.get('book', slug)

    # 作業中かどうかの判定（複数フォーマット対応）
    cs = cp.get('current_state', {}) or {}
    phase = cs.get('phase', cp.get('phase_name', ''))
    section = cs.get('current_section', cp.get('current_section'))
    remaining = (cp.get('progress', {}) or {}).get('remaining',
                 cp.get('total_pilot_sections', 0) - cp.get('completed_sections', 0))

    is_done = ('完了' in str(phase)) and (section is None or str(section) == 'completed')
    # remaining > 0 でもフェーズ完了なら次フェーズ待ち（作業中扱い）
    has_work = remaining > 0

    must_reread = cp.get('must_reread', [])

    info = {
        'slug': slug, 'book': book, 'path': cp_path,
        'phase': phase, 'section': section,
        'must_reread': must_reread, 'remaining': remaining,
    }

    if not is_done and section and str(section) != 'completed':
        active.append(info)
    elif has_work:
        # フェーズ完了だが残セクションあり → 次フェーズ待ち
        completed.append(info)
    else:
        completed.append(info)

# --- 出力 ---
print()
print('╔══════════════════════════════════════════════════════════════╗')
print('║  ⚠ コンテキストコンパクション検知 — 再読込プロトコル発動 ⚠  ║')
print('╚══════════════════════════════════════════════════════════════╝')
print()

if active:
    # 作業中の参考書がある場合：must_reread のファイルを明示
    for a in active:
        print(f'■ 作業中: {a[\"book\"]}（{a[\"slug\"]}）')
        print(f'  フェーズ: {a[\"phase\"]}')
        print(f'  現在セクション: {a[\"section\"]}')
        print(f'  残セクション数: {a[\"remaining\"]}')
        print()

    # 常に読むべきファイル（must_reread に含まれていなくても必ず追加）
    ALWAYS_READ = ['docs/design/構造化共通ワークフロー.md']

    print('以下のファイルを Read ツールで順番に全文読み込んでから作業を再開すること:')
    print()
    seq = 1
    seen = set()
    # 1. 全 active の checkpoint
    for a in active:
        print(f'  {seq}. {a[\"path\"]}')
        seen.add(a['path'])
        seq += 1
    # 2. 常に読むファイル
    for ar in ALWAYS_READ:
        if ar not in seen and os.path.exists(ar):
            print(f'  {seq}. {ar}')
            seen.add(ar)
            seq += 1
    # 3. must_reread（重複排除）
    for a in active:
        for mr in a['must_reread']:
            if mr not in seen and os.path.exists(mr):
                print(f'  {seq}. {mr}')
                seen.add(mr)
                seq += 1
    print()
    print('読み終わるまで構造化作業に着手しないこと。')
else:
    print('現在作業中の参考書はありません。')
    if completed:
        print()
        for c in completed:
            status = f'残 {c[\"remaining\"]} セクション' if c['remaining'] > 0 else '全完了'
            print(f'  - {c[\"book\"]}（{c[\"slug\"]}）: {c[\"phase\"]} [{status}]')

print()
print('--- 全チェックポイント ---')
for cp_path in checkpoints:
    print(f'=== {cp_path} ===')
    with open(cp_path) as f:
        print(f.read())
" 2>/dev/null
