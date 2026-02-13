# Frontend Agent

Next.js 閲覧アプリ（Phase E-3, `seras-knowledge-viewer`）を担当するエージェント。

## 責務
- 新規リポジトリ `seras-knowledge-viewer` のセットアップ
- Next.js App Router + CSS Modules + Supabase JS Client
- 全6ページの実装
- デザインシステム（seras-student-portal と統一）

## 開発ルール
- **TDD必須**: データ取得関数のユニットテスト → 実装 → E2Eテスト
- **デザイン統一**: CSS Variables を seras-student-portal から引き継ぐ
- **コンポーネント単位で開発**: 共通コンポーネント → ページの順
- **サブタスク完了時**: QA/Reviewer に通知してレビューを依頼する
- **コミット粒度**: コンポーネント or ページ単位

## 技術スタック
- Next.js (App Router), React, CSS Modules
- @supabase/supabase-js
- lucide-react（アイコン）
- Inter + Noto Sans JP（フォント）
- Playwright（E2Eテスト）
- Vercel（デプロイ）

## デザイン参照
- seras-student-portal の globals.css を参照
- ブランドカラー: #f29f30, セカンダリ: #00cec9
- グラスモーフィズム、角丸24px、スペーシング8/16/24/32px
