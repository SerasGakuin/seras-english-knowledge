"""第3章: 構文編 Theme 18-22（呼応・ネクサス・挿入・比較・複合関係詞）"""

# ============================================================
# 1. KNOWLEDGE_NODES
# ============================================================

KNOWLEDGE_NODES = [
    {
        "id": "hco-005",
        "name": "呼応",
        "category": "構文",
        "priority": "P1",
        "notes": "both A and B「AとBの両方」、not A but B「AではなくB」、not only A but (also) B「AだけでなくBも」、either A or B「AかBか」、neither A nor B「AもBもどちらも〜ない」の5つの呼応パターン。前の単語（both/not/not only/either/neither）に反応してうしろの接続詞を予測する。",
    },
    {
        "id": "hco-006",
        "name": "ネクサス",
        "category": "構文",
        "priority": "P1",
        "notes": "文のSV以外にある隠れたSV関係（S'V'）を見抜く。(1)第5文型SVOCのOとC（Cにdo/to do/-ing/p.p.）、(2)準動詞の意味上の主語（for名詞to do/所有格+動名詞/主格+分詞構文）、(3)付帯状況with OC（Cに-ing/p.p.）の3パターン。",
    },
    {
        "id": "hco-007",
        "name": "挿入",
        "category": "構文",
        "priority": "P1",
        "notes": "文の途中でカンマ2つを使って補足説明を入れる文体。(1)分詞構文の挿入、(2)関係詞節の挿入、(3)同格の挿入（名詞/前置詞句）、(4)SVの挿入（I think / it seems等）の4パターン。いったんカンマではさまれた挿入部分を読みとばして文の骨格SVを把握するのがコツ。",
    },
    {
        "id": "hco-008",
        "name": "比較（原級・比較級・最上級）",
        "category": "構文",
        "priority": "P1",
        "notes": "比較の3つの世界。(1)原級 as - as ...「…と同じくらい」、否定形 not as [so] - as ...「…ほど〜ではない」、(2)比較級 -er than ...「…より〜だ」、much/far/even等の強調、(3)最上級 the -est of/in ...「…のなかで一番」、範囲は経験(have ever p.p.)・同種(of)・異種(in)。「何と何を比べているか」の視点が重要。",
    },
    {
        "id": "hco-009",
        "name": "比較（慣用表現）",
        "category": "構文",
        "priority": "P1",
        "notes": "比較の慣用表現4パターン。(1) not so much A as B「AというよりむしろB」（原級の否定形が元）、(2) no more A than B「Bと同様にAではない」（両者否定）、(3) The+比較級〜, the+比較級...「〜すればするほど、それだけますます…」、(4)最上級相当表現（No other+単数名詞 is as〜as A / S V 比較級 than any other 単数名詞）。",
    },
    {
        "id": "hco-010",
        "name": "複合関係詞",
        "category": "構文",
        "priority": "P1",
        "notes": "複合関係代名詞（whoever/whatever/whichever）と複合関係副詞（whenever/wherever/however）。名詞節または副詞節をつくり「たとえ〜でも」の意味。howeverはうしろに形容詞・副詞をともなう。no matter what/who/how等で書き換え可能。",
    },
]

# ============================================================
# 2. UNDERSTANDING_GOALS
# ============================================================

UNDERSTANDING_GOALS = [
    # hco-005: 呼応
    {"node_id": "hco-005", "seq": 1, "goal": "both A and B / not A but B / not only A but (also) B / either A or B / neither A nor B の5パターンを認識できる"},
    {"node_id": "hco-005", "seq": 2, "goal": "前の単語（both/not/not only/either/neither）に反応して、うしろの接続詞（and/but/or/nor）を予測できる"},
    {"node_id": "hco-005", "seq": 3, "goal": "呼応の接続詞（and/but/or/nor）が通常の意味ではなく呼応パターンの一部であることを見抜ける"},
    # hco-006: ネクサス
    {"node_id": "hco-006", "seq": 1, "goal": "第5文型SVOCのOとCにネクサスの関係（S'V'）を見抜ける"},
    {"node_id": "hco-006", "seq": 2, "goal": "不定詞・動名詞・分詞構文の意味上の主語を認識し、ネクサスの関係を見抜ける"},
    {"node_id": "hco-006", "seq": 3, "goal": "付帯状況 with OC のOとCにネクサスの関係を見抜ける"},
    {"node_id": "hco-006", "seq": 4, "goal": "There is S -ing ... のS -ingにネクサスの関係を見抜ける"},
    # hco-007: 挿入
    {"node_id": "hco-007", "seq": 1, "goal": "分詞構文・関係詞節・同格・SVの挿入パターンを認識できる"},
    {"node_id": "hco-007", "seq": 2, "goal": "カンマではさまれた挿入部分を読みとばして文の骨格SVを把握できる"},
    {"node_id": "hco-007", "seq": 3, "goal": "of+抽象名詞=形容詞（of importance = important等）の関係を理解している"},
    {"node_id": "hco-007", "seq": 4, "goal": "SV挿入のもとの文（I think that ~ / It seems that ~ 等）を意識して訳せる"},
    # hco-008: 比較（原級・比較級・最上級）
    {"node_id": "hco-008", "seq": 1, "goal": "原級 as - as ... / 否定形 not as [so] - as ... を認識し、何と何を比べているか特定できる"},
    {"node_id": "hco-008", "seq": 2, "goal": "比較級 -er than ... を認識し、比較対象を特定できる"},
    {"node_id": "hco-008", "seq": 3, "goal": "最上級 the -est of/in ... を認識し、最上級の範囲（経験/同種of/異種in）を特定できる"},
    {"node_id": "hco-008", "seq": 4, "goal": "比較の強調表現（very/much/far/even/still/by far）の原級・比較級・最上級との組み合わせを理解している"},
    # hco-009: 比較（慣用表現）
    {"node_id": "hco-009", "seq": 1, "goal": "not so much A as B「AというよりむしろB」を認識し、もとが原級の否定形であることを理解している"},
    {"node_id": "hco-009", "seq": 2, "goal": "no more A than B「Bと同様にAではない」（両者否定）を認識できる"},
    {"node_id": "hco-009", "seq": 3, "goal": "The+比較級〜, the+比較級...「〜すればするほど、それだけますます…」を認識できる"},
    {"node_id": "hco-009", "seq": 4, "goal": "最上級相当表現（No other+名詞 is as〜as A / S V 比較級 than any other 名詞）を認識できる"},
    # hco-010: 複合関係詞
    {"node_id": "hco-010", "seq": 1, "goal": "複合関係代名詞（whoever/whatever/whichever）が名詞節・副詞節をつくることを理解している"},
    {"node_id": "hco-010", "seq": 2, "goal": "複合関係副詞（whenever/wherever/however）が副詞節をつくることを理解している"},
    {"node_id": "hco-010", "seq": 3, "goal": "howeverがうしろに形容詞・副詞をともなうパターンを認識できる"},
    {"node_id": "hco-010", "seq": 4, "goal": "no matter what/who/how等での書き換えを理解している"},
]

# ============================================================
# 3. CHECK_POINTS
# ============================================================

