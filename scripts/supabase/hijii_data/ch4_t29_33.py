"""第4章: 動詞の型編 Theme 29-33（SVA for/as/to/into B / 受動態）"""

# ============================================================
# 1. KNOWLEDGE_NODES
# ============================================================

KNOWLEDGE_NODES = [
    {
        "id": "hvp-007",
        "name": "SVA for B型",
        "category": "動詞の型",
        "priority": "P1",
        "notes": "S V A for B の型をとる動詞を2系統に分類。(1)「理由」系: thank A for B / apologize to A for B / blame A for B / praise A for B。(2)「交換」系: exchange A for B / take A for B / substitute A for B。forが「理由」か「交換」かを意識して読解する。",
    },
    {
        "id": "hvp-008",
        "name": "SVA as B型",
        "category": "動詞の型",
        "priority": "P1",
        "notes": "S V A as B の型をとる動詞を2系統に分類。(1)[A=B]系: regard A as B / think of A as B / look on A as B「AをBとみなす」。(2)[S=B]系: S strike A as B「SはAにBという印象を与える」/ S replace A as B「SはBとしてAに取って代わる」。asはイコールの関係。",
    },
    {
        "id": "hvp-009",
        "name": "SVA to B型",
        "category": "動詞の型",
        "priority": "P1",
        "notes": "S V A to B の型をとる動詞を3系統に分類。(1)「方向」系: apply / attach / expose。(2)「oneself」系: adapt / adjust / devote（Aにoneselfが入り「～に順応する/専念する」）。(3)「因果」系: attribute / owe（Aが結果、Bが原因）。toの方向・到達をイメージする。",
    },
    {
        "id": "hvp-010",
        "name": "SVA into B型",
        "category": "動詞の型",
        "priority": "P1",
        "notes": "S V A into B の型をとる動詞を2系統に分類。(1)「Bに-ing」系: talk A into -ing / persuade A into -ing「Aを説得して～させる」（否定はout of）。(2)「Bに名詞」系: change / turn / put / translate。intoは「変化」を表し、AがBに変わるイメージ。",
    },
    {
        "id": "hvp-011",
        "name": "受動態（by以外の前置詞を使う受動態）",
        "category": "動詞の型",
        "priority": "P1",
        "notes": "日本語に訳しにくい受動態の読み方。(1)能動態で訳す: 受動態のSは能動態のO、by以下が能動態のS。(2)能動態になおして考える: もとの動詞の型（remind A of B, make O C, think of A as B, rob A of B等）を意識して訳す。「れる・られる」で不自然なら能動態で訳す。",
    },
]

# ============================================================
# 2. UNDERSTANDING_GOALS
# ============================================================

UNDERSTANDING_GOALS = [
    # hvp-007: SVA for B型
    {"node_id": "hvp-007", "seq": 1, "goal": "thank / apologize / blame / praiseを見たら、A for Bの「理由」系の型を予測できる"},
    {"node_id": "hvp-007", "seq": 2, "goal": "exchange / take / substituteを見たら、A for Bの「交換」系の型を予測できる"},
    {"node_id": "hvp-007", "seq": 3, "goal": "apologize to A for Bのように、Aの前にtoが必要な動詞を認識できる"},
    {"node_id": "hvp-007", "seq": 4, "goal": "forが「理由」か「交換」かを文脈から判断し、正確に和訳できる"},
    # hvp-008: SVA as B型
    {"node_id": "hvp-008", "seq": 1, "goal": "regard / think of / look onを見たら、A as Bの[A=B]系の型を予測できる"},
    {"node_id": "hvp-008", "seq": 2, "goal": "strikeを見たら、S strike A as Bの[S=B]系の型を予測できる"},
    {"node_id": "hvp-008", "seq": 3, "goal": "replaceを見たら、S replace A as B「SはBとしてAに取って代わる」の型を予測できる"},
    {"node_id": "hvp-008", "seq": 4, "goal": "asがイコールの関係を結ぶことを理解し、A=BかS=Bかを見分けられる"},
    # hvp-009: SVA to B型
    {"node_id": "hvp-009", "seq": 1, "goal": "apply / attach / exposeを見たら、A to Bの「方向」系の型を予測できる"},
    {"node_id": "hvp-009", "seq": 2, "goal": "adapt / adjust / devoteがoneself to Bの形をとり「順応する/専念する」となるパターンを認識できる"},
    {"node_id": "hvp-009", "seq": 3, "goal": "attribute / oweを見たら、A to Bの「因果」系の型を予測し、Aが結果・Bが原因と認識できる"},
    {"node_id": "hvp-009", "seq": 4, "goal": "toの方向・到達のイメージで各表現を統一的に理解できる"},
    # hvp-010: SVA into B型
    {"node_id": "hvp-010", "seq": 1, "goal": "talk / persuadeを見たら、A into -ing「Aを説得して～させる」の型を予測できる"},
    {"node_id": "hvp-010", "seq": 2, "goal": "intoをout ofに変えると「Aを説得して～させない」になることを理解している"},
    {"node_id": "hvp-010", "seq": 3, "goal": "change / turn / put / translateを見たら、A into Bの「変化」系の型を予測できる"},
    {"node_id": "hvp-010", "seq": 4, "goal": "intoが「変化」を表すことを理解し、AがBに変わるイメージで読解できる"},
    # hvp-011: 受動態
    {"node_id": "hvp-011", "seq": 1, "goal": "受動態を「れる・られる」で訳して不自然なとき、能動態で訳すことができる"},
    {"node_id": "hvp-011", "seq": 2, "goal": "受動態のSは能動態のO、by以下が能動態のSであることを理解している"},
    {"node_id": "hvp-011", "seq": 3, "goal": "もとの動詞の型（remind A of B, think of A as B, rob A of B等）を意識して受動態を読解できる"},
    {"node_id": "hvp-011", "seq": 4, "goal": "make O Cが受動態になるとO be made to doとtoが入ることを理解している"},
]

# ============================================================
# 3. CHECK_POINTS
# ============================================================

