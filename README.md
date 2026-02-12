# seras-english-knowledge

英語塾（Seras学院）の知識管理システム。

参考書の知識を**参考書に依存しない標準体系**として構造化し、確認テスト生成・講師の指導標準化を支援する。

## 3レイヤー構成

| レイヤー | ディレクトリ | 内容 |
|---------|------------|------|
| **Knowledge** | `knowledge/` | 知識ノード（84件・5カテゴリ） |
| **Sentences** | `sentences/` | 英文データベース（498英文） |
| **Mappings** | `mappings/` | 参考書セクション⇔知識ノード対応表 |

## 対象参考書

- [x] はじめの英文読解ドリル（構造化完了）
- [ ] 入門英文法の核心
- [ ] 成川英文法INPUT
- [ ] スクランブル英文法・語法
- [ ] 肘井学の読解のための英文法
- [ ] 入門英文問題精講

## ドキュメント

- [CLAUDE.md](CLAUDE.md) — プロジェクト概要・セッション向けガイド
- [docs/ROADMAP.md](docs/ROADMAP.md) — ロードマップ
- [docs/strategy/](docs/strategy/) — 戦略・方針
- [docs/design/](docs/design/) — 設計・仕様
- [docs/log/](docs/log/) — 作業ログ

## バリデーション

```bash
.venv/bin/python scripts/validate.py
```
