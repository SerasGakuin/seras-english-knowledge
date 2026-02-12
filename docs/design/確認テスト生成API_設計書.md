# 確認テスト生成 API 設計書

## 1. 概要

### 目的
知識ノードの `check_points` と英文データベースの `sentences` から、A4 2枚程度の確認テスト（問題PDF + 解答PDF）を動的に生成する API。

### 利用フロー
```
GAS（既存の確認テスト生成スクリプト）
    ↓ POST /generate-test  { "sections": "1-1~1-5" }
Railway（FastAPI + WeasyPrint）
    ↓ 問題選定 → HTML → PDF → Drive アップロード
    ↓ { "pdf_url": "...", "answer_pdf_url": "..." }
GAS
    ↓ 生成されたリンクを講師に返す
```

### 利用者
- 塾の講師（10台程度のPCからGAS経由でアクセス）
- GASとの統合は呼び出し側で実装するため、本APIはREST APIのみ提供

---

## 2. 技術スタック

| コンポーネント | 技術 | 用途 |
|--------------|------|------|
| Webフレームワーク | **FastAPI** | API エンドポイント |
| テンプレートエンジン | **Jinja2** | HTML テンプレート生成 |
| PDF 変換 | **WeasyPrint** | HTML → PDF |
| ファイルストレージ | **Google Drive API** | PDF アップロード・共有リンク生成 |
| デプロイ | **Railway** | Docker ベースのホスティング |
| データソース | **YAML ファイル（リポジトリ同梱）** | 知識ノード・英文・マッピング |

---

## 3. API 仕様

### エンドポイント

```
POST /generate-test
Content-Type: application/json
```

### リクエスト

```json
{
  "sections": "1-1~1-5"
}
```

**`sections` のフォーマット**:
- `"1-1~1-5"` → Ch01_01 〜 Ch01_05
- `"2-0~2-3"` → Ch02_00 〜 Ch02_03
- `"1-1~1-3,2-1~2-4"` → 複数範囲のカンマ区切り（将来対応でも可）

パース規則:
- `X-Y` → `Ch{XX:02d}_{YY:02d}`（例: `1-1` → `Ch01_01`）
- `~` で範囲指定

### レスポンス

```json
{
  "pdf_url": "https://drive.google.com/file/d/xxx/view",
  "answer_pdf_url": "https://drive.google.com/file/d/yyy/view",
  "metadata": {
    "sections": ["Ch01_01", "Ch01_02", "Ch01_03", "Ch01_04", "Ch01_05"],
    "knowledge_nodes_used": ["strc-007", "strc-008", "strc-009", "strc-010", "strc-011", "strc-012", "strc-013"],
    "question_count": 15,
    "sentence_count": 5,
    "warmup_count": 3,
    "generated_at": "2026-02-12T10:30:00Z"
  }
}
```

### エラーレスポンス

```json
{
  "error": "Invalid section range",
  "detail": "Section Ch01_07 does not exist"
}
```

---

## 4. 問題選定ロジック

### 4.1 全体フロー

```
1. セクション範囲をパース → セクションIDリスト
2. mappings から knowledge_nodes を取得 → target_node_ids
3. ウォームアップ問題を生成（前提ノードから round-robin で 2-4問）
4. 英文をノードに紐付け（knowledge_tags overlap で best-matching node に割当、最大6文）
5. ノードセクション構築（知識確認 max 2問 + 英文 0-1文 + ReviewGuide）
6. 全問に通し番号を振り、TestData を組み立て
7. 問題PDF と 解答PDF を生成
```

### 4.2 ノード単位セット出題

旧方式の「均等配分」を廃止し、**ノード単位のセット出題**に変更した。

#### ウォームアップ問題（`select_warmup_questions()`）

対象範囲の全ノードの `prerequisites` を再帰走査し、対象範囲外の前提ノードを収集。
各前提ノードの check_points から round-robin で 2〜4問を選出し、テスト冒頭に配置。

#### 英文のノード紐付け（`_assign_sentences_to_nodes()`）