CHECK_POINTS = [
    # hvp-007: SVA for B型
    {"node_id": "hvp-007", "seq": 1, "question": "SVA for B型の「理由」系の動詞を4つ挙げよ。", "answer": "thank / apologize / blame / praise。forは「理由」を表す。"},
    {"node_id": "hvp-007", "seq": 2, "question": "SVA for B型の「交換」系の動詞を3つ挙げよ。", "answer": "exchange / take / substitute。forは「交換」で前後を入れ替えるイメージ。"},
    {"node_id": "hvp-007", "seq": 3, "question": "apologizeがSVA for B型をとるとき、thankと異なる点は何か？", "answer": "Aの前にtoが必要。apologize to A for B「AにBで謝罪する」の形になる。"},
    {"node_id": "hvp-007", "seq": 4, "question": "substitute A for Bの意味は？", "answer": "AをBの代わりに使う。交換のforで前後を入れ替えるイメージ。"},
    # hvp-008: SVA as B型
    {"node_id": "hvp-008", "seq": 1, "question": "SVA as B型で[A=B]系の動詞を3つ挙げよ。", "answer": "regard / think of / look on [upon]。いずれも「AをBとみなす」の意味。"},
    {"node_id": "hvp-008", "seq": 2, "question": "S strike A as Bの意味は？A=BとS=Bのどちらか？", "answer": "「SはAにBという印象を与える」。S=Bの関係が成り立つ。"},
    {"node_id": "hvp-008", "seq": 3, "question": "S replace A as Bの意味は？", "answer": "SはBとしてAに取って代わる。S=Bの関係が成り立つ。"},
    {"node_id": "hvp-008", "seq": 4, "question": "asは前後をどのような関係で結ぶか？", "answer": "イコールの関係。A=BまたはS=Bの関係を表す。"},
    # hvp-009: SVA to B型
    {"node_id": "hvp-009", "seq": 1, "question": "SVA to B型の「方向」系の動詞を3つ挙げよ。", "answer": "apply / attach / expose。toが方向を表し「AをBに応用する/取りつける/さらす」。"},
    {"node_id": "hvp-009", "seq": 2, "question": "SVA to B型の「oneself」系の動詞を3つ挙げよ。", "answer": "adapt / adjust / devote。Aにoneselfが入り「～に順応する/順応する/専念する」。"},
    {"node_id": "hvp-009", "seq": 3, "question": "owe A to Bの意味と、AとBの関係は？", "answer": "「AはBのおかげだ」。Aが結果、Bが原因の因果関係。"},
    {"node_id": "hvp-009", "seq": 4, "question": "attribute A to Bの意味は？", "answer": "「AはBのおかげだ」。oweと同じく因果関係を表す。"},
    # hvp-010: SVA into B型
    {"node_id": "hvp-010", "seq": 1, "question": "talk A into -ingの意味は？否定の場合はどうなるか？", "answer": "「Aを説得して～させる」。否定はintoをout ofにして「Aを説得して～させない」。"},
    {"node_id": "hvp-010", "seq": 2, "question": "SVA into B型の「Bに名詞」系の動詞を4つ挙げよ。", "answer": "change / turn / put / translate。intoは「変化」を表す。"},
    {"node_id": "hvp-010", "seq": 3, "question": "put A into practiceの意味は？", "answer": "Aを実行に移す。Aが変化して実行される状態になる。"},
    {"node_id": "hvp-010", "seq": 4, "question": "translate A into Bの意味は？", "answer": "AをBに翻訳する。Aという言語がBという言語に変化するイメージ。"},
    # hvp-011: 受動態
    {"node_id": "hvp-011", "seq": 1, "question": "受動態を日本語の「れる・られる」で訳して不自然なとき、どうすべきか？", "answer": "能動態で訳す。受動態のSは能動態のO、by以下が能動態のSにあたる。"},
    {"node_id": "hvp-011", "seq": 2, "question": "was reminded ofのもとの型は何か？", "answer": "remind A of B「AにBを思い出させる」。受動態で「～を思い出した」と能動態で訳す。"},
    {"node_id": "hvp-011", "seq": 3, "question": "make O Cが受動態になるとき、Cに動詞の原形がくる場合の注意点は？", "answer": "O be made to doとtoが入る。能動態ではmake O V原形だが、受動態ではtoが必要。"},
    {"node_id": "hvp-011", "seq": 4, "question": "was robbed ofのもとの型は何か？", "answer": "rob A of B「AからBを奪う」。受動態で「Bを奪われた」と訳す。"},
]

# ============================================================
# 4. NODE_PREREQUISITES
# ============================================================

NODE_PREREQUISITES = [
    {"node_id": "hvp-007", "prerequisite_id": "hvp-006"},
    {"node_id": "hvp-008", "prerequisite_id": "hvp-007"},
    {"node_id": "hvp-009", "prerequisite_id": "hvp-008"},
    {"node_id": "hvp-010", "prerequisite_id": "hvp-009"},
    {"node_id": "hvp-011", "prerequisite_id": "hvp-010"},
]

# ============================================================
# 5. KNOWLEDGE_REFERENCES
# ============================================================

KNOWLEDGE_REFERENCES = [
    {"node_id": "hvp-007", "book": "肘井の読解のための英文法", "section_id": "Hij_29", "pages": "p.190-193"},
    {"node_id": "hvp-008", "book": "肘井の読解のための英文法", "section_id": "Hij_30", "pages": "p.194-197"},
    {"node_id": "hvp-009", "book": "肘井の読解のための英文法", "section_id": "Hij_31", "pages": "p.198-201"},
    {"node_id": "hvp-010", "book": "肘井の読解のための英文法", "section_id": "Hij_32", "pages": "p.202-205"},
    {"node_id": "hvp-011", "book": "肘井の読解のための英文法", "section_id": "Hij_33", "pages": "p.206-209"},
]

# ============================================================
# 6. SECTIONS
# ============================================================

