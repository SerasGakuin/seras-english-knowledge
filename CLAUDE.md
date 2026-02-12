# seras-english-knowledge

英語塾（Seras学院）の知識管理システム。理論派の生徒向け（関関同立以上/国公立志望）。
参考書の知識を構造化し、確認テスト生成・習熟度管理を行う。

## プロジェクト構造

```
seras-english-knowledge/
├── knowledge/           # 知識ノード（参考書に依存しない標準体系）
│   ├── 品詞と文型/       strc-001〜015 (15件)
│   ├── 動詞の型/         vtyp-001〜021 (21件)
│   ├── 句と節/           clau-001〜041 (29件)
│   ├── 準動詞の意味上の主語/ subj-001〜005 (5件)
│   └── 読解テクニック/    read-001〜014 (14件)
├── sentences/           # 英文データベース（参考書ごとにサブディレクトリ）
│   └── はじめの英文読解ドリル/  Ch01_01〜Ch06_06 (498英文)
├── mappings/            # セクション⇔知識ノードの対応表
│   └── はじめの英文読解ドリル.yaml
├── manifest.yaml        # 作業進捗管理
├── scripts/
│   └── validate.py      # バリデーション（10種チェック）
├── seras-test-generator/ # 確認テスト生成API（FastAPI + WeasyPrint）
├── reference/           # 他参考書の書き起こし（参照用）
└── docs/                # ドキュメント
    ├── ROADMAP.md       # ロードマップ（今どこにいるか）
    ├── strategy/        # 戦略・方針ドキュメント
    ├── design/          # 設計・仕様ドキュメント
    └── log/             # 作業ログ
```

## 現在のフェーズ

> Phase B（知識ノード品質改善）完了。Phase C（確認テスト生成API）進行中（改善適用完了、デプロイ待ち）。
> 詳細は [ROADMAP.md](docs/ROADMAP.md) を参照。

## 作業別ガイド：何を読むべきか

| やりたいこと | 読むドキュメント |
|------------|---------------|
| プロジェクトの背景を理解 | [提案書](docs/strategy/英語参考書統合知識システム_提案書.md)、[ブレスト](docs/strategy/ブレスト_2025-02-03.md) |
| 知識ノード・英文の構造を理解 | [構造化設計案](docs/design/構造化設計案_はじめの英文読解ドリル.md) |
| 知識ノードの追加・修正 | [作業ワークフロー](docs/design/作業ワークフロー.md) |
| 確認テスト生成APIの実装 | [確認テスト生成API設計書](docs/design/確認テスト生成API_設計書.md)、[改善指示書](docs/design/確認テスト改善_指示書.md) |
| 過去の作業内容を確認 | [作業ログ](docs/log/作業ログ.md) |
| 今後の計画を確認 | [ROADMAP.md](docs/ROADMAP.md) |

## 作業ルール

- **1セクション完結原則**: 途中で飛ばさない
- **PDF画像との照合必須**: 書き起こしMDだけを信じない
- **バリデーション必須**: `.venv/bin/python scripts/validate.py`（引数なし全体実行推奨）を実行し、0エラーになるまで次に進まない
- **manifest.yamlで進捗管理**: セクション完了時に必ず更新

## 外部リソース

- 書き起こしMD: `/Users/aruohta/dev/seras-english-grammar/pdf/output/はじめの英文読解ドリル/`
- PDF画像: `/Users/aruohta/dev/seras-english-grammar/pdf/images/はじめの英文読解ドリル/page_XXX.png`
- PDFオフセット: 物理ページ = 参考書ページ（page_006.png = p.6）

## ID体系

- 形式: `prefix-NNN`（例: strc-001）
- strc: 品詞と文型 / vtyp: 動詞の型 / clau: 句と節 / subj: 準動詞の意味上の主語 / read: 読解テクニック

## ドキュメント更新ルール

- knowledge/ や sentences/ を変更したら、manifest.yaml の該当セクションを更新すること
- フェーズの状態が変わったら docs/ROADMAP.md を更新すること
- 新しい設計ドキュメントを追加したら、このファイルの「作業別ガイド」テーブルに追記すること