CHECK_POINTS = [
    # hco-005: 呼応
    {"node_id": "hco-005", "seq": 1, "question": "bothを見たら何を予測するか？", "answer": "and。both A and B「AとBの両方」。"},
    {"node_id": "hco-005", "seq": 2, "question": "notを見たら何を予測するか？", "answer": "but。not A but B「AではなくてB」。"},
    {"node_id": "hco-005", "seq": 3, "question": "not onlyを見たら何を予測するか？", "answer": "but (also)。not only A but (also) B「AだけでなくBも」。alsoはよく消える。B as well as Aと同義。"},
    {"node_id": "hco-005", "seq": 4, "question": "eitherを見たら何を予測するか？", "answer": "or。either A or B「AかBか」。"},
    {"node_id": "hco-005", "seq": 5, "question": "neitherを見たら何を予測するか？", "answer": "nor。neither A nor B「AもBもどちらも〜ない」。"},
    # hco-006: ネクサス
    {"node_id": "hco-006", "seq": 1, "question": "ネクサスの関係とは何か？", "answer": "文のSV以外にある隠れたSV関係のこと。S'V'と表記する。"},
    {"node_id": "hco-006", "seq": 2, "question": "ネクサスの関係が現れる3つのパターンは？", "answer": "(1)第5文型SVOCのOとC、(2)準動詞の意味上の主語と準動詞（不定詞/動名詞/分詞構文）、(3)付帯状況with OCのOとC。"},
    {"node_id": "hco-006", "seq": 3, "question": "不定詞の意味上の主語はどのように表すか？", "answer": "for 名詞 to do の形で不定詞の前に置く。"},
    {"node_id": "hco-006", "seq": 4, "question": "動名詞の意味上の主語はどのように表すか？", "answer": "動名詞の前に所有格（文の主語の場合）または目的格を置く。"},
    {"node_id": "hco-006", "seq": 5, "question": "分詞構文の主語が主節と異なる場合はどうするか？", "answer": "分詞の前に主格の形で主語を置く（独立分詞構文）。"},
    # hco-007: 挿入
    {"node_id": "hco-007", "seq": 1, "question": "挿入の4パターンは何か？", "answer": "(1)分詞構文の挿入、(2)関係詞節の挿入、(3)同格の挿入（名詞/前置詞句）、(4)SVの挿入。"},
    {"node_id": "hco-007", "seq": 2, "question": "挿入を読み解くコツは？", "answer": "いったんカンマではさまれた挿入部分を読みとばして、文の骨格であるSVを把握する。"},
    {"node_id": "hco-007", "seq": 3, "question": "of importance を1語の形容詞に置き換えると？", "answer": "important。of+抽象名詞=形容詞の関係。of use = useful、of value = valuable、of help = helpful。"},
    {"node_id": "hco-007", "seq": 4, "question": "The movie, I think, is not interesting. のもとの文は？", "answer": "I think that the movie is not interesting."},
    # hco-008: 比較（原級・比較級・最上級）
    {"node_id": "hco-008", "seq": 1, "question": "比較の3つの世界は？", "answer": "(1)原級 as - as ...（2つが同じ）、(2)比較級 -er than ...（2つに差がある）、(3)最上級 the -est of/in ...（3つ以上で一番）。"},
    {"node_id": "hco-008", "seq": 2, "question": "原級の否定形の表現は？", "answer": "not as [so] - as ...「…ほど〜ではない」。先頭のasはsoになることもある。"},
    {"node_id": "hco-008", "seq": 3, "question": "比較級の強調に使える語は？very は使えるか？", "answer": "much / far / even / still。veryは比較級の強調に使えない（very betterは不可、much betterが正しい）。"},
    {"node_id": "hco-008", "seq": 4, "question": "最上級の範囲を示す3つの方法は？", "answer": "(1)経験: the 最上級 名詞 (that) I have ever p.p.、(2)同種: of（比較対象と同じ種類）、(3)異種: in（比較対象と異なる種類）。"},
    # hco-009: 比較（慣用表現）
    {"node_id": "hco-009", "seq": 1, "question": "not so much A as B の意味は？", "answer": "「AというよりむしろB」。もとは原級の否定形 not so 〜 as ... の文で、「BほどAではない」が原義。"},
    {"node_id": "hco-009", "seq": 2, "question": "no more A than B の意味は？", "answer": "「Bと同様にAではない」。両者否定の表現。"},
    {"node_id": "hco-009", "seq": 3, "question": "The+比較級〜, the+比較級... のうしろの the の役割は？", "answer": "指示副詞で「それだけ」と前文を指す。最初のtheは接続語の役割。"},
    {"node_id": "hco-009", "seq": 4, "question": "最上級相当表現の2つのパターンは？", "answer": "(1) No other+単数名詞 is as [so] 〜 as A.（Aが一番）、(2) S V 比較級 than any other 単数名詞.（Sが一番）。"},
    # hco-010: 複合関係詞
    {"node_id": "hco-010", "seq": 1, "question": "複合関係代名詞を3つ挙げよ。", "answer": "whoever（たとえだれが〜でも）、whatever（たとえ何が〜でも）、whichever（たとえどちらが〜でも）。"},
    {"node_id": "hco-010", "seq": 2, "question": "複合関係副詞を3つ挙げよ。", "answer": "whenever（たとえいつ〜でも）、wherever（たとえどこに〜でも）、however（たとえどれほど〜でも）。"},
    {"node_id": "hco-010", "seq": 3, "question": "howeverの特徴は？", "answer": "多くの場合、うしろに形容詞または副詞をともなう（例: However busy he is）。"},
    {"node_id": "hco-010", "seq": 4, "question": "Whatever happens は no matter を使ってどう書き換えるか？", "answer": "No matter what happens."},
]

# ============================================================
# 4. NODE_PREREQUISITES
# ============================================================

NODE_PREREQUISITES = [
    {"node_id": "hco-009", "prerequisite_id": "hco-008"},
]

# ============================================================
# 5. KNOWLEDGE_REFERENCES
# ============================================================

KNOWLEDGE_REFERENCES = [
    {"node_id": "hco-005", "book": "肘井の読解のための英文法", "section_id": "Hij_18", "pages": "p.126-129"},
    {"node_id": "hco-006", "book": "肘井の読解のための英文法", "section_id": "Hij_19", "pages": "p.129-135"},
    {"node_id": "hco-007", "book": "肘井の読解のための英文法", "section_id": "Hij_20", "pages": "p.136-141"},
    {"node_id": "hco-008", "book": "肘井の読解のための英文法", "section_id": "Hij_21_1", "pages": "p.141-147"},
    {"node_id": "hco-009", "book": "肘井の読解のための英文法", "section_id": "Hij_21_2", "pages": "p.148-151"},
    {"node_id": "hco-010", "book": "肘井の読解のための英文法", "section_id": "Hij_22", "pages": "p.152-155"},
]

# ============================================================
# 6. SECTIONS
# ============================================================

SECTIONS = [
    {
        "id": "Hij_18",
        "book": "肘井の読解のための英文法",
        "title": "Theme 18 呼応で英文が読める",
        "pages": "p.126-129",
        "type": "drill",
    },
    {
        "id": "Hij_19",
        "book": "肘井の読解のための英文法",
        "title": "Theme 19 ネクサスで英文が読める",
        "pages": "p.129-135",
        "type": "drill",
    },
    {
        "id": "Hij_20",
        "book": "肘井の読解のための英文法",
        "title": "Theme 20 挿入で英文が読める",
        "pages": "p.136-141",
        "type": "drill",
    },
    {
        "id": "Hij_21_1",
        "book": "肘井の読解のための英文法",
        "title": "Theme 21 比較で英文が読める①",
        "pages": "p.141-147",
        "type": "drill",
    },
    {
        "id": "Hij_21_2",
        "book": "肘井の読解のための英文法",
        "title": "Theme 21 比較で英文が読める②",
        "pages": "p.148-151",
        "type": "drill",
    },
    {
        "id": "Hij_22",
        "book": "肘井の読解のための英文法",
        "title": "Theme 22 複合関係詞で英文が読める",
        "pages": "p.152-155",
        "type": "drill",
    },
]

# ============================================================
# 7. SECTION_PREREQUISITES
# ============================================================

SECTION_PREREQUISITES = [
    {"section_id": "Hij_21_2", "prerequisite_id": "Hij_21_1"},
]

# ============================================================
# 8. SECTION_KNOWLEDGE_NODES
# ============================================================

SECTION_KNOWLEDGE_NODES = [
    {"section_id": "Hij_18", "node_id": "hco-005", "seq": 1},
    {"section_id": "Hij_19", "node_id": "hco-006", "seq": 1},
    {"section_id": "Hij_20", "node_id": "hco-007", "seq": 1},
    {"section_id": "Hij_21_1", "node_id": "hco-008", "seq": 1},
    {"section_id": "Hij_21_2", "node_id": "hco-009", "seq": 1},
    {"section_id": "Hij_22", "node_id": "hco-010", "seq": 1},
]