SECTIONS = [
    {
        "id": "Hij_29",
        "book": "肘井の読解のための英文法",
        "title": "Theme 29 SVA for B型で英文が読める",
        "pages": "p.190-193",
        "type": "drill",
    },
    {
        "id": "Hij_30",
        "book": "肘井の読解のための英文法",
        "title": "Theme 30 SVA as B型で英文が読める",
        "pages": "p.194-197",
        "type": "drill",
    },
    {
        "id": "Hij_31",
        "book": "肘井の読解のための英文法",
        "title": "Theme 31 SVA to B型で英文が読める",
        "pages": "p.198-201",
        "type": "drill",
    },
    {
        "id": "Hij_32",
        "book": "肘井の読解のための英文法",
        "title": "Theme 32 SVA into B型で英文が読める",
        "pages": "p.202-205",
        "type": "drill",
    },
    {
        "id": "Hij_33",
        "book": "肘井の読解のための英文法",
        "title": "Theme 33 受動態で英文が読める",
        "pages": "p.206-209",
        "type": "drill",
    },
]

# ============================================================
# 7. SECTION_PREREQUISITES
# ============================================================

SECTION_PREREQUISITES = [
    {"section_id": "Hij_29", "prerequisite_id": "Hij_28"},
    {"section_id": "Hij_30", "prerequisite_id": "Hij_29"},
    {"section_id": "Hij_31", "prerequisite_id": "Hij_30"},
    {"section_id": "Hij_32", "prerequisite_id": "Hij_31"},
    {"section_id": "Hij_33", "prerequisite_id": "Hij_32"},
]

# ============================================================
# 8. SECTION_KNOWLEDGE_NODES
# ============================================================

SECTION_KNOWLEDGE_NODES = [
    {"section_id": "Hij_29", "node_id": "hvp-007", "seq": 1},
    {"section_id": "Hij_30", "node_id": "hvp-008", "seq": 1},
    {"section_id": "Hij_31", "node_id": "hvp-009", "seq": 1},
    {"section_id": "Hij_32", "node_id": "hvp-010", "seq": 1},
    {"section_id": "Hij_33", "node_id": "hvp-011", "seq": 1},
]

# ============================================================
# 9. SENTENCES
# ============================================================