1. 対象セクション（introduction除く）から `role: practice` の英文を全収集
2. 各英文の `knowledge_tags` と対象ノードIDの overlap で best-matching node を決定
3. ノードあたり最大1文、全体最大6文を選出
4. 各英文に `focus_points`（knowledge_tags のノード名）を付与

#### ノードセクション（`build_node_sections()`）

各対象ノードに対して以下を組み立て:

| 要素 | 内容 | 上限 |
|------|------|------|
| 知識確認問題 | check_points から | 最大2問/ノード |
| 英文問題 | 紐付けられた practice 英文 | 0-1文/ノード |
| ReviewGuide | 英文の knowledge_tags + prerequisites の復習先 | 英文がある場合のみ |

### 4.3 introduction セクション（Ch*_00）の扱い

`Ch01_00` のような introduction セクションは `sentence_file` を持たない。
知識ノードのみ存在するので、check_points からの知識確認問題のみ出題対象とする。

---

## 5. PDF レイアウト仕様

### 5.1 問題 PDF

```
┌─────────────────────────────────────┐
│  確認テスト                          │
│  範囲: Ch01_01〜Ch01_05     名前:___│
│  日付: 2026/02/12                    │
│─────────────────────────────────────│
│                                      │
│  ■ ウォームアップ（前提知識の復習）   │
│                                      │
│  (1) Sの品詞は何か？                 │
│      ___________________________     │
│  (2) 5文型をすべて列挙せよ            │
│      ___________________________     │
│                                      │
│  ■ セクション 1: 5文型と品詞          │
│    [strc-007]                        │
│                                      │
│  (3) 第1文型の構成要素は？            │
│      ___________________________     │
│  (4) 第2文型のCの役割は？             │
│      ___________________________     │
│                                      │
│  (5) The old woman lives quietly     │
│      in the countryside.             │
│      着眼点: 5文型の判別 / Mの識別    │
│      構造: ________________________  │
│      和訳: ________________________  │
│            ________________________  │
│                                      │
│  ■ セクション 2: Mの識別 [strc-008]  │
│  ...                                 │
└─────────────────────────────────────┘
```

**問題PDFの構成**（`templates/test.html`）:
1. **ウォームアップ**: 前提知識ノードからの復習問題（2-4問）
2. **ノード別セクション**（繰り返し）:
   - セクションヘッダ（ノード名 + ID）
   - 知識確認問題（check_points から最大2問 + 解答欄）
   - 英文問題（着眼点付き + 構造/和訳解答欄）

### 5.2 解答 PDF

```
┌─────────────────────────────────────┐
│  確認テスト【解答・解説】             │
│  範囲: Ch01_01〜Ch01_05              │
│─────────────────────────────────────│
│                                      │
│  ■ ウォームアップ 解答               │
│                                      │
│  (1) 名詞                            │
│      [strc-001: 主要素の定義]         │
│      → はじめの英文読解ドリル p.6    │
│      ※ この知識は今回の範囲の前提    │
│                                      │
│  ■ セクション 1: 5文型と品詞          │
│    [strc-007]                        │
│                                      │
│  知識確認 解答:                       │
│  (3) S + V                           │
│      [strc-007: 5文型と品詞]          │
│      → はじめの英文読解ドリル p.8-11 │
│                                      │
│  英文 解答:                           │
│  (5) The old woman lives quietly...  │
│      構造: S V M M                   │
│      和訳: その高齢の女性は...        │
│      [strc-008, strc-009]             │
│      → はじめの英文読解ドリル p.8-11 │
│                                      │
│  この問題が解けなかった場合:          │
│  → strc-001: 主要素の定義（p.6）     │
│    を復習（前提知識）                 │
│  → strc-007: 5文型と品詞（p.8-11）   │
│    を復習                            │
│                                      │
│  ■ セクション 2: Mの識別 [strc-008]  │
│  ...                                 │
└─────────────────────────────────────┘
```