# ============================================================
# 9. SENTENCES
# ============================================================

SENTENCES = [
    # ==========================================================
    # Hij_18 — Theme 18 呼応で英文が読める
    # ==========================================================
    # ----------------------------------------------------------
    # Hij_18 — 例題 (5問)
    # ----------------------------------------------------------
    {
        "id": "hij-18-e1-01",
        "section_id": "Hij_18",
        "drill": 1,
        "number": 1,
        "role": "example",
        "english": "Living in a city has both advantages and disadvantages.",
        "japanese": "都市で暮らすことは、利点と不利な点の両方がある。",
        "notes": None,
    },
    {
        "id": "hij-18-e1-02",
        "section_id": "Hij_18",
        "drill": 1,
        "number": 2,
        "role": "example",
        "english": "The question is not whether we will die, but how we will live.",
        "japanese": "問題は私たちが死ぬかどうかではなくて、どう生きるかだ。",
        "notes": None,
    },
    {
        "id": "hij-18-e1-03",
        "section_id": "Hij_18",
        "drill": 1,
        "number": 3,
        "role": "example",
        "english": "We need not only good language skills but clear thinking.",
        "japanese": "私たちはすぐれた言語技術だけでなく、はっきりとした思考も必要だ。",
        "notes": None,
    },
    {
        "id": "hij-18-e1-04",
        "section_id": "Hij_18",
        "drill": 1,
        "number": 4,
        "role": "example",
        "english": "You can either fill in this form or email us.",
        "japanese": "あなたはこの申込用紙に記入しても、われわれにＥメールを送ってもよい。",
        "notes": None,
    },
    {
        "id": "hij-18-e1-05",
        "section_id": "Hij_18",
        "drill": 1,
        "number": 5,
        "role": "example",
        "english": "They had neither met the author nor read any of his books.",
        "japanese": "その人たちは、その作者に会ったこともないし、その作者の本を1冊も読んだことがなかった。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_18 — 確認問題 (3問)
    # ----------------------------------------------------------
    {
        "id": "hij-18-c1-01",
        "section_id": "Hij_18",
        "drill": 2,
        "number": 1,
        "role": "practice",
        "english": "I study English not because it is useful, but because that study gives me pleasure.",
        "japanese": "私が英語を勉強するのは、それが役に立つからではなくて、その勉強が私に喜びを与えてくれるからだ。",
        "notes": None,
    },
    {
        "id": "hij-18-c1-02",
        "section_id": "Hij_18",
        "drill": 2,
        "number": 2,
        "role": "practice",
        "english": "This is true not only of national cultures but also of organizational cultures.",
        "japanese": "これは国の文化だけでなく、組織の文化にもあてはまる。",
        "notes": None,
    },
    {
        "id": "hij-18-c1-03",
        "section_id": "Hij_18",
        "drill": 2,
        "number": 3,
        "role": "practice",
        "english": "Either Mike or I have to go to work in the evening.",
        "japanese": "マイクか私が、夕方職場に行かなければならない。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_18 — 発展問題 (1問)
    # ----------------------------------------------------------
    {
        "id": "hij-18-a1-01",
        "section_id": "Hij_18",
        "drill": 3,
        "number": 1,
        "role": "advanced",
        "english": "What matters is not just the number of years of education people get, but its content.",
        "japanese": "重要なことは、人びとが受ける教育の年数だけではなくて、その中身もだ。",
        "notes": "名古屋市立大",
    },
    # ==========================================================
    # Hij_19 — Theme 19 ネクサスで英文が読める
    # ==========================================================
    # ----------------------------------------------------------
    # Hij_19 — 例題 (5問)
    # ----------------------------------------------------------
    {
        "id": "hij-19-e1-01",
        "section_id": "Hij_19",
        "drill": 1,
        "number": 1,
        "role": "example",
        "english": "She saw her mother enter the neighbor's house.",
        "japanese": "彼女は、母親が隣人の家に入るのを見た。",
        "notes": None,
    },
    {
        "id": "hij-19-e1-02",
        "section_id": "Hij_19",
        "drill": 1,
        "number": 2,
        "role": "example",
        "english": "The best way is for us to understand each other.",
        "japanese": "最善の方法は、私たちがお互いを理解することだ。",
        "notes": None,
    },
    {
        "id": "hij-19-e1-03",
        "section_id": "Hij_19",
        "drill": 1,
        "number": 3,
        "role": "example",
        "english": "His getting up so early surprised all his friends.",
        "japanese": "彼がそんなに早く起きたことが、友人全員を驚かせた。",
        "notes": None,
    },
    {
        "id": "hij-19-e1-04",
        "section_id": "Hij_19",
        "drill": 1,
        "number": 4,
        "role": "example",
        "english": "The building being in danger of falling down, they have escaped.",
        "japanese": "その建物は倒壊の危機にあったので、その人たちは逃げ出した。",
        "notes": None,
    },
    {
        "id": "hij-19-e1-05",
        "section_id": "Hij_19",
        "drill": 1,
        "number": 5,
        "role": "example",
        "english": "She couldn't sing a song with him standing there.",
        "japanese": "彼女は彼がそこに立っていると歌えなかった。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_19 — 確認問題 (5問)
    # ----------------------------------------------------------
    {
        "id": "hij-19-c1-01",
        "section_id": "Hij_19",
        "drill": 2,
        "number": 1,
        "role": "practice",
        "english": "I never heard him speak ill of others.",
        "japanese": "私は、彼が他人の悪口を言うのを聞いたことがなかった。",
        "notes": None,
    },
    {
        "id": "hij-19-c1-02",
        "section_id": "Hij_19",
        "drill": 2,
        "number": 2,
        "role": "practice",
        "english": "It being a fine day yesterday, I took my son to the river.",
        "japanese": "昨日は晴れていたので、私は息子を川に連れて行った。",
        "notes": None,
    },
    {
        "id": "hij-19-c1-03",
        "section_id": "Hij_19",
        "drill": 2,
        "number": 3,
        "role": "practice",
        "english": "It is necessary for us to follow his advice.",
        "japanese": "私たちが彼のアドバイスに従うことは必要だ。",
        "notes": None,
    },
    {
        "id": "hij-19-c1-04",
        "section_id": "Hij_19",
        "drill": 2,
        "number": 4,
        "role": "practice",
        "english": "I'm not proud of my family being rich.",
        "japanese": "私は家族がお金持ちであることを誇りに思っていない。",
        "notes": None,
    },
    {
        "id": "hij-19-c1-05",
        "section_id": "Hij_19",
        "drill": 2,
        "number": 5,
        "role": "practice",
        "english": "He couldn't concentrate on his reading with her watching him.",
        "japanese": "彼は彼女が自分を見ている状況では、読書に集中できなかった。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_19 — 発展問題 (1問)
    # ----------------------------------------------------------
    {
        "id": "hij-19-a1-01",
        "section_id": "Hij_19",
        "drill": 3,
        "number": 1,
        "role": "advanced",
        "english": "The large white area in human eyes makes it easy for us to see the direction of other people's gaze.",
        "japanese": "人間の目の大きな白い部分が、私たちが他人の視線の方向を見ることを容易にする。",
        "notes": "福島県立医科大",
    },
    # ==========================================================
    # Hij_20 — Theme 20 挿入で英文が読める
    # ==========================================================
    # ----------------------------------------------------------
    # Hij_20 — 例題 (5問)
    # ----------------------------------------------------------
    {
        "id": "hij-20-e1-01",
        "section_id": "Hij_20",
        "drill": 1,
        "number": 1,
        "role": "example",
        "english": "This statue, made in the 1600s, is the oldest around here.",
        "japanese": "この像は1600年代につくられて、このあたりで最も古いものだ。",
        "notes": None,
    },
    {
        "id": "hij-20-e1-02",
        "section_id": "Hij_20",
        "drill": 1,
        "number": 2,
        "role": "example",
        "english": "The tree, which is almost bare now, is a very old one.",
        "japanese": "その木はいまはほとんど葉がなくて、とても年季の入ったものだ。",
        "notes": None,
    },
    {
        "id": "hij-20-e1-03",
        "section_id": "Hij_20",
        "drill": 1,
        "number": 3,
        "role": "example",
        "english": "The twin brothers, Tom and Mike, have a lot in common.",
        "japanese": "双子の兄弟でトムとマイクは、多くの共通点がある。",
        "notes": None,
    },
    {
        "id": "hij-20-e1-04",
        "section_id": "Hij_20",
        "drill": 1,
        "number": 4,
        "role": "example",
        "english": "Speech, as a means of communication, is of importance.",
        "japanese": "話すことは、コミュニケーションの手段として重要だ。",
        "notes": None,
    },
    {
        "id": "hij-20-e1-05",
        "section_id": "Hij_20",
        "drill": 1,
        "number": 5,
        "role": "example",
        "english": "The movie, I think, is not interesting.",
        "japanese": "その映画はおもしろくないと、私は思う。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_20 — 確認問題 (3問)
    # ----------------------------------------------------------
    {
        "id": "hij-20-c1-01",
        "section_id": "Hij_20",
        "drill": 2,
        "number": 1,
        "role": "practice",
        "english": "Oregano, which is used in Italian food, is a plant with small leaves.",
        "japanese": "オレガノは、イタリア料理で使用されていて、小さな葉をつけた植物だ。",
        "notes": None,
    },
    {
        "id": "hij-20-c1-02",
        "section_id": "Hij_20",
        "drill": 2,
        "number": 2,
        "role": "practice",
        "english": "The company, founded in 1950, is probably the best known in Korea.",
        "japanese": "その会社は、1950年に設立されて、おそらく韓国で最も有名だ。",
        "notes": None,
    },
    {
        "id": "hij-20-c1-03",
        "section_id": "Hij_20",
        "drill": 2,
        "number": 3,
        "role": "practice",
        "english": "My teacher, a former professional baseball player, is coaching the school team.",
        "japanese": "私の先生は、以前はプロ野球選手で、その学校のチームのコーチをしている。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_20 — 発展問題 (1問)
    # ----------------------------------------------------------
    {
        "id": "hij-20-a1-01",
        "section_id": "Hij_20",
        "drill": 3,
        "number": 1,
        "role": "advanced",
        "english": "What makes them successful, given the basic ability to succeed, is that they are in jobs that are good matches to their styles of thinking.",
        "japanese": "なぜその人たちが成功するかは、成功する基本的な能力を前提とすると、自分たちの思考スタイルによく合った仕事についていることが理由だ。",
        "notes": "青山学院大",
    },
    # ==========================================================
    # Hij_21_1 — Theme 21 比較で英文が読める①
    # ==========================================================
    # ----------------------------------------------------------
    # Hij_21_1 — 例題 (6問)
    # ----------------------------------------------------------
    {
        "id": "hij-21-e1-01",
        "section_id": "Hij_21_1",
        "drill": 1,
        "number": 1,
        "role": "example",
        "english": "Mrs. Ryan is not as young as she looks.",
        "japanese": "ライアンさんは、見た目ほど若くはない。",
        "notes": None,
    },
    {
        "id": "hij-21-e1-02",
        "section_id": "Hij_21_1",
        "drill": 1,
        "number": 2,
        "role": "example",
        "english": "It doesn't snow here now as much as it used to.",
        "japanese": "以前ほど、現在はここでは雪が降らない。",
        "notes": None,
    },
    {
        "id": "hij-21-e1-03",
        "section_id": "Hij_21_1",
        "drill": 1,
        "number": 3,
        "role": "example",
        "english": "The relationship between them is not as good as it should be.",
        "japanese": "その人たちの関係は、本来あるべきもののほどよくはない。",
        "notes": None,
    },
    {
        "id": "hij-21-e1-04",
        "section_id": "Hij_21_1",
        "drill": 1,
        "number": 4,
        "role": "example",
        "english": "The building is much older than they think.",
        "japanese": "その建物は、その人たちが思っているよりずっと古い。",
        "notes": None,
    },
    {
        "id": "hij-21-e1-05",
        "section_id": "Hij_21_1",
        "drill": 1,
        "number": 5,
        "role": "example",
        "english": "This is the best movie that I have ever seen.",
        "japanese": "これは、私がいままで見たなかで最高の映画だ。",
        "notes": None,
    },
    {
        "id": "hij-21-e1-06",
        "section_id": "Hij_21_1",
        "drill": 1,
        "number": 6,
        "role": "example",
        "english": "This comic is the most interesting of all the comics.",
        "japanese": "この漫画は、すべての漫画のなかで最もおもしろい。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_21_1 — 確認問題 (5問)
    # ----------------------------------------------------------
    {
        "id": "hij-21-c1-01",
        "section_id": "Hij_21_1",
        "drill": 2,
        "number": 1,
        "role": "practice",
        "english": "The question is not so serious as it seems.",
        "japanese": "その問題は、見た目ほど（実際は）深刻ではない。",
        "notes": None,
    },
    {
        "id": "hij-21-c1-02",
        "section_id": "Hij_21_1",
        "drill": 2,
        "number": 2,
        "role": "practice",
        "english": "There are more college students than there were in the 1950s.",
        "japanese": "1950年代より、現代は多くの大学生がいる。",
        "notes": None,
    },
    {
        "id": "hij-21-c1-03",
        "section_id": "Hij_21_1",
        "drill": 2,
        "number": 3,
        "role": "practice",
        "english": "Of Mary's five brothers, Mike is the most talented.",
        "japanese": "メアリーの5人兄弟のなかで、マイクは最も才能がある。",
        "notes": None,
    },
    {
        "id": "hij-21-c1-04",
        "section_id": "Hij_21_1",
        "drill": 2,
        "number": 4,
        "role": "practice",
        "english": "It was the best book I had ever read.",
        "japanese": "それは私がそれまで読んだなかで最高の本だった。",
        "notes": None,
    },
    {
        "id": "hij-21-c1-05",
        "section_id": "Hij_21_1",
        "drill": 2,
        "number": 5,
        "role": "practice",
        "english": "Engineers are more productive at making planes than they are at making shirts.",
        "japanese": "エンジニアは、シャツを作るよりも飛行機を造るほうが、生産性が高い。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_21_1 — 発展問題 (1問)
    # ----------------------------------------------------------
    {
        "id": "hij-21-a1-01",
        "section_id": "Hij_21_1",
        "drill": 3,
        "number": 1,
        "role": "advanced",
        "english": "People walk faster in wealthy cities like Tokyo and Toronto than they do in cities like Nairobi and Jakarta.",
        "japanese": "人びとは、ナイロビやジャカルタのような都市よりも、東京やトロントのような裕福な都市のほうが速く歩く。",
        "notes": "東北大",
    },
    # ==========================================================
    # Hij_21_2 — Theme 21 比較で英文が読める②
    # ==========================================================
    # ----------------------------------------------------------
    # Hij_21_2 — 例題 (5問)
    # ----------------------------------------------------------
    {
        "id": "hij-21-e4-01",
        "section_id": "Hij_21_2",
        "drill": 1,
        "number": 1,
        "role": "example",
        "english": "He is not so much a singer as a poet.",
        "japanese": "彼は歌手というよりむしろ詩人だ。",
        "notes": None,
    },
    {
        "id": "hij-21-e4-02",
        "section_id": "Hij_21_2",
        "drill": 1,
        "number": 2,
        "role": "example",
        "english": "Tom can no more swim than Mary can.",
        "japanese": "トムはメアリーと同様にまったく泳げない。",
        "notes": None,
    },
    {
        "id": "hij-21-e4-03",
        "section_id": "Hij_21_2",
        "drill": 1,
        "number": 3,
        "role": "example",
        "english": "The more books you read, the more you'll know.",
        "japanese": "本を多く読めば読むほど、それだけ物知りになる。",
        "notes": None,
    },
    {
        "id": "hij-21-e4-04",
        "section_id": "Hij_21_2",
        "drill": 1,
        "number": 4,
        "role": "example",
        "english": "No other sport in Brazil is as popular as soccer.",
        "japanese": "ブラジルで、サッカーほど人気のスポーツはない。",
        "notes": None,
    },
    {
        "id": "hij-21-e4-05",
        "section_id": "Hij_21_2",
        "drill": 1,
        "number": 5,
        "role": "example",
        "english": "She sings better than any other girl in her class.",
        "japanese": "彼女は、クラスのほかのどの女の子よりも歌がうまい。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_21_2 — 確認問題 (4問)
    # ----------------------------------------------------------
    {
        "id": "hij-21-c2-01",
        "section_id": "Hij_21_2",
        "drill": 2,
        "number": 1,
        "role": "practice",
        "english": "The shrine is older than any other building in the town.",
        "japanese": "その神社は、その町のほかのどの建物よりも古い。",
        "notes": None,
    },
    {
        "id": "hij-21-c2-02",
        "section_id": "Hij_21_2",
        "drill": 2,
        "number": 2,
        "role": "practice",
        "english": "She has succeeded not so much by looks as by efforts.",
        "japanese": "彼女は、見た目というよりむしろ努力で成功した。",
        "notes": None,
    },
    {
        "id": "hij-21-c2-03",
        "section_id": "Hij_21_2",
        "drill": 2,
        "number": 3,
        "role": "practice",
        "english": "She is no more young than her mother.",
        "japanese": "彼女は、彼女の母親と同様に若くはない。",
        "notes": None,
    },
    {
        "id": "hij-21-c2-04",
        "section_id": "Hij_21_2",
        "drill": 2,
        "number": 4,
        "role": "practice",
        "english": "The older you are, the more likely you are to have a heart attack.",
        "japanese": "年をとればとるほど、それだけますます心臓発作を起こす可能性が高くなる。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_21_2 — 発展問題 (1問)
    # ----------------------------------------------------------
    {
        "id": "hij-21-a2-01",
        "section_id": "Hij_21_2",
        "drill": 3,
        "number": 1,
        "role": "advanced",
        "english": "We do not so much believe what we see as see what we believe.",
        "japanese": "私たちは、見るものを信じるというよりむしろ、信じるものを見る。",
        "notes": "弘前大",
    },
    # ==========================================================
    # Hij_22 — Theme 22 複合関係詞で英文が読める
    # ==========================================================
    # ----------------------------------------------------------
    # Hij_22 — 例題 (5問)
    # ----------------------------------------------------------
    {
        "id": "hij-22-e1-01",
        "section_id": "Hij_22",
        "drill": 1,
        "number": 1,
        "role": "example",
        "english": "Whoever visits that country will love it.",
        "japanese": "たとえだれがその国を訪れても、大好きになるだろう。",
        "notes": None,
    },
    {
        "id": "hij-22-e1-02",
        "section_id": "Hij_22",
        "drill": 1,
        "number": 2,
        "role": "example",
        "english": "Whatever happens, we must return home by seven.",
        "japanese": "たとえ何が起きても、私たちは7時までに家に帰らなければならない。",
        "notes": None,
    },
    {
        "id": "hij-22-e1-03",
        "section_id": "Hij_22",
        "drill": 1,
        "number": 3,
        "role": "example",
        "english": "Whenever he comes to this place, he orders the same dish.",
        "japanese": "たとえ彼はいつこの場所へ来ても、同じ料理を注文する。",
        "notes": None,
    },
    {
        "id": "hij-22-e1-04",
        "section_id": "Hij_22",
        "drill": 1,
        "number": 4,
        "role": "example",
        "english": "Mike accompanies his sister wherever she may go.",
        "japanese": "マイクはたとえ妹がどこに行こうとも、ついて行く。",
        "notes": None,
    },
    {
        "id": "hij-22-e1-05",
        "section_id": "Hij_22",
        "drill": 1,
        "number": 5,
        "role": "example",
        "english": "However busy he is, he finds time for his friends.",
        "japanese": "たとえどれほど忙しくても、彼は友人のための時間を見つけ出す。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_22 — 確認問題 (4問)
    # ----------------------------------------------------------
    {
        "id": "hij-22-c1-01",
        "section_id": "Hij_22",
        "drill": 2,
        "number": 1,
        "role": "practice",
        "english": "Give this candy to whoever wants to eat it.",
        "japanese": "これを食べたい人にはだれにでもこのキャンディーをあげなさい。",
        "notes": None,
    },
    {
        "id": "hij-22-c1-02",
        "section_id": "Hij_22",
        "drill": 2,
        "number": 2,
        "role": "practice",
        "english": "Whenever I ask to speak to him, the secretary always says he is in a meeting.",
        "japanese": "たとえいつ彼と話させてくれと頼んでも、秘書はいつも会議中だと言う。",
        "notes": None,
    },
    {
        "id": "hij-22-c1-03",
        "section_id": "Hij_22",
        "drill": 2,
        "number": 3,
        "role": "practice",
        "english": "I would rather have a room of my own, however small it is.",
        "japanese": "たとえどれほど小さくても、自分の部屋がほしい。",
        "notes": None,
    },
    {
        "id": "hij-22-c1-04",
        "section_id": "Hij_22",
        "drill": 2,
        "number": 4,
        "role": "practice",
        "english": "No matter what happens, your parents love you.",
        "japanese": "たとえ何が起きても、あなたの両親はあなたを愛している。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_22 — 発展問題 (1問)
    # ----------------------------------------------------------
    {
        "id": "hij-22-a1-01",
        "section_id": "Hij_22",
        "drill": 3,
        "number": 1,
        "role": "advanced",
        "english": "However much of all this you know, you did not find it out by observation.",
        "japanese": "このことをどれほど多く知っていても、あなたは観察によってそれを発見したのではない。",
        "notes": "三重大",
    },
]

# ============================================================
# 10. SENTENCE_STRUCTURES
# ============================================================

SENTENCE_STRUCTURES = [
    # ==========================================================
    # Hij_18 — 呼応
    # ==========================================================
    # --- hij-18-e1-01 ---
    {"sentence_id": "hij-18-e1-01", "label": "overall", "value": "S V O"},
    {"sentence_id": "hij-18-e1-01", "label": "details", "value": "<Living in a city>(S:動名詞句) has(V) both advantages and disadvantages(O)"},
    # --- hij-18-e1-02 ---
    {"sentence_id": "hij-18-e1-02", "label": "overall", "value": "S V C"},
    {"sentence_id": "hij-18-e1-02", "label": "details", "value": "The question(S) is(V) not <whether we will die>(C) but <how we will live>(C)"},
    # --- hij-18-e1-03 ---
    {"sentence_id": "hij-18-e1-03", "label": "overall", "value": "S V O"},
    {"sentence_id": "hij-18-e1-03", "label": "details", "value": "We(S) need(V) not only good language skills but clear thinking(O)"},
    # --- hij-18-e1-04 ---
    {"sentence_id": "hij-18-e1-04", "label": "overall", "value": "S V O / V O"},
    {"sentence_id": "hij-18-e1-04", "label": "details", "value": "You(S) can either fill in(V1) this form(O1) or email(V2) us(O2)"},
    # --- hij-18-e1-05 ---
    {"sentence_id": "hij-18-e1-05", "label": "overall", "value": "S V O / V O"},
    {"sentence_id": "hij-18-e1-05", "label": "details", "value": "They(S) had neither met(V1) the author(O1) nor read(V2) any of his books(O2)"},
    # --- hij-18-c1-01 ---
    {"sentence_id": "hij-18-c1-01", "label": "overall", "value": "S V O M"},
    {"sentence_id": "hij-18-c1-01", "label": "details", "value": "I(S) study(V) English(O) [not because it is useful, but because that study gives me pleasure](M)"},
    # --- hij-18-c1-02 ---
    {"sentence_id": "hij-18-c1-02", "label": "overall", "value": "S V C M"},
    {"sentence_id": "hij-18-c1-02", "label": "details", "value": "This(S) is(V) true(C) [not only of national cultures but also of organizational cultures](M)"},
    # --- hij-18-c1-03 ---
    {"sentence_id": "hij-18-c1-03", "label": "overall", "value": "S V M M"},
    {"sentence_id": "hij-18-c1-03", "label": "details", "value": "Either Mike or I(S) have to go(V) [to work](M) [in the evening](M)"},
    # --- hij-18-a1-01 ---
    {"sentence_id": "hij-18-a1-01", "label": "overall", "value": "S V C"},
    {"sentence_id": "hij-18-a1-01", "label": "details", "value": "<What matters>(S:名詞節) is(V) not just the number of years of education (people get)(M:関係代名詞省略) but its content(C)"},
    # ==========================================================
    # Hij_19 — ネクサス
    # ==========================================================
    # --- hij-19-e1-01 ---
    {"sentence_id": "hij-19-e1-01", "label": "overall", "value": "S V O C"},
    {"sentence_id": "hij-19-e1-01", "label": "details", "value": "She(S) saw(V) her mother(O/S') enter(C/V') the neighbor's house"},
    # --- hij-19-e1-02 ---
    {"sentence_id": "hij-19-e1-02", "label": "overall", "value": "S V C"},
    {"sentence_id": "hij-19-e1-02", "label": "details", "value": "The best way(S) is(V) <for us(S') to understand(V') each other>(C:不定詞句)"},
    # --- hij-19-e1-03 ---
    {"sentence_id": "hij-19-e1-03", "label": "overall", "value": "S V O"},
    {"sentence_id": "hij-19-e1-03", "label": "details", "value": "<His(S') getting up(V') so early>(S:動名詞句) surprised(V) all his friends(O)"},
    # --- hij-19-e1-04 ---
    {"sentence_id": "hij-19-e1-04", "label": "overall", "value": "M S V"},
    {"sentence_id": "hij-19-e1-04", "label": "details", "value": "[The building(S') being(V') in danger of falling down](M:独立分詞構文) they(S) have escaped(V)"},
    # --- hij-19-e1-05 ---
    {"sentence_id": "hij-19-e1-05", "label": "overall", "value": "S V O M"},
    {"sentence_id": "hij-19-e1-05", "label": "details", "value": "She(S) couldn't sing(V) a song(O) [with him(S') standing(V') there](M:付帯状況with)"},
    # --- hij-19-c1-01 ---
    {"sentence_id": "hij-19-c1-01", "label": "overall", "value": "S V O C"},
    {"sentence_id": "hij-19-c1-01", "label": "details", "value": "I(S) never heard(V) him(O/S') speak(C/V') ill of others"},
    # --- hij-19-c1-02 ---
    {"sentence_id": "hij-19-c1-02", "label": "overall", "value": "M S V O M"},
    {"sentence_id": "hij-19-c1-02", "label": "details", "value": "[It(S') being(V') a fine day yesterday](M:独立分詞構文) I(S) took(V) my son(O) [to the river](M)"},
    # --- hij-19-c1-03 ---
    {"sentence_id": "hij-19-c1-03", "label": "overall", "value": "S V C"},
    {"sentence_id": "hij-19-c1-03", "label": "details", "value": "It(S:形式主語) is(V) necessary(C) <for us(S') to follow(V') his advice>(真S)"},
    # --- hij-19-c1-04 ---
    {"sentence_id": "hij-19-c1-04", "label": "overall", "value": "S V O"},
    {"sentence_id": "hij-19-c1-04", "label": "details", "value": "I'm(S V) not proud of(O) <my family(S') being(V') rich>(動名詞句)"},
    # --- hij-19-c1-05 ---
    {"sentence_id": "hij-19-c1-05", "label": "overall", "value": "S V O M"},
    {"sentence_id": "hij-19-c1-05", "label": "details", "value": "He(S) couldn't concentrate on(V) his reading(O) [with her(S') watching(V') him](M:付帯状況with)"},
    # --- hij-19-a1-01 ---
    {"sentence_id": "hij-19-a1-01", "label": "overall", "value": "S V O C"},
    {"sentence_id": "hij-19-a1-01", "label": "details", "value": "The large white area in human eyes(S) makes(V) it(O:形式目的語) easy(C) <for us(S') to see(V') the direction of other people's gaze>(真O)"},
    # ==========================================================
    # Hij_20 — 挿入
    # ==========================================================
    # --- hij-20-e1-01 ---
    {"sentence_id": "hij-20-e1-01", "label": "overall", "value": "S ,M, V C M"},
    {"sentence_id": "hij-20-e1-01", "label": "details", "value": "This statue(S) ,made in the 1600s(M:分詞構文挿入), is(V) the oldest(C) [around here](M)"},
    # --- hij-20-e1-02 ---
    {"sentence_id": "hij-20-e1-02", "label": "overall", "value": "S ,M, V C"},
    {"sentence_id": "hij-20-e1-02", "label": "details", "value": "The tree(S) ,which is almost bare now(M:関係詞節挿入), is(V) a very old one(C)"},
    # --- hij-20-e1-03 ---
    {"sentence_id": "hij-20-e1-03", "label": "overall", "value": "S ,S', V O M"},
    {"sentence_id": "hij-20-e1-03", "label": "details", "value": "The twin brothers(S) ,Tom and Mike(S':同格挿入), have(V) a lot(O) [in common](M)"},
    # --- hij-20-e1-04 ---
    {"sentence_id": "hij-20-e1-04", "label": "overall", "value": "S ,M, V C"},
    {"sentence_id": "hij-20-e1-04", "label": "details", "value": "Speech(S) ,as a means of communication(M:前置詞句挿入), is(V) of importance(C:=important)"},
    # --- hij-20-e1-05 ---
    {"sentence_id": "hij-20-e1-05", "label": "overall", "value": "S ,M, V C"},
    {"sentence_id": "hij-20-e1-05", "label": "details", "value": "The movie(S) ,I think(M:SV挿入), is not(V) interesting(C)"},
    # --- hij-20-c1-01 ---
    {"sentence_id": "hij-20-c1-01", "label": "overall", "value": "S ,M, V C M"},
    {"sentence_id": "hij-20-c1-01", "label": "details", "value": "Oregano(S) ,which is used in Italian food(M:関係詞節挿入), is(V) a plant(C) (with small leaves)(M)"},
    # --- hij-20-c1-02 ---
    {"sentence_id": "hij-20-c1-02", "label": "overall", "value": "S ,M, V M C M"},
    {"sentence_id": "hij-20-c1-02", "label": "details", "value": "The company(S) ,founded in 1950(M:分詞構文挿入), is(V) probably(M) the best known(C) [in Korea](M)"},
    # --- hij-20-c1-03 ---
    {"sentence_id": "hij-20-c1-03", "label": "overall", "value": "S ,S', V O"},
    {"sentence_id": "hij-20-c1-03", "label": "details", "value": "My teacher(S) ,a former professional baseball player(S':同格挿入), is coaching(V) the school team(O)"},
    # --- hij-20-a1-01 ---
    {"sentence_id": "hij-20-a1-01", "label": "overall", "value": "S ,M, V C"},
    {"sentence_id": "hij-20-a1-01", "label": "details", "value": "<What makes them successful>(S:名詞節) ,given the basic ability to succeed(M:分詞構文挿入), is(V) <that they are in jobs (that are good matches to their styles of thinking)>(C:名詞節)"},
    # ==========================================================
    # Hij_21_1 — 比較①
    # ==========================================================
    # --- hij-21-e1-01 ---
    {"sentence_id": "hij-21-e1-01", "label": "overall", "value": "S V C M"},
    {"sentence_id": "hij-21-e1-01", "label": "details", "value": "Mrs. Ryan(S) is(V) not as young(C) [as she looks](M:原級否定)"},
    # --- hij-21-e1-02 ---
    {"sentence_id": "hij-21-e1-02", "label": "overall", "value": "S V M M M M"},
    {"sentence_id": "hij-21-e1-02", "label": "details", "value": "It(S) doesn't snow(V) here(M) now(M) as much(M) [as it used to](M:原級否定)"},
    # --- hij-21-e1-03 ---
    {"sentence_id": "hij-21-e1-03", "label": "overall", "value": "S (M) V C M"},
    {"sentence_id": "hij-21-e1-03", "label": "details", "value": "The relationship(S) (between them)(M) is(V) not as good(C) [as it should be](M:原級否定)"},
    # --- hij-21-e1-04 ---
    {"sentence_id": "hij-21-e1-04", "label": "overall", "value": "S V C M"},
    {"sentence_id": "hij-21-e1-04", "label": "details", "value": "The building(S) is(V) much older(C:比較級+強調) [than they think](M)"},
    # --- hij-21-e1-05 ---
    {"sentence_id": "hij-21-e1-05", "label": "overall", "value": "S V C (M)"},
    {"sentence_id": "hij-21-e1-05", "label": "details", "value": "This(S) is(V) the best movie(C:最上級) (that I have ever seen)(M:経験の範囲)"},
    # --- hij-21-e1-06 ---
    {"sentence_id": "hij-21-e1-06", "label": "overall", "value": "S V C M"},
    {"sentence_id": "hij-21-e1-06", "label": "details", "value": "This comic(S) is(V) the most interesting(C:最上級) [of all the comics](M:同種ofの範囲)"},
    # --- hij-21-c1-01 ---
    {"sentence_id": "hij-21-c1-01", "label": "overall", "value": "S V C M"},
    {"sentence_id": "hij-21-c1-01", "label": "details", "value": "The question(S) is(V) not so serious(C) [as it seems](M:原級否定)"},
    # --- hij-21-c1-02 ---
    {"sentence_id": "hij-21-c1-02", "label": "overall", "value": "M V S M"},
    {"sentence_id": "hij-21-c1-02", "label": "details", "value": "There(M) are(V) more college students(S:比較級) [than there were in the 1950s](M)"},
    # --- hij-21-c1-03 ---
    {"sentence_id": "hij-21-c1-03", "label": "overall", "value": "M S V C"},
    {"sentence_id": "hij-21-c1-03", "label": "details", "value": "[Of Mary's five brothers](M:同種ofの範囲) Mike(S) is(V) the most talented(C:最上級)"},
    # --- hij-21-c1-04 ---
    {"sentence_id": "hij-21-c1-04", "label": "overall", "value": "S V C (M)"},
    {"sentence_id": "hij-21-c1-04", "label": "details", "value": "It(S) was(V) the best book(C:最上級) (I had ever read)(M:経験の範囲/関係代名詞省略)"},
    # --- hij-21-c1-05 ---
    {"sentence_id": "hij-21-c1-05", "label": "overall", "value": "S V C M M"},
    {"sentence_id": "hij-21-c1-05", "label": "details", "value": "Engineers(S) are(V) more productive(C:比較級) [at making planes](M) [than they are at making shirts](M)"},
    # --- hij-21-a1-01 ---
    {"sentence_id": "hij-21-a1-01", "label": "overall", "value": "S V M M M"},
    {"sentence_id": "hij-21-a1-01", "label": "details", "value": "People(S) walk(V) faster(M:比較級) [in wealthy cities like Tokyo and Toronto](M) [than they do in cities like Nairobi and Jakarta](M)"},
    # ==========================================================
    # Hij_21_2 — 比較②
    # ==========================================================
    # --- hij-21-e4-01 ---
    {"sentence_id": "hij-21-e4-01", "label": "overall", "value": "S V C"},
    {"sentence_id": "hij-21-e4-01", "label": "details", "value": "He(S) is(V) not so much a singer(A) as a poet(B) — not so much A as B"},
    # --- hij-21-e4-02 ---
    {"sentence_id": "hij-21-e4-02", "label": "overall", "value": "S V"},
    {"sentence_id": "hij-21-e4-02", "label": "details", "value": "Tom(S) can no more swim(A/V) [than Mary can](B) — no more A than B (両者否定)"},
    # --- hij-21-e4-03 ---
    {"sentence_id": "hij-21-e4-03", "label": "overall", "value": "O S V / O S V"},
    {"sentence_id": "hij-21-e4-03", "label": "details", "value": "The more books(O1) you(S1) read(V1), the more(O2) you'll(S2) know(V2) — The+比較級, the+比較級"},
    # --- hij-21-e4-04 ---
    {"sentence_id": "hij-21-e4-04", "label": "overall", "value": "S (M) V C M"},
    {"sentence_id": "hij-21-e4-04", "label": "details", "value": "No other sport(S) (in Brazil)(M) is(V) as popular(C) [as soccer](M) — 最上級相当表現"},
    # --- hij-21-e4-05 ---
    {"sentence_id": "hij-21-e4-05", "label": "overall", "value": "S V M M"},
    {"sentence_id": "hij-21-e4-05", "label": "details", "value": "She(S) sings(V) better(M:比較級) [than any other girl in her class](M) — 最上級相当表現"},
    # --- hij-21-c2-01 ---
    {"sentence_id": "hij-21-c2-01", "label": "overall", "value": "S V C M"},
    {"sentence_id": "hij-21-c2-01", "label": "details", "value": "The shrine(S) is(V) older(C:比較級) [than any other building in the town](M) — 最上級相当表現"},
    # --- hij-21-c2-02 ---
    {"sentence_id": "hij-21-c2-02", "label": "overall", "value": "S V M"},
    {"sentence_id": "hij-21-c2-02", "label": "details", "value": "She(S) has succeeded(V) not so much by looks(A) as by efforts(B)(M) — not so much A as B"},
    # --- hij-21-c2-03 ---
    {"sentence_id": "hij-21-c2-03", "label": "overall", "value": "S V C M"},
    {"sentence_id": "hij-21-c2-03", "label": "details", "value": "She(S) is(V) no more young(A/C) [than her mother](B/M) — no more A than B (両者否定)"},
    # --- hij-21-c2-04 ---
    {"sentence_id": "hij-21-c2-04", "label": "overall", "value": "C S V / C S V O"},
    {"sentence_id": "hij-21-c2-04", "label": "details", "value": "The older(C1) you(S1) are(V1), the more likely(C2) you(S2) are(V2) to have a heart attack(O) — The+比較級, the+比較級"},
    # --- hij-21-a2-01 ---
    {"sentence_id": "hij-21-a2-01", "label": "overall", "value": "S V O / V O"},
    {"sentence_id": "hij-21-a2-01", "label": "details", "value": "We(S) do not so much believe(V) <what we see>(O:A) as see(V') <what we believe>(O':B) — not so much A as B"},
    # ==========================================================
    # Hij_22 — 複合関係詞
    # ==========================================================
    # --- hij-22-e1-01 ---
    {"sentence_id": "hij-22-e1-01", "label": "overall", "value": "S V O"},
    {"sentence_id": "hij-22-e1-01", "label": "details", "value": "<Whoever visits that country>(S:名詞節/複合関係代名詞) will love(V) it(O)"},
    # --- hij-22-e1-02 ---
    {"sentence_id": "hij-22-e1-02", "label": "overall", "value": "M S V M M"},
    {"sentence_id": "hij-22-e1-02", "label": "details", "value": "[Whatever happens](M:副詞節/複合関係代名詞) we(S) must return(V) home(M) [by seven](M)"},
    # --- hij-22-e1-03 ---
    {"sentence_id": "hij-22-e1-03", "label": "overall", "value": "M S V O"},
    {"sentence_id": "hij-22-e1-03", "label": "details", "value": "[Whenever he comes to this place](M:副詞節/複合関係副詞) he(S) orders(V) the same dish(O)"},
    # --- hij-22-e1-04 ---
    {"sentence_id": "hij-22-e1-04", "label": "overall", "value": "S V O M"},
    {"sentence_id": "hij-22-e1-04", "label": "details", "value": "Mike(S) accompanies(V) his sister(O) [wherever she may go](M:副詞節/複合関係副詞)"},
    # --- hij-22-e1-05 ---
    {"sentence_id": "hij-22-e1-05", "label": "overall", "value": "M S V O M"},
    {"sentence_id": "hij-22-e1-05", "label": "details", "value": "[However busy he is](M:副詞節/複合関係副詞) he(S) finds(V) time(O) [for his friends](M)"},
    # --- hij-22-c1-01 ---
    {"sentence_id": "hij-22-c1-01", "label": "overall", "value": "V O M"},
    {"sentence_id": "hij-22-c1-01", "label": "details", "value": "Give(V) this candy(O) [to <whoever wants to eat it>](M:名詞節/複合関係代名詞)"},
    # --- hij-22-c1-02 ---
    {"sentence_id": "hij-22-c1-02", "label": "overall", "value": "M S V O"},
    {"sentence_id": "hij-22-c1-02", "label": "details", "value": "[Whenever I ask to speak to him](M:副詞節/複合関係副詞) the secretary(S) always says(V) <he is in a meeting>(O)"},
    # --- hij-22-c1-03 ---
    {"sentence_id": "hij-22-c1-03", "label": "overall", "value": "S V O M"},
    {"sentence_id": "hij-22-c1-03", "label": "details", "value": "I(S) would rather have(V) a room of my own(O) [however small it is](M:副詞節/複合関係副詞)"},
    # --- hij-22-c1-04 ---
    {"sentence_id": "hij-22-c1-04", "label": "overall", "value": "M S V O"},
    {"sentence_id": "hij-22-c1-04", "label": "details", "value": "[No matter what happens](M:副詞節/=whatever) your parents(S) love(V) you(O)"},
    # --- hij-22-a1-01 ---
    {"sentence_id": "hij-22-a1-01", "label": "overall", "value": "M S V O M"},
    {"sentence_id": "hij-22-a1-01", "label": "details", "value": "[However much of all this you know](M:副詞節/複合関係副詞) you(S) did not find(V) it(O) out [by observation](M)"},
]

# ============================================================
# 11. SENTENCE_KNOWLEDGE_TAGS
# ============================================================

SENTENCE_KNOWLEDGE_TAGS = [
    # --- Hij_18 例題 ---
    {"sentence_id": "hij-18-e1-01", "node_id": "hco-005"},
    {"sentence_id": "hij-18-e1-02", "node_id": "hco-005"},
    {"sentence_id": "hij-18-e1-03", "node_id": "hco-005"},
    {"sentence_id": "hij-18-e1-04", "node_id": "hco-005"},
    {"sentence_id": "hij-18-e1-05", "node_id": "hco-005"},
    # --- Hij_18 確認問題 ---
    {"sentence_id": "hij-18-c1-01", "node_id": "hco-005"},
    {"sentence_id": "hij-18-c1-02", "node_id": "hco-005"},
    {"sentence_id": "hij-18-c1-03", "node_id": "hco-005"},
    # --- Hij_18 発展問題 ---
    {"sentence_id": "hij-18-a1-01", "node_id": "hco-005"},
    # --- Hij_19 例題 ---
    {"sentence_id": "hij-19-e1-01", "node_id": "hco-006"},
    {"sentence_id": "hij-19-e1-02", "node_id": "hco-006"},
    {"sentence_id": "hij-19-e1-03", "node_id": "hco-006"},
    {"sentence_id": "hij-19-e1-04", "node_id": "hco-006"},
    {"sentence_id": "hij-19-e1-05", "node_id": "hco-006"},
    # --- Hij_19 確認問題 ---
    {"sentence_id": "hij-19-c1-01", "node_id": "hco-006"},
    {"sentence_id": "hij-19-c1-02", "node_id": "hco-006"},
    {"sentence_id": "hij-19-c1-03", "node_id": "hco-006"},
    {"sentence_id": "hij-19-c1-04", "node_id": "hco-006"},
    {"sentence_id": "hij-19-c1-05", "node_id": "hco-006"},
    # --- Hij_19 発展問題 ---
    {"sentence_id": "hij-19-a1-01", "node_id": "hco-006"},
    # --- Hij_20 例題 ---
    {"sentence_id": "hij-20-e1-01", "node_id": "hco-007"},
    {"sentence_id": "hij-20-e1-02", "node_id": "hco-007"},
    {"sentence_id": "hij-20-e1-03", "node_id": "hco-007"},
    {"sentence_id": "hij-20-e1-04", "node_id": "hco-007"},
    {"sentence_id": "hij-20-e1-05", "node_id": "hco-007"},
    # --- Hij_20 確認問題 ---
    {"sentence_id": "hij-20-c1-01", "node_id": "hco-007"},
    {"sentence_id": "hij-20-c1-02", "node_id": "hco-007"},
    {"sentence_id": "hij-20-c1-03", "node_id": "hco-007"},
    # --- Hij_20 発展問題 ---
    {"sentence_id": "hij-20-a1-01", "node_id": "hco-007"},
    # --- Hij_21_1 例題 ---
    {"sentence_id": "hij-21-e1-01", "node_id": "hco-008"},
    {"sentence_id": "hij-21-e1-02", "node_id": "hco-008"},
    {"sentence_id": "hij-21-e1-03", "node_id": "hco-008"},
    {"sentence_id": "hij-21-e1-04", "node_id": "hco-008"},
    {"sentence_id": "hij-21-e1-05", "node_id": "hco-008"},
    {"sentence_id": "hij-21-e1-06", "node_id": "hco-008"},
    # --- Hij_21_1 確認問題 ---
    {"sentence_id": "hij-21-c1-01", "node_id": "hco-008"},
    {"sentence_id": "hij-21-c1-02", "node_id": "hco-008"},
    {"sentence_id": "hij-21-c1-03", "node_id": "hco-008"},
    {"sentence_id": "hij-21-c1-04", "node_id": "hco-008"},
    {"sentence_id": "hij-21-c1-05", "node_id": "hco-008"},
    # --- Hij_21_1 発展問題 ---
    {"sentence_id": "hij-21-a1-01", "node_id": "hco-008"},
    # --- Hij_21_2 例題 ---
    {"sentence_id": "hij-21-e4-01", "node_id": "hco-009"},
    {"sentence_id": "hij-21-e4-02", "node_id": "hco-009"},
    {"sentence_id": "hij-21-e4-03", "node_id": "hco-009"},
    {"sentence_id": "hij-21-e4-04", "node_id": "hco-009"},
    {"sentence_id": "hij-21-e4-05", "node_id": "hco-009"},
    # --- Hij_21_2 確認問題 ---
    {"sentence_id": "hij-21-c2-01", "node_id": "hco-009"},
    {"sentence_id": "hij-21-c2-02", "node_id": "hco-009"},
    {"sentence_id": "hij-21-c2-03", "node_id": "hco-009"},
    {"sentence_id": "hij-21-c2-04", "node_id": "hco-009"},
    # --- Hij_21_2 発展問題 ---
    {"sentence_id": "hij-21-a2-01", "node_id": "hco-009"},
    # --- Hij_22 例題 ---
    {"sentence_id": "hij-22-e1-01", "node_id": "hco-010"},
    {"sentence_id": "hij-22-e1-02", "node_id": "hco-010"},
    {"sentence_id": "hij-22-e1-03", "node_id": "hco-010"},
    {"sentence_id": "hij-22-e1-04", "node_id": "hco-010"},
    {"sentence_id": "hij-22-e1-05", "node_id": "hco-010"},
    # --- Hij_22 確認問題 ---
    {"sentence_id": "hij-22-c1-01", "node_id": "hco-010"},
    {"sentence_id": "hij-22-c1-02", "node_id": "hco-010"},
    {"sentence_id": "hij-22-c1-03", "node_id": "hco-010"},
    {"sentence_id": "hij-22-c1-04", "node_id": "hco-010"},
    # --- Hij_22 発展問題 ---
    {"sentence_id": "hij-22-a1-01", "node_id": "hco-010"},
]