SENTENCES = [
    # ==========================================================
    # Hij_29 -- Theme 29 SVA for B型で英文が読める
    # ==========================================================
    # ----------------------------------------------------------
    # Hij_29 -- 例題 (5問)
    # ----------------------------------------------------------
    {
        "id": "hij-29-e1-01",
        "section_id": "Hij_29",
        "drill": 1,
        "number": 1,
        "role": "example",
        "english": "He thanked me for helping him across the road.",
        "japanese": "彼は私に、道を横断するのを手伝ったことで感謝した。",
        "notes": None,
    },
    {
        "id": "hij-29-e1-02",
        "section_id": "Hij_29",
        "drill": 1,
        "number": 2,
        "role": "example",
        "english": "We apologized to the customers for making a mistake.",
        "japanese": "私たちは、顧客に間違いをしたことで謝罪した。",
        "notes": None,
    },
    {
        "id": "hij-29-e1-03",
        "section_id": "Hij_29",
        "drill": 1,
        "number": 3,
        "role": "example",
        "english": "He blamed everyone else for his lack of success.",
        "japanese": "彼は自分が成功していないのを、ほかのみんなのせいにした。",
        "notes": None,
    },
    {
        "id": "hij-29-e1-04",
        "section_id": "Hij_29",
        "drill": 1,
        "number": 4,
        "role": "example",
        "english": "I would like to exchange yen for dollars.",
        "japanese": "私は円をドルと交換したい。",
        "notes": None,
    },
    {
        "id": "hij-29-e1-05",
        "section_id": "Hij_29",
        "drill": 1,
        "number": 5,
        "role": "example",
        "english": "When I glanced at him, I took him for a Chinese.",
        "japanese": "私が彼をちらっと見たとき、私は彼を中国人だと思い込んだ。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_29 -- 確認問題 (3問)
    # ----------------------------------------------------------
    {
        "id": "hij-29-c1-01",
        "section_id": "Hij_29",
        "drill": 2,
        "number": 1,
        "role": "practice",
        "english": "I didn't blame her for getting angry.",
        "japanese": "私は彼女を、怒ったことで責めなかった。",
        "notes": None,
    },
    {
        "id": "hij-29-c1-02",
        "section_id": "Hij_29",
        "drill": 2,
        "number": 2,
        "role": "practice",
        "english": "You should apologize to him for your rude behavior.",
        "japanese": "あなたは彼に、自分のとった無礼な態度のことで謝るべきだ。",
        "notes": None,
    },
    {
        "id": "hij-29-c1-03",
        "section_id": "Hij_29",
        "drill": 2,
        "number": 3,
        "role": "practice",
        "english": "You should not substitute snacks for regular meals.",
        "japanese": "あなたはスナックを、いつもの食事の代わりにするべきではない。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_29 -- 発展問題 (1問)
    # ----------------------------------------------------------
    {
        "id": "hij-29-a1-01",
        "section_id": "Hij_29",
        "drill": 3,
        "number": 1,
        "role": "advanced",
        "english": "It's important to praise children for the little steps they take toward their goals.",
        "japanese": "子どもたちを、目標に向かって少しずつ歩んでいることでほめてあげるのは、重要だ。",
        "notes": "中央大",
    },
    # ==========================================================
    # Hij_30 -- Theme 30 SVA as B型で英文が読める
    # ==========================================================
    # ----------------------------------------------------------
    # Hij_30 -- 例題 (4問) + ポイント49 例文 (1問)
    # ----------------------------------------------------------
    {
        "id": "hij-30-e1-01",
        "section_id": "Hij_30",
        "drill": 1,
        "number": 1,
        "role": "example",
        "english": "Americans do not regard Coca-Cola only as a drink.",
        "japanese": "アメリカ人は、コカ・コーラを単なる飲み物とはみなしていない。",
        "notes": None,
    },
    {
        "id": "hij-30-e1-02",
        "section_id": "Hij_30",
        "drill": 1,
        "number": 2,
        "role": "example",
        "english": "Kyoko thinks of Yumi as her best friend.",
        "japanese": "キョウコは、ユミを親友とみなしている。",
        "notes": None,
    },
    {
        "id": "hij-30-e1-03",
        "section_id": "Hij_30",
        "drill": 1,
        "number": 3,
        "role": "example",
        "english": "He looked on the situation as a good opportunity.",
        "japanese": "彼は、その状況をよい機会とみなした。",
        "notes": None,
    },
    {
        "id": "hij-30-e1-04",
        "section_id": "Hij_30",
        "drill": 1,
        "number": 4,
        "role": "example",
        "english": "The jokes didn't strike me as being very funny.",
        "japanese": "その冗談は、私にはあまりおもしろい印象を与えなかった。",
        "notes": None,
    },
    # ポイント49 例文
    {
        "id": "hij-30-e1-05",
        "section_id": "Hij_30",
        "drill": 1,
        "number": 5,
        "role": "example",
        "english": "The young woman will replace the old man as president.",
        "japanese": "その若い女性が、社長としてその高齢の男性に取って代わるだろう。",
        "notes": "ポイント49 例文",
    },
    # ----------------------------------------------------------
    # Hij_30 -- 確認問題 (3問)
    # ----------------------------------------------------------
    {
        "id": "hij-30-c1-01",
        "section_id": "Hij_30",
        "drill": 2,
        "number": 1,
        "role": "practice",
        "english": "I don't want people to think of me as being too serious.",
        "japanese": "私は人びとに、自分をまじめすぎると思われたくない。",
        "notes": None,
    },
    {
        "id": "hij-30-c1-02",
        "section_id": "Hij_30",
        "drill": 2,
        "number": 2,
        "role": "practice",
        "english": "The ancient Greek philosophers regarded debate as superior to experiment.",
        "japanese": "古代ギリシャの哲学者は、議論を実験よりすぐれているとみなしていた。",
        "notes": None,
    },
    {
        "id": "hij-30-c1-03",
        "section_id": "Hij_30",
        "drill": 2,
        "number": 3,
        "role": "practice",
        "english": "Her mother strikes me as very kind.",
        "japanese": "彼女のお母さんは私に、とても優しい印象を与える。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_30 -- 発展問題 (1問)
    # ----------------------------------------------------------
    {
        "id": "hij-30-a1-01",
        "section_id": "Hij_30",
        "drill": 3,
        "number": 1,
        "role": "advanced",
        "english": "Many students think of learning as something that just happens when they read a text over and over again.",
        "japanese": "多くの生徒が、学習とは、ひたすら教科書を読めばただ起こるものだと考えている。",
        "notes": "宮城教育大",
    },
    # ==========================================================
    # Hij_31 -- Theme 31 SVA to B型で英文が読める
    # ==========================================================
    # ----------------------------------------------------------
    # Hij_31 -- 例題 (5問)
    # ----------------------------------------------------------
    {
        "id": "hij-31-e1-01",
        "section_id": "Hij_31",
        "drill": 1,
        "number": 1,
        "role": "example",
        "english": "It is necessary to apply Information Technology to education.",
        "japanese": "ITを教育に応用することは必要だ。",
        "notes": None,
    },
    {
        "id": "hij-31-e1-02",
        "section_id": "Hij_31",
        "drill": 1,
        "number": 2,
        "role": "example",
        "english": "She attached a label to the package.",
        "japanese": "彼女は荷札をその荷物に取りつけた。",
        "notes": None,
    },
    {
        "id": "hij-31-e1-03",
        "section_id": "Hij_31",
        "drill": 1,
        "number": 3,
        "role": "example",
        "english": "I have to adjust myself to my new way of life.",
        "japanese": "私は、新しい生活様式に順応しなければならない。",
        "notes": None,
    },
    {
        "id": "hij-31-e1-04",
        "section_id": "Hij_31",
        "drill": 1,
        "number": 4,
        "role": "example",
        "english": "He devoted himself to a peace movement.",
        "japanese": "彼は平和活動に専念した。",
        "notes": None,
    },
    {
        "id": "hij-31-e1-05",
        "section_id": "Hij_31",
        "drill": 1,
        "number": 5,
        "role": "example",
        "english": "I owe what I am to my grandmother.",
        "japanese": "いまの私があるのは、祖母のおかげだ。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_31 -- 確認問題 (3問)
    # ----------------------------------------------------------
    {
        "id": "hij-31-c1-01",
        "section_id": "Hij_31",
        "drill": 2,
        "number": 1,
        "role": "practice",
        "english": "His kindness exposed him to many dangers.",
        "japanese": "親切心のせいで、彼は多くの危険な目にあった。",
        "notes": None,
    },
    {
        "id": "hij-31-c1-02",
        "section_id": "Hij_31",
        "drill": 2,
        "number": 2,
        "role": "practice",
        "english": "He adapted his way to the new circumstances.",
        "japanese": "彼は、自分のやり方を新しい状況に合わせた。",
        "notes": None,
    },
    {
        "id": "hij-31-c1-03",
        "section_id": "Hij_31",
        "drill": 2,
        "number": 3,
        "role": "practice",
        "english": "I attribute my success to my father.",
        "japanese": "私の成功は父のおかげだ。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_31 -- 発展問題 (1問)
    # ----------------------------------------------------------
    {
        "id": "hij-31-a1-01",
        "section_id": "Hij_31",
        "drill": 3,
        "number": 1,
        "role": "advanced",
        "english": "Babies attach the word 'mama' to their own mother and not to just any woman.",
        "japanese": "赤ちゃんは「ママ」という言葉を自分の母親につけているのであって、女性ならだれにでもつけているというわけではない。",
        "notes": "滋賀大",
    },
    # ==========================================================
    # Hij_32 -- Theme 32 SVA into B型で英文が読める
    # ==========================================================
    # ----------------------------------------------------------
    # Hij_32 -- 例題 (5問)
    # ----------------------------------------------------------
    {
        "id": "hij-32-e1-01",
        "section_id": "Hij_32",
        "drill": 1,
        "number": 1,
        "role": "example",
        "english": "I talked my father into buying me a camera.",
        "japanese": "私は父を説得して、カメラを買ってもらった。",
        "notes": None,
    },
    {
        "id": "hij-32-e1-02",
        "section_id": "Hij_32",
        "drill": 1,
        "number": 2,
        "role": "example",
        "english": "I managed to persuade my mother into accepting my plan.",
        "japanese": "私は母を何とか説得して、私の計画を受け入れさせた。",
        "notes": None,
    },
    {
        "id": "hij-32-e1-03",
        "section_id": "Hij_32",
        "drill": 1,
        "number": 3,
        "role": "example",
        "english": "The trees turn carbon dioxide into clean air.",
        "japanese": "木は二酸化炭素をきれいな空気に変化させる。",
        "notes": None,
    },
    {
        "id": "hij-32-e1-04",
        "section_id": "Hij_32",
        "drill": 1,
        "number": 4,
        "role": "example",
        "english": "I put her ideas into practice.",
        "japanese": "私は彼女の考えを実行に移した。",
        "notes": None,
    },
    {
        "id": "hij-32-e1-05",
        "section_id": "Hij_32",
        "drill": 1,
        "number": 5,
        "role": "example",
        "english": "She translates English sentences into Japanese.",
        "japanese": "彼女は英文を日本語に翻訳する。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_32 -- 確認問題 (3問)
    # ----------------------------------------------------------
    {
        "id": "hij-32-c1-01",
        "section_id": "Hij_32",
        "drill": 2,
        "number": 1,
        "role": "practice",
        "english": "I talked her out of running away from home.",
        "japanese": "私は彼女を説得して家出させなかった。",
        "notes": None,
    },
    {
        "id": "hij-32-c1-02",
        "section_id": "Hij_32",
        "drill": 2,
        "number": 2,
        "role": "practice",
        "english": "It is important to change negative thinking into positive action.",
        "japanese": "否定的な考えを、前向きな行動に変えるのは重要だ。",
        "notes": None,
    },
    {
        "id": "hij-32-c1-03",
        "section_id": "Hij_32",
        "drill": 2,
        "number": 3,
        "role": "practice",
        "english": "His job is to translate documents into English.",
        "japanese": "彼の仕事は、文書を英語に翻訳することだ。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_32 -- 発展問題 (1問)
    # ----------------------------------------------------------
    {
        "id": "hij-32-a1-01",
        "section_id": "Hij_32",
        "drill": 3,
        "number": 1,
        "role": "advanced",
        "english": "Her novels are well known all over the world and have been translated into a number of languages, including French and Chinese.",
        "japanese": "彼女の小説は世界中でよく知られていて、フランス語や中国語を含むたくさんの言語に翻訳されてきた。",
        "notes": "福島大",
    },
    # ==========================================================
    # Hij_33 -- Theme 33 受動態で英文が読める
    # ==========================================================
    # ----------------------------------------------------------
    # Hij_33 -- 例題 (5問)
    # ----------------------------------------------------------
    {
        "id": "hij-33-e1-01",
        "section_id": "Hij_33",
        "drill": 1,
        "number": 1,
        "role": "example",
        "english": "The special book can be bought by anyone.",
        "japanese": "だれでも、その特別な本を買うことができる。",
        "notes": None,
    },
    {
        "id": "hij-33-e1-02",
        "section_id": "Hij_33",
        "drill": 1,
        "number": 2,
        "role": "example",
        "english": "I was reminded of our plans to go shopping.",
        "japanese": "私は、買い物に行くという私たちの計画を思い出した。",
        "notes": None,
    },
    {
        "id": "hij-33-e1-03",
        "section_id": "Hij_33",
        "drill": 1,
        "number": 3,
        "role": "example",
        "english": "I was made to go against my will.",
        "japanese": "私は自分の意思に反して、むりやり行くはめになった。",
        "notes": None,
    },
    {
        "id": "hij-33-e1-04",
        "section_id": "Hij_33",
        "drill": 1,
        "number": 4,
        "role": "example",
        "english": "In Britain, February is thought of as one of the worst months.",
        "japanese": "イギリスでは、2月は最悪の月のひとつとみなされる。",
        "notes": None,
    },
    {
        "id": "hij-33-e1-05",
        "section_id": "Hij_33",
        "drill": 1,
        "number": 5,
        "role": "example",
        "english": "She was robbed of her ring last night.",
        "japanese": "彼女は昨晩、指輪を奪われた。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_33 -- 確認問題 (3問)
    # ----------------------------------------------------------
    {
        "id": "hij-33-c1-01",
        "section_id": "Hij_33",
        "drill": 2,
        "number": 1,
        "role": "practice",
        "english": "He is compelled to do what he does not enjoy doing.",
        "japanese": "彼は、やっていて楽しくないことをせざるをえない。",
        "notes": None,
    },
    {
        "id": "hij-33-c1-02",
        "section_id": "Hij_33",
        "drill": 2,
        "number": 2,
        "role": "practice",
        "english": "He is regarded as one of the most famous writers.",
        "japanese": "彼は、最も有名な作家の一人とみなされている。",
        "notes": None,
    },
    {
        "id": "hij-33-c1-03",
        "section_id": "Hij_33",
        "drill": 2,
        "number": 3,
        "role": "practice",
        "english": "He was seen reading a book in the library.",
        "japanese": "彼は図書館で本を読んでいるところを見られた。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_33 -- 発展問題 (1問)
    # ----------------------------------------------------------
    {
        "id": "hij-33-a1-01",
        "section_id": "Hij_33",
        "drill": 3,
        "number": 1,
        "role": "advanced",
        "english": "Those people who do not require help will not be made to feel unfairly treated by high levels of taxation.",
        "japanese": "助けを必要としないそれらの人びとは、高い税金をかけられているからといって、自分たちが不当に扱われていると感じることはないだろう。",
        "notes": "東京大",
    },
]

# ============================================================
# 10. SENTENCE_STRUCTURES
# ============================================================

SENTENCE_STRUCTURES = [
    # --- Hij_29 例題 ---
    # --- hij-29-e1-01 ---
    {"sentence_id": "hij-29-e1-01", "label": "overall", "value": "S V A for B"},
    {"sentence_id": "hij-29-e1-01", "label": "details", "value": "He(S) thanked(V) me(A) [for helping him across the road](for B)"},
    # --- hij-29-e1-02 ---
    {"sentence_id": "hij-29-e1-02", "label": "overall", "value": "S V to A for B"},
    {"sentence_id": "hij-29-e1-02", "label": "details", "value": "We(S) apologized(V) [to the customers](to A) [for making a mistake](for B)"},
    # --- hij-29-e1-03 ---
    {"sentence_id": "hij-29-e1-03", "label": "overall", "value": "S V A for B"},
    {"sentence_id": "hij-29-e1-03", "label": "details", "value": "He(S) blamed(V) everyone else(A) [for his lack of success](for B)"},
    # --- hij-29-e1-04 ---
    {"sentence_id": "hij-29-e1-04", "label": "overall", "value": "S V A for B"},
    {"sentence_id": "hij-29-e1-04", "label": "details", "value": "I(S) would like to exchange(V) yen(A) [for dollars](for B)"},
    # --- hij-29-e1-05 ---
    {"sentence_id": "hij-29-e1-05", "label": "overall", "value": "M S V A for B"},
    {"sentence_id": "hij-29-e1-05", "label": "details", "value": "[When I glanced at him](M) I(S) took(V) him(A) [for a Chinese](for B)"},
    # --- Hij_29 確認問題 ---
    # --- hij-29-c1-01 ---
    {"sentence_id": "hij-29-c1-01", "label": "overall", "value": "S V A for B"},
    {"sentence_id": "hij-29-c1-01", "label": "details", "value": "I(S) didn't blame(V) her(A) [for getting angry](for B)"},
    # --- hij-29-c1-02 ---
    {"sentence_id": "hij-29-c1-02", "label": "overall", "value": "S V to A for B"},
    {"sentence_id": "hij-29-c1-02", "label": "details", "value": "You(S) should apologize(V) [to him](to A) [for your rude behavior](for B)"},
    # --- hij-29-c1-03 ---
    {"sentence_id": "hij-29-c1-03", "label": "overall", "value": "S V A for B"},
    {"sentence_id": "hij-29-c1-03", "label": "details", "value": "You(S) should not substitute(V) snacks(A) [for regular meals](for B)"},
    # --- Hij_29 発展問題 ---
    # --- hij-29-a1-01 ---
    {"sentence_id": "hij-29-a1-01", "label": "overall", "value": "S V C V' A for B"},
    {"sentence_id": "hij-29-a1-01", "label": "details", "value": "It(S) is(V) important(C) <to praise(V') children(A) [for the little steps (they take toward their goals)](for B)>"},
    # --- Hij_30 例題 ---
    # --- hij-30-e1-01 ---
    {"sentence_id": "hij-30-e1-01", "label": "overall", "value": "S V A M as B"},
    {"sentence_id": "hij-30-e1-01", "label": "details", "value": "Americans(S) do not regard(V) Coca-Cola(A) only(M) [as a drink](as B)"},
    # --- hij-30-e1-02 ---
    {"sentence_id": "hij-30-e1-02", "label": "overall", "value": "S V A as B"},
    {"sentence_id": "hij-30-e1-02", "label": "details", "value": "Kyoko(S) thinks of(V) Yumi(A) [as her best friend](as B)"},
    # --- hij-30-e1-03 ---
    {"sentence_id": "hij-30-e1-03", "label": "overall", "value": "S V A as B"},
    {"sentence_id": "hij-30-e1-03", "label": "details", "value": "He(S) looked on(V) the situation(A) [as a good opportunity](as B)"},
    # --- hij-30-e1-04 ---
    {"sentence_id": "hij-30-e1-04", "label": "overall", "value": "S V A as B"},
    {"sentence_id": "hij-30-e1-04", "label": "details", "value": "The jokes(S) didn't strike(V) me(A) [as being very funny](as B)"},
    # --- hij-30-e1-05 (ポイント49) ---
    {"sentence_id": "hij-30-e1-05", "label": "overall", "value": "S V A as B"},
    {"sentence_id": "hij-30-e1-05", "label": "details", "value": "The young woman(S) will replace(V) the old man(A) [as president](as B)"},
    # --- Hij_30 確認問題 ---
    # --- hij-30-c1-01 ---
    {"sentence_id": "hij-30-c1-01", "label": "overall", "value": "S V O V' A as B"},
    {"sentence_id": "hij-30-c1-01", "label": "details", "value": "I(S) don't want(V) people(O) <to think of(V') me(A) [as being too serious](as B)>"},
    # --- hij-30-c1-02 ---
    {"sentence_id": "hij-30-c1-02", "label": "overall", "value": "S V A as B"},
    {"sentence_id": "hij-30-c1-02", "label": "details", "value": "The ancient Greek philosophers(S) regarded(V) debate(A) [as superior to experiment](as B)"},
    # --- hij-30-c1-03 ---
    {"sentence_id": "hij-30-c1-03", "label": "overall", "value": "S V A as B"},
    {"sentence_id": "hij-30-c1-03", "label": "details", "value": "Her mother(S) strikes(V) me(A) [as very kind](as B)"},
    # --- Hij_30 発展問題 ---
    # --- hij-30-a1-01 ---
    {"sentence_id": "hij-30-a1-01", "label": "overall", "value": "S V A as B (M)"},
    {"sentence_id": "hij-30-a1-01", "label": "details", "value": "Many students(S) think of(V) learning(A) [as something (that just happens when they read a text over and over again)](as B)"},
    # --- Hij_31 例題 ---
    # --- hij-31-e1-01 ---
    {"sentence_id": "hij-31-e1-01", "label": "overall", "value": "S V C V' A to B"},
    {"sentence_id": "hij-31-e1-01", "label": "details", "value": "It(S) is(V) necessary(C) <to apply(V') Information Technology(A) [to education](to B)>"},
    # --- hij-31-e1-02 ---
    {"sentence_id": "hij-31-e1-02", "label": "overall", "value": "S V A to B"},
    {"sentence_id": "hij-31-e1-02", "label": "details", "value": "She(S) attached(V) a label(A) [to the package](to B)"},
    # --- hij-31-e1-03 ---
    {"sentence_id": "hij-31-e1-03", "label": "overall", "value": "S V oneself to B"},
    {"sentence_id": "hij-31-e1-03", "label": "details", "value": "I(S) have to adjust(V) myself(A:oneself) [to my new way of life](to B)"},
    # --- hij-31-e1-04 ---
    {"sentence_id": "hij-31-e1-04", "label": "overall", "value": "S V oneself to B"},
    {"sentence_id": "hij-31-e1-04", "label": "details", "value": "He(S) devoted(V) himself(A:oneself) [to a peace movement](to B)"},
    # --- hij-31-e1-05 ---
    {"sentence_id": "hij-31-e1-05", "label": "overall", "value": "S V A to B"},
    {"sentence_id": "hij-31-e1-05", "label": "details", "value": "I(S) owe(V) <what I am>(A) [to my grandmother](to B)"},
    # --- Hij_31 確認問題 ---
    # --- hij-31-c1-01 ---
    {"sentence_id": "hij-31-c1-01", "label": "overall", "value": "S V A to B"},
    {"sentence_id": "hij-31-c1-01", "label": "details", "value": "His kindness(S) exposed(V) him(A) [to many dangers](to B)"},
    # --- hij-31-c1-02 ---
    {"sentence_id": "hij-31-c1-02", "label": "overall", "value": "S V A to B"},
    {"sentence_id": "hij-31-c1-02", "label": "details", "value": "He(S) adapted(V) his way(A) [to the new circumstances](to B)"},
    # --- hij-31-c1-03 ---
    {"sentence_id": "hij-31-c1-03", "label": "overall", "value": "S V A to B"},
    {"sentence_id": "hij-31-c1-03", "label": "details", "value": "I(S) attribute(V) my success(A) [to my father](to B)"},
    # --- Hij_31 発展問題 ---
    # --- hij-31-a1-01 ---
    {"sentence_id": "hij-31-a1-01", "label": "overall", "value": "S V A to B to B"},
    {"sentence_id": "hij-31-a1-01", "label": "details", "value": "Babies(S) attach(V) the word 'mama'(A) [to their own mother](to B) and not [to just any woman](to B)"},
    # --- Hij_32 例題 ---
    # --- hij-32-e1-01 ---
    {"sentence_id": "hij-32-e1-01", "label": "overall", "value": "S V A into -ing"},
    {"sentence_id": "hij-32-e1-01", "label": "details", "value": "I(S) talked(V) my father(A) [into buying me a camera](into -ing)"},
    # --- hij-32-e1-02 ---
    {"sentence_id": "hij-32-e1-02", "label": "overall", "value": "S V A into -ing"},
    {"sentence_id": "hij-32-e1-02", "label": "details", "value": "I(S) managed to persuade(V) my mother(A) [into accepting my plan](into -ing)"},
    # --- hij-32-e1-03 ---
    {"sentence_id": "hij-32-e1-03", "label": "overall", "value": "S V A into B"},
    {"sentence_id": "hij-32-e1-03", "label": "details", "value": "The trees(S) turn(V) carbon dioxide(A) [into clean air](into B)"},
    # --- hij-32-e1-04 ---
    {"sentence_id": "hij-32-e1-04", "label": "overall", "value": "S V A into B"},
    {"sentence_id": "hij-32-e1-04", "label": "details", "value": "I(S) put(V) her ideas(A) [into practice](into B)"},
    # --- hij-32-e1-05 ---
    {"sentence_id": "hij-32-e1-05", "label": "overall", "value": "S V A into B"},
    {"sentence_id": "hij-32-e1-05", "label": "details", "value": "She(S) translates(V) English sentences(A) [into Japanese](into B)"},
    # --- Hij_32 確認問題 ---
    # --- hij-32-c1-01 ---
    {"sentence_id": "hij-32-c1-01", "label": "overall", "value": "S V A out of -ing"},
    {"sentence_id": "hij-32-c1-01", "label": "details", "value": "I(S) talked(V) her(A) [out of running away from home](out of -ing)"},
    # --- hij-32-c1-02 ---
    {"sentence_id": "hij-32-c1-02", "label": "overall", "value": "S V C V' A into B"},
    {"sentence_id": "hij-32-c1-02", "label": "details", "value": "It(S) is(V) important(C) <to change(V') negative thinking(A) [into positive action](into B)>"},
    # --- hij-32-c1-03 ---
    {"sentence_id": "hij-32-c1-03", "label": "overall", "value": "S V C V' A into B"},
    {"sentence_id": "hij-32-c1-03", "label": "details", "value": "His job(S) is(V) <to translate(V') documents(A) [into English](into B)>(C)"},
    # --- Hij_32 発展問題 ---
    # --- hij-32-a1-01 ---
    {"sentence_id": "hij-32-a1-01", "label": "overall", "value": "S V1 C M V2 M M"},
    {"sentence_id": "hij-32-a1-01", "label": "details", "value": "Her novels(S) are(V1) well known(C) [all over the world](M) and have been translated(V2) [into a number of languages](into B) [including French and Chinese](M)"},
    # --- Hij_33 例題 ---
    # --- hij-33-e1-01 ---
    {"sentence_id": "hij-33-e1-01", "label": "overall", "value": "S V M"},
    {"sentence_id": "hij-33-e1-01", "label": "details", "value": "The special book(S) can be bought(V) [by anyone](M)"},
    # --- hij-33-e1-02 ---
    {"sentence_id": "hij-33-e1-02", "label": "overall", "value": "S V O M"},
    {"sentence_id": "hij-33-e1-02", "label": "details", "value": "I(S) was reminded(V) [of our plans (to go shopping)](O)"},
    # --- hij-33-e1-03 ---
    {"sentence_id": "hij-33-e1-03", "label": "overall", "value": "S V M"},
    {"sentence_id": "hij-33-e1-03", "label": "details", "value": "I(S) was made to go(V) [against my will](M)"},
    # --- hij-33-e1-04 ---
    {"sentence_id": "hij-33-e1-04", "label": "overall", "value": "M S V M"},
    {"sentence_id": "hij-33-e1-04", "label": "details", "value": "[In Britain](M) February(S) is thought of(V) [as one of the worst months](M)"},
    # --- hij-33-e1-05 ---
    {"sentence_id": "hij-33-e1-05", "label": "overall", "value": "S V O M"},
    {"sentence_id": "hij-33-e1-05", "label": "details", "value": "She(S) was robbed(V) [of her ring](O) [last night](M)"},
    # --- Hij_33 確認問題 ---
    # --- hij-33-c1-01 ---
    {"sentence_id": "hij-33-c1-01", "label": "overall", "value": "S V O"},
    {"sentence_id": "hij-33-c1-01", "label": "details", "value": "He(S) is compelled to do(V) <what he does not enjoy doing>(O)"},
    # --- hij-33-c1-02 ---
    {"sentence_id": "hij-33-c1-02", "label": "overall", "value": "S V M"},
    {"sentence_id": "hij-33-c1-02", "label": "details", "value": "He(S) is regarded(V) [as one of the most famous writers](M)"},
    # --- hij-33-c1-03 ---
    {"sentence_id": "hij-33-c1-03", "label": "overall", "value": "S V C"},
    {"sentence_id": "hij-33-c1-03", "label": "details", "value": "He(S) was seen(V) reading a book in the library(C)"},
    # --- Hij_33 発展問題 ---
    # --- hij-33-a1-01 ---
    {"sentence_id": "hij-33-a1-01", "label": "overall", "value": "S (M) V C"},
    {"sentence_id": "hij-33-a1-01", "label": "details", "value": "Those people(S) (who do not require help)(M:関係詞節) will not be made to feel(V) unfairly treated [by high levels of taxation](C)"},
]

# ============================================================
# 11. SENTENCE_KNOWLEDGE_TAGS
# ============================================================

SENTENCE_KNOWLEDGE_TAGS = [
    # --- Hij_29 例題 ---
    {"sentence_id": "hij-29-e1-01", "node_id": "hvp-007"},
    {"sentence_id": "hij-29-e1-02", "node_id": "hvp-007"},
    {"sentence_id": "hij-29-e1-03", "node_id": "hvp-007"},
    {"sentence_id": "hij-29-e1-04", "node_id": "hvp-007"},
    {"sentence_id": "hij-29-e1-05", "node_id": "hvp-007"},
    # --- Hij_29 確認問題 ---
    {"sentence_id": "hij-29-c1-01", "node_id": "hvp-007"},
    {"sentence_id": "hij-29-c1-02", "node_id": "hvp-007"},
    {"sentence_id": "hij-29-c1-03", "node_id": "hvp-007"},
    # --- Hij_29 発展問題 ---
    {"sentence_id": "hij-29-a1-01", "node_id": "hvp-007"},
    # --- Hij_30 例題 ---
    {"sentence_id": "hij-30-e1-01", "node_id": "hvp-008"},
    {"sentence_id": "hij-30-e1-02", "node_id": "hvp-008"},
    {"sentence_id": "hij-30-e1-03", "node_id": "hvp-008"},
    {"sentence_id": "hij-30-e1-04", "node_id": "hvp-008"},
    {"sentence_id": "hij-30-e1-05", "node_id": "hvp-008"},
    # --- Hij_30 確認問題 ---
    {"sentence_id": "hij-30-c1-01", "node_id": "hvp-008"},
    {"sentence_id": "hij-30-c1-02", "node_id": "hvp-008"},
    {"sentence_id": "hij-30-c1-03", "node_id": "hvp-008"},
    # --- Hij_30 発展問題 ---
    {"sentence_id": "hij-30-a1-01", "node_id": "hvp-008"},
    # --- Hij_31 例題 ---
    {"sentence_id": "hij-31-e1-01", "node_id": "hvp-009"},
    {"sentence_id": "hij-31-e1-02", "node_id": "hvp-009"},
    {"sentence_id": "hij-31-e1-03", "node_id": "hvp-009"},
    {"sentence_id": "hij-31-e1-04", "node_id": "hvp-009"},
    {"sentence_id": "hij-31-e1-05", "node_id": "hvp-009"},
    # --- Hij_31 確認問題 ---
    {"sentence_id": "hij-31-c1-01", "node_id": "hvp-009"},
    {"sentence_id": "hij-31-c1-02", "node_id": "hvp-009"},
    {"sentence_id": "hij-31-c1-03", "node_id": "hvp-009"},
    # --- Hij_31 発展問題 ---
    {"sentence_id": "hij-31-a1-01", "node_id": "hvp-009"},
    # --- Hij_32 例題 ---
    {"sentence_id": "hij-32-e1-01", "node_id": "hvp-010"},
    {"sentence_id": "hij-32-e1-02", "node_id": "hvp-010"},
    {"sentence_id": "hij-32-e1-03", "node_id": "hvp-010"},
    {"sentence_id": "hij-32-e1-04", "node_id": "hvp-010"},
    {"sentence_id": "hij-32-e1-05", "node_id": "hvp-010"},
    # --- Hij_32 確認問題 ---
    {"sentence_id": "hij-32-c1-01", "node_id": "hvp-010"},
    {"sentence_id": "hij-32-c1-02", "node_id": "hvp-010"},
    {"sentence_id": "hij-32-c1-03", "node_id": "hvp-010"},
    # --- Hij_32 発展問題 ---
    {"sentence_id": "hij-32-a1-01", "node_id": "hvp-010"},
    # --- Hij_33 例題 ---
    {"sentence_id": "hij-33-e1-01", "node_id": "hvp-011"},
    {"sentence_id": "hij-33-e1-02", "node_id": "hvp-011"},
    {"sentence_id": "hij-33-e1-03", "node_id": "hvp-011"},
    {"sentence_id": "hij-33-e1-04", "node_id": "hvp-011"},
    {"sentence_id": "hij-33-e1-05", "node_id": "hvp-011"},
    # --- Hij_33 確認問題 ---
    {"sentence_id": "hij-33-c1-01", "node_id": "hvp-011"},
    {"sentence_id": "hij-33-c1-02", "node_id": "hvp-011"},
    {"sentence_id": "hij-33-c1-03", "node_id": "hvp-011"},
    # --- Hij_33 発展問題 ---
    {"sentence_id": "hij-33-a1-01", "node_id": "hvp-011"},
]