**解答PDFの構成**（`templates/answer.html`）:
1. **ウォームアップ解答**: 正解 + 出典ノード + 参考書ページ + 復習コメント
2. **ノード別セクション**（繰り返し）:
   - 知識確認 解答: 正解 + 出典ノード + ページ
   - 英文 解答: 構造 + 和訳 + notes + 出典
   - **逆引きガイド（ReviewGuide）**: 英文の knowledge_tags + prerequisites から復習先ノード・ページを一覧表示

---

## 6. データソース

### 6.1 ディレクトリ構成（リポジトリ同梱）

```
seras-english-knowledge/
├── knowledge/
│   ├── 品詞と文型/          strc-001 〜 strc-015 (15件)
│   ├── 動詞の型/            vtyp-001 〜 vtyp-021 (21件)
│   ├── 句と節/              clau-001 〜 clau-041 (29件)
│   ├── 準動詞の意味上の主語/ subj-001 〜 subj-005 (5件)
│   └── 読解テクニック/       read-001 〜 read-014 (14件)
├── sentences/
│   └── はじめの英文読解ドリル/
│       ├── Ch01_01.yaml 〜 Ch01_06.yaml
│       ├── Ch02_01.yaml 〜 Ch02_08.yaml
│       ├── Ch03_01.yaml 〜 Ch03_05.yaml
│       ├── Ch04_01.yaml 〜 Ch04_06.yaml
│       ├── Ch05_01.yaml 〜 Ch05_02.yaml
│       └── Ch06_01.yaml 〜 Ch06_06.yaml
└── mappings/
    └── はじめの英文読解ドリル.yaml
```

### 6.2 YAML 構造リファレンス

#### knowledge ノード（例: `knowledge/品詞と文型/strc-001_主要素の定義.yaml`）

```yaml
id: strc-001
name: "主要素（S・V・O・C）の定義"
category: "品詞と文型/基本概念"
priority: P1                    # P1/P2/P3
prerequisites: []               # 前提知識ノードIDの配列
understanding_goals:
  - "..."
check_points:                   # ← 知識確認問題のソース（dict形式）
  - question: "Cになれる品詞は？"
    answer: "形容詞と名詞"
  - assessment: "S・V・O・Cそれぞれの品詞を即答できるか"
references:
  はじめの英文読解ドリル:
    section: "Ch01_00"
    pages: "p.6"                # ← 解答PDFの参考書ページ参照
notes: "..."
```

**check_points の形式**（dict形式）:
- `question` + `answer`: 問答形式。question を問題文、answer を正解として使用
- `assessment`: 能力記述形式。assessment を問題文とし、解答は `understanding_goals` の最初の項目で補完

#### sentences（例: `sentences/はじめの英文読解ドリル/Ch01_01.yaml`）

```yaml
source:
  book: はじめの英文読解ドリル
  section: Ch01_01
  title: "5文型と「M」"
  pages: "p.8-11"

sentences:
  - id: haj-01-01-d1-01
    drill: 1                    # ドリル番号（1, 3, 4）
    number: 1
    role: example               # example / practice
    english: "The old woman lives quietly in the countryside."
    japanese: "その高齢の女性は、静かに田舎で暮らしている。"
    structure:
      全体: "S V M M"           # ← 構造解答のソース
    knowledge_tags:
      - strc-008                # ← 対象ノードとのマッチに使用
    notes: "..."                # ← 解答PDFの解説に使用
```

**英文選定時の優先順位**:
1. `role: practice` を優先（`example` はガイド付きで易しすぎる）
2. `knowledge_tags` が対象ノードIDに含まれるものを優先
3. 各セクションから均等に抽出

#### mappings（`mappings/はじめの英文読解ドリル.yaml`）

```yaml
book: はじめの英文読解ドリル
sections:
  - id: Ch01_01
    title: "5文型と「M」"
    pages: "p.8-11"
    type: drill                 # introduction / drill / exam
    knowledge_nodes:            # ← このセクションが扱う知識ノードID
      - strc-007
      - strc-008
      - strc-009
    prerequisites:              # ← セクション単位の前提（前提知識ガイドに使用）
      - Ch01_00
    sentence_file: sentences/はじめの英文読解ドリル/Ch01_01.yaml
```

