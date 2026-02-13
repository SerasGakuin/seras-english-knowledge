# seras-english-knowledge

英語塾（Seras学院）の知識管理システム。理論派の生徒向け（関関同立以上/国公立志望）。
参考書の知識を構造化し、確認テスト生成・習熟度管理を行う。

## プロジェクト構造

```
seras-english-knowledge/
├── seras-test-generator/ # 確認テスト生成API（FastAPI + Supabase）
│   ├── app/
│   │   ├── main.py
│   │   ├── config.py          # Settings（Supabase接続情報等）
│   │   ├── models.py          # データモデル
│   │   ├── services/
│   │   │   ├── data_loader.py         # DataStore（YAML版）+ get_data_store()
│   │   │   ├── supabase_client.py     # PostgRESTクライアント
│   │   │   ├── supabase_data_store.py # SupabaseDataStore（本番用）
│   │   │   ├── question_selector.py   # 出題ロジック
│   │   │   ├── section_parser.py      # セクション範囲パーサ
│   │   │   ├── pdf_generator.py       # PDF生成（WeasyPrint）
│   │   │   └── gcs_uploader.py        # GCS アップロード
│   │   └── templates/                 # Jinja2テンプレート
│   └── tests/                         # 85テスト
├── scripts/
│   └── supabase/              # DB関連スクリプト
│       ├── 001_create_tables.sql  # DDL（11テーブル）
│       ├── import_to_supabase.py  # YAML→DB インポート
│       └── verify_supabase.py     # データ整合性検証
├── Dockerfile             # Cloud Run デプロイ用
├── reference/             # 他参考書の書き起こし（参照用）
└── docs/                  # ドキュメント
    ├── ROADMAP.md         # ロードマップ（今どこにいるか）
    ├── strategy/          # 戦略・方針ドキュメント
    ├── design/            # 設計・仕様ドキュメント
    └── log/               # 作業ログ
```

## データストア

> Phase E（2026-02-13）でYAML → Supabase（PostgreSQL）に移行完了。YAML は削除済み。

- **DB**: Supabase (PostgreSQL, Tokyo リージョン)
- **テーブル数**: 11（knowledge_nodes, sections, sentences + 関連テーブル）
- **データ量**: 84ノード、498英文、39セクション（+2 Exam未構造化）
- **接続**: postgrest-py（REST API経由）
- **環境変数**: `SUPABASE_URL`, `SUPABASE_KEY`, `DATA_STORE_TYPE=supabase`

## 現在のフェーズ

> Phase A〜E 完了。**実運用開始（2026-02-13）**。Cloud Run + GAS統合でスプレッドシートからPDF生成可能。
> 次: Phase B'（講師主導の品質改善）、Phase D（Exam構造化）。
> 詳細は [ROADMAP.md](docs/ROADMAP.md) を参照。

## 関連リポジトリ

- **seras-knowledge-viewer**: Next.js 閲覧アプリ（`/Users/aruohta/dev/seras-knowledge-viewer/`）
  - Supabase から直接データ取得
  - 6ページ: ダッシュボード、ノード一覧/詳細、セクション一覧/詳細、英文検索
  - URL: https://seras-knowledge-viewer.vercel.app
  - GitHub: SerasGakuin/seras-knowledge-viewer

## 作業別ガイド：何を読むべきか

| やりたいこと | 読むドキュメント |
|------------|---------------|
| プロジェクトの背景を理解 | [提案書](docs/strategy/英語参考書統合知識システム_提案書.md)、[ブレスト](docs/strategy/ブレスト_2025-02-03.md) |
| 知識ノード・英文の構造を理解 | [構造化設計案](docs/design/構造化設計案_はじめの英文読解ドリル.md) |
| 確認テスト生成APIの実装 | [確認テスト生成API設計書](docs/design/確認テスト生成API_設計書.md)、[改善指示書](docs/design/確認テスト改善_指示書.md) |
| DB移行・Webアプリの設計 | [Phase E 設計案](docs/design/Phase_E_設計案.md) |
| 過去の作業内容を確認 | [作業ログ](docs/log/作業ログ.md) |
| 今後の計画を確認 | [ROADMAP.md](docs/ROADMAP.md) |

## デプロイ情報

### 確認テスト生成API（Cloud Run）
- API URL: `https://seras-test-generator-hif2eccama-an.a.run.app`
- GCPプロジェクト: `seras-test-generator`
- GCS: `gs://seras-test-pdfs`
- CI/CD: GitHub Actions（main push → 自動デプロイ）

## 外部リソース

- 書き起こしMD: `/Users/aruohta/dev/seras-english-grammar/pdf/output/はじめの英文読解ドリル/`
- PDF画像: `/Users/aruohta/dev/seras-english-grammar/pdf/images/はじめの英文読解ドリル/page_XXX.png`
- PDFオフセット: 物理ページ = 参考書ページ（page_006.png = p.6）

## ID体系

- 形式: `prefix-NNN`（例: strc-001）
- strc: 品詞と文型 / vtyp: 動詞の型 / clau: 句と節 / subj: 準動詞の意味上の主語 / read: 読解テクニック

## ドキュメント更新ルール

- フェーズの状態が変わったら docs/ROADMAP.md を更新すること
- 新しい設計ドキュメントを追加したら、このファイルの「作業別ガイド」テーブルに追記すること
