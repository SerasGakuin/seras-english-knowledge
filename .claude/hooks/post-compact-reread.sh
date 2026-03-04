#!/bin/bash
# コンパクション後に作業中の参考書の指示書を確実に読み込ませる
cd "$CLAUDE_PROJECT_DIR" || exit 0

python3 -c "
import yaml, glob, os, sys

def eprint(msg=''):
    print(msg, file=sys.stderr)

checkpoints = sorted(glob.glob('scripts/supabase/*_data/checkpoint.yaml'))
if not checkpoints:
    eprint('(checkpoint.yaml が見つかりませんでした)')
    sys.exit(0)

# 全 checkpoint を読み込み、残作業の有無で分類
has_work = []   # remaining > 0（セクション作業中 or バッチ間）
done = []       # remaining == 0（全完了）

for cp_path in checkpoints:
    with open(cp_path) as f:
        cp = yaml.safe_load(f) or {}

    slug = os.path.basename(os.path.dirname(cp_path)).replace('_data', '')
    book = cp.get('book', slug)

    cs = cp.get('current_state', {}) or {}
    phase = cs.get('phase', cp.get('phase_name', ''))
    section = cs.get('current_section', cp.get('current_section'))
    remaining = (cp.get('progress', {}) or {}).get('remaining',
                 cp.get('total_pilot_sections', 0) - cp.get('completed_sections', 0))

    must_reread = cp.get('must_reread', [])

    info = {
        'slug': slug, 'book': book, 'path': cp_path,
        'phase': phase, 'section': section,
        'must_reread': must_reread, 'remaining': remaining,
    }

    if remaining > 0:
        has_work.append(info)
    else:
        done.append(info)

# --- 出力 ---
eprint()
eprint('╔══════════════════════════════════════════════════════════════╗')
eprint('║  ⚠ コンテキストコンパクション検知 — 再読込プロトコル発動 ⚠  ║')
eprint('╚══════════════════════════════════════════════════════════════╝')
eprint()

if has_work:
    for b in has_work:
        sec_label = b['section'] if b['section'] else 'バッチ間（次セクション未着手）'
        eprint(f'■ {b[\"book\"]}（{b[\"slug\"]}）')
        eprint(f'  フェーズ: {b[\"phase\"]}')
        eprint(f'  現在セクション: {sec_label}')
        eprint(f'  残セクション数: {b[\"remaining\"]}')
        eprint()

    ALWAYS_READ = ['docs/design/構造化共通ワークフロー.md']

    eprint('自分が担当している参考書の checkpoint + 設計書を Read ツールで全文読み込んでから作業を再開すること。')
    eprint('どの参考書を担当しているか不明な場合は、全て読むこと。')
    eprint()
    seq = 1
    seen = set()
    # 1. 全参考書の checkpoint
    for b in has_work:
        eprint(f'  {seq}. {b[\"path\"]}')
        seen.add(b['path'])
        seq += 1
    # 2. 常に読むファイル
    for ar in ALWAYS_READ:
        if ar not in seen and os.path.exists(ar):
            eprint(f'  {seq}. {ar}')
            seen.add(ar)
            seq += 1
    # 3. 全参考書の must_reread（重複排除）
    for b in has_work:
        for mr in b['must_reread']:
            if mr not in seen and os.path.exists(mr):
                eprint(f'  {seq}. {mr}  ← {b[\"book\"]}')
                seen.add(mr)
                seq += 1
    eprint()
    eprint('読み終わるまで構造化作業に着手しないこと。')
else:
    eprint('現在作業中の参考書はありません。')

if done:
    eprint()
    for d in done:
        eprint(f'  (完了) {d[\"book\"]}（{d[\"slug\"]}）: {d[\"phase\"]}')

eprint()
eprint('--- 全チェックポイント ---')
for cp_path in checkpoints:
    eprint(f'=== {cp_path} ===')
    with open(cp_path) as f:
        eprint(f.read())
"