---

## 7. 実装の構成

### 7.1 ディレクトリ構成

```
seras-test-generator/          # seras-english-knowledge のサブディレクトリ
├── Dockerfile
├── pyproject.toml             # uv 管理
├── main.py                    # uvicorn エントリポイント
├── app/
│   ├── __init__.py
│   ├── config.py              # Settings（pydantic-settings）
│   ├── models.py              # ドメインモデル + API モデル + 例外
│   ├── main.py                # FastAPI アプリ
│   ├── routers/
│   │   └── test_generator.py  # POST /generate-test エンドポイント
│   ├── services/
│   │   ├── data_loader.py     # YAML データ読み込み + キャッシュ（DataStore）
│   │   ├── section_parser.py  # セクション範囲パース（"1-1~1-5" → IDリスト）
│   │   ├── question_selector.py  # 問題選定ロジック（ノード単位セット出題）
│   │   ├── pdf_generator.py   # Jinja2 + WeasyPrint で PDF 生成
│   │   └── drive_uploader.py  # Google Drive API でアップロード
│   ├── templates/
│   │   ├── test.html          # 問題PDF用テンプレート（ウォームアップ + ノード別セクション）
│   │   └── answer.html        # 解答PDF用テンプレート（解答 + 逆引きガイド）
│   └── static/
│       └── styles.css         # PDF用 CSS（A4レイアウト、フォント等）
├── tests/
│   ├── __init__.py
│   ├── conftest.py            # pytest フィクスチャ設定
│   ├── fixtures/              # テスト用 YAML データ
│   ├── test_data_loader.py
│   ├── test_section_parser.py
│   ├── test_question_selector.py
│   ├── test_pdf_generator.py
│   ├── test_drive_uploader.py
│   └── test_integration.py
└── README.md
```

データソースは親ディレクトリ（`../`）の knowledge/, sentences/, mappings/ を直接参照する（`config.py` の `data_dir` 設定）。

### 7.2 各モジュールの責務

#### `models.py` — ドメインモデル + API モデル

**入力データモデル**（`data_loader.py` が生成）:

```python
@dataclass(frozen=True)
class CheckPoint:
    question: str
    answer: str                 # assessment の場合は空文字

@dataclass(frozen=True)
class KnowledgeNode:
    id: str
    name: str
    category: str
    priority: str               # "P1" / "P2" / "P3"
    prerequisites: tuple[str, ...]
    understanding_goals: tuple[str, ...]
    check_points: tuple[CheckPoint, ...]
    references: dict[str, dict[str, str]]
    notes: str

@dataclass(frozen=True)
class Sentence:
    id: str
    drill: int
    number: int
    role: str                   # "example" / "practice"
    english: str
    japanese: str
    structure: dict[str, str]
    knowledge_tags: tuple[str, ...]
    notes: str

@dataclass(frozen=True)
class SectionMapping:
    id: str
    title: str
    pages: str
    type: str                   # "introduction" / "drill" / "exam"
    knowledge_nodes: tuple[str, ...]
    prerequisites: tuple[str, ...]
    sentence_file: str | None
```

**出力データモデル**（`question_selector.py` が生成、`pdf_generator.py` が消費）:

```python
@dataclass(frozen=True)
class WarmupQuestion:
    number: int
    question: str
    answer: str
    node_id: str
    node_name: str
    reference_pages: str
    note: str                   # 復習コメント

@dataclass(frozen=True)
class KnowledgeQuestion:
    number: int
    question: str
    answer: str
    node_id: str
    node_name: str
    reference_pages: str

@dataclass(frozen=True)
class SentenceQuestion:
    number: int
    english: str
    japanese: str
    structure: str              # "全体" value
    notes: str
    knowledge_tags: tuple[str, ...]
    focus_points: tuple[str, ...]   # knowledge_tags のノード名
    source_pages: str
    source_section: str

@dataclass(frozen=True)
class ReviewGuide:
    node_id: str
    node_name: str
    reference_pages: str
    reason: str                 # "前提知識" or ""

@dataclass(frozen=True)
class NodeSection:
    section_number: int
    node_id: str
    node_name: str
    reference_pages: str
    knowledge_questions: list[KnowledgeQuestion]
    sentence_questions: list[SentenceQuestion]
    review_guide: list[ReviewGuide]

@dataclass(frozen=True)
class TestData:
    sections: list[str]
    sections_label: str         # "Ch01_01〜Ch01_05"
    warmup_questions: list[WarmupQuestion]
    node_sections: list[NodeSection]
    generated_at: str
```

