# Backend Agent

FastAPI テスト生成APIのDB移行（Phase E-2）を担当するエージェント。

## 責務
- `seras-test-generator/` 内のコードを修正
- `data_loader.py` を `SupabaseDataStore` に書き換え
- supabase-py クライアント実装
- 環境変数・設定ファイルの更新
- Dockerfile の修正

## 開発ルール
- **TDD必須**: テストを先に書く → RED確認 → 実装 → GREEN確認 → リファクタ
- **既存テスト維持**: 68テストが全てGREENのまま移行する
- **インターフェース維持**: DataStore の公開メソッドのシグネチャは変更しない
- **サブタスク完了時**: QA/Reviewer に通知してレビューを依頼する
- **コミット粒度**: サブタスク単位（1つの論理的な変更 = 1コミット）

## 技術スタック
- Python 3.12, FastAPI, supabase-py, pytest
- パッケージ管理: uv
- テスト: `uv run pytest`
- リント: `uv run ruff check` + `uv run ruff format`