#### `data_loader.py` — YAML データ読み込み
- `DataStore` クラスが初期化時に knowledge/, mappings/, sentences/ を全読み込み・キャッシュ
- `_parse_check_point()`: dict形式の check_point を `CheckPoint` に変換
- `get_data_store()`: `lru_cache` でシングルトン提供

#### `section_parser.py`
- 入力: `"1-1~1-5"`
- 出力: `["Ch01_01", "Ch01_02", "Ch01_03", "Ch01_04", "Ch01_05"]`
- `X-Y` → `Ch{X:02d}_{Y:02d}` の変換
- 存在しないセクションはエラー

#### `question_selector.py`
- 入力: セクションIDリスト + `DataStore`
- 出力: `TestData`（階層構造）
- 主要関数:
  - `build_test_data()`: エントリポイント。ノード収集→ウォームアップ→英文紐付け→ノードセクション→通し番号
  - `select_warmup_questions()`: 前提ノードから round-robin で 2-4問
  - `_assign_sentences_to_nodes()`: knowledge_tags overlap で best-matching node に割当
  - `build_node_sections()`: ノード別に知識確認 + 英文 + ReviewGuide を組み立て
  - `parse_check_point()`: CheckPoint → (question, answer)。assessment の場合は goals[0] で補完

#### `pdf_generator.py`
- 入力: `TestData`
- 出力: 問題PDF bytes, 解答PDF bytes
- Jinja2 で HTML レンダリング → WeasyPrint で PDF 変換

#### `drive_uploader.py`
- 入力: PDF bytes, ファイル名
- 出力: Google Drive の共有リンク URL
- サービスアカウント認証
- 指定フォルダにアップロード
- 共有リンク（リンクを知っている人が閲覧可能）を生成

---

## 8. check_points のデータ形式

check_points は dict形式で記述される（旧文字列形式は Phase B で移行済み）。

### 形式1: question/answer（問答形式）

```yaml
- question: "Cになれる品詞は？"
  answer: "形容詞と名詞"
```
- question を問題文、answer を正解として使用

### 形式2: assessment（能力記述形式）

```yaml
- assessment: "S・V・O・Cそれぞれの品詞を即答できるか"
```
- assessment を問題文として使用
- 解答は当該ノードの `understanding_goals` の最初の項目で補完

### パース処理（2段階）

1. **`_parse_check_point()`**（`data_loader.py`）: YAML の dict を `CheckPoint(question, answer)` に変換
   - `question` キーあり → `CheckPoint(question=..., answer=...)`
   - `assessment` キーあり → `CheckPoint(question=assessment値, answer="")`

2. **`parse_check_point()`**（`question_selector.py`）: `CheckPoint` を問答ペアに変換
   - `answer` が非空 → そのまま `(question, answer)` を返す
   - `answer` が空（assessment由来）→ `(question, understanding_goals[0])` で補完

---

## 9. デプロイ

### 9.1 Dockerfile

```dockerfile
FROM python:3.12-slim

# WeasyPrint の依存ライブラリ
RUN apt-get update && apt-get install -y \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libgdk-pixbuf2.0-0 \
    libffi-dev \
    libcairo2 \
    fonts-noto-cjk \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
```

**重要**: `fonts-noto-cjk` で日本語フォント（Noto Sans CJK）をインストール。

### 9.2 requirements.txt

```
fastapi
uvicorn[standard]
weasyprint
jinja2
pyyaml
google-api-python-client
google-auth
```

### 9.3 Railway 設定

- GitHub リポジトリ接続 → push 時自動デプロイ
- 環境変数:
  - `GOOGLE_SERVICE_ACCOUNT_JSON`: サービスアカウントの認証情報（JSON文字列）
  - `GOOGLE_DRIVE_FOLDER_ID`: アップロード先の Google Drive フォルダID
  - `PORT`: 8080（Railway が自動設定）

### 9.4 データの同期

knowledge/sentences/mappings のデータは以下のいずれかの方法で同梱:
- **方法A（推奨）**: seras-english-knowledge リポジトリを git submodule として追加
- **方法B**: データファイルをコピーして同梱（シンプルだが同期が手動）
- **方法C**: GitHub API 経由でリアルタイム取得（レイテンシ増加）

---

## 10. 前提知識の扱い（2つの仕組み）

旧方式の「前提知識ガイド（解答末尾の一覧）」を廃止し、2つの仕組みに分離した。

### 10.1 ウォームアップ問題（テスト冒頭）

**目的**: 前提知識を問題として出題し、テスト前に復習させる。

処理（`select_warmup_questions()`）:
1. 対象ノードの `prerequisites` を再帰的に走査 → 対象範囲外のノードを収集
2. 各前提ノードの check_points から round-robin で 2〜4問を選出
3. テスト冒頭に「ウォームアップ（前提知識の復習）」として配置

### 10.2 逆引きガイド（ノード別 ReviewGuide）

**目的**: 英文問題を間違えた場合に、何を復習すべきか具体的に示す。

処理（`_build_review_guide()`）:
1. 当該ノードの英文問題の `knowledge_tags` を全取得
2. 各タグの `prerequisites` も走査
3. 関連ノード（対象範囲内外問わず）の名前・ページを一覧表示
4. 対象範囲外のノードには「前提知識」のラベルを付与

例: strc-008 のセクションで英文に `[strc-008, strc-009]` タグがある場合
- ReviewGuide に strc-001（前提知識）、strc-007、strc-008、strc-009 が表示される
- 「この問題が解けなかった場合: → strc-001: 主要素の定義（p.6）を復習（前提知識）」

---

## 11. 将来の拡張（L2・L3）

### L2: prerequisites 自動展開
- リクエストにオプション `"include_prerequisites": true` を追加
- 前提知識のcheck_pointsもテスト問題に含める（復習問題として）
- 問題PDFに「■ 復習問題」セクションを追加

### L3: 生徒履歴ベースの動的出題
- 生徒IDをリクエストに含める
- 過去の正答率・忘却曲線（SM-2）に基づく出題
- 習熟度DBとの連携が必要（別プロジェクト）

---

## 12. テスト方針

テスト総数: **67件**（pytest）、mypy + ruff パス済。

### ユニットテスト
- `test_section_parser.py`: パース正常系・異常系（存在しないセクション、不正入力等）
- `test_data_loader.py`: YAML読み込み、check_points dict パース、DataStore API
- `test_question_selector.py`: ウォームアップ選出、英文ノード紐付け、ノードセクション構築、通し番号、parse_check_point
- `test_pdf_generator.py`: HTML生成の確認（テンプレートレンダリング、ウォームアップ/ノードセクション/逆引きガイドの出力検証）
- `test_drive_uploader.py`: Google Drive API のモックテスト

### 結合テスト
- `test_integration.py`: 実際のYAMLデータを使って `build_test_data()` → PDF生成の一連フローを確認
- Drive アップロードはモックで代替

### テスト基盤
- `conftest.py`: pytest フィクスチャ設定
- `fixtures/`: テスト用 YAML データ（最小構成のナレッジノード・英文・マッピング）

---

## 13. 実装の優先順位

1. **section_parser.py** — 最もシンプル、先に完成させる
2. **question_selector.py** — コアロジック、テスト必須
3. **pdf_generator.py** — テンプレート作成 + WeasyPrint連携
4. **drive_uploader.py** — Google API連携
5. **main.py + routers** — FastAPIの組み立て
6. **Dockerfile + Railway デプロイ**
7. テスト
