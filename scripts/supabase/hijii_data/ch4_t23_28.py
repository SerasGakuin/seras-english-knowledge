"""第4章: 動詞の型編 Theme 23-28（第4文型/第5文型/SVO to do/SVA from/of/with B）"""

# ============================================================
# 1. KNOWLEDGE_NODES
# ============================================================

KNOWLEDGE_NODES = [
    {
        "id": "hvp-001",
        "name": "第4文型 SVOO",
        "category": "動詞の型",
        "priority": "P1",
        "notes": "第4文型（S V O1 O2）をとる動詞を3パターンに分類する。(1)「与える」系（give/tell/show/lend/teach）、(2)「してあげる」系（buy/cook/make/get/leave）、(3)「奪う」系（take/cost/save/owe）。動詞を見たらO1 O2の型を予測することが重要。It takes O1 O2 to do / It costs O1 O2 to doは形式主語itの第4文型。",
    },
    {
        "id": "hvp-002",
        "name": "第5文型 SVOC",
        "category": "動詞の型",
        "priority": "P1",
        "notes": "第5文型（S V O C）をとる動詞を3パターンに分類する。(1)CにV原形（使役動詞make/let/have、知覚動詞see/hear/feel、help）、(2)Cに-ing/p.p.（keep/leave/get）、(3)Cに形容詞・名詞（「認識」系think/believe/consider/find、「命名」系call/name）。動詞を見たらO Cの型を予測することが重要。",
    },
    {
        "id": "hvp-003",
        "name": "SVO to do型",
        "category": "動詞の型",
        "priority": "P1",
        "notes": "S V O to do型をとる動詞を3パターンに分類する。(1)「伝達」系（tell/advise/ask/remind）「Oに～するように言う」、(2)「因果」系（enable/allow/cause/encourage/persuade）「Sが原因でOが～する」、(3)「認識」系（expect/want/would like）「Oが～すると思う」。動詞を見たらO to doの型を予測することが重要。",
    },
    {
        "id": "hvp-004",
        "name": "SVA from B型",
        "category": "動詞の型",
        "priority": "P1",
        "notes": "S V A from B型をとる動詞を2パターンに分類する。(1)「分離」系（prevent/keep/stop/prohibit）O from -ing「Oが～するのを妨げる」=「Sのせいで O が～できない」、(2)「区別」系（distinguish/know/tell）A from B「AをBと区別する」。fromがAとBを分離させる機能を持つ。",
    },
    {
        "id": "hvp-005",
        "name": "SVA of B型",
        "category": "動詞の型",
        "priority": "P1",
        "notes": "S V A of B型をとる動詞を2パターンに分類する。(1)「伝達」系（inform/remind/convince/warn）「AにBを伝える」、(2)「略奪」系（rob/deprive/cure/relieve）「AからBを奪う」。informのofは関連のof（aboutに置換可能）、robのofは分離のof。",
    },
    {
        "id": "hvp-006",
        "name": "SVA with B型",
        "category": "動詞の型",
        "priority": "P1",
        "notes": "S V A with B型をとる動詞を2パターンに分類する。(1)「与える」系（provide/present/supply）「AにBを与える」withは所有のwith、provide A with B = provide B for Aの書き換えが可能、(2)「つなぐ」系（associate/combine/compare/connect/share）「AをBとつなげる」。",
    },
]

# ============================================================
# 2. UNDERSTANDING_GOALS
# ============================================================

UNDERSTANDING_GOALS = [
    # hvp-001: 第4文型 SVOO
    {"node_id": "hvp-001", "seq": 1, "goal": "第4文型（S V O1 O2）を「与える」系・「してあげる」系・「奪う」系の3パターンに分類できる"},
    {"node_id": "hvp-001", "seq": 2, "goal": "give/tell/show/lend/teachを見たらO1 O2の型を予測し「O1にO2を与える」と解釈できる"},
    {"node_id": "hvp-001", "seq": 3, "goal": "buy/cook/make/get/leaveを見たらO1 O2の型を予測し「O1にO2をしてあげる」と解釈できる"},
    {"node_id": "hvp-001", "seq": 4, "goal": "It takes O1 O2 to do / It costs O1 O2 to doの形式主語構文を「O1が～するのにO2がかかる」と解釈できる"},
    {"node_id": "hvp-001", "seq": 5, "goal": "save O1 O2「O1のO2を省く」のように「奪う」系動詞の意味を理解できる"},
    # hvp-002: 第5文型 SVOC
    {"node_id": "hvp-002", "seq": 1, "goal": "第5文型（S V O C）を「CにV原形」「Cに-ing/p.p.」「Cに形容詞・名詞」の3パターンに分類できる"},
    {"node_id": "hvp-002", "seq": 2, "goal": "使役動詞（make/let/have）のニュアンスの違い（強制・許可・依頼）を説明できる"},
    {"node_id": "hvp-002", "seq": 3, "goal": "知覚動詞（see/hear/feel）がO Cの型をとり、CにV原形/-ing/p.p.が入ることを理解している"},
    {"node_id": "hvp-002", "seq": 4, "goal": "keep O C（維持）とleave O C（放置）のニュアンスの違いを説明できる"},
    {"node_id": "hvp-002", "seq": 5, "goal": "「認識」系（think/believe/consider/find）と「命名」系（call/name）の第5文型を認識できる"},
    # hvp-003: SVO to do型
    {"node_id": "hvp-003", "seq": 1, "goal": "SVO to do型を「伝達」系・「因果」系・「認識」系の3パターンに分類できる"},
    {"node_id": "hvp-003", "seq": 2, "goal": "tell/advise/ask/remindを見たらO to doの型を予測し「伝達」のニュアンス（命令・助言・依頼・義務）を解釈できる"},
    {"node_id": "hvp-003", "seq": 3, "goal": "enable/allow/cause/encourage/persuadeを見たらO to doの型を予測し「Sが原因でOが～する」という因果関係で解釈できる"},
    {"node_id": "hvp-003", "seq": 4, "goal": "expect/want/would likeを見たらO to doの型を予測し「Oが～すると思う」と解釈できる"},
    # hvp-004: SVA from B型
    {"node_id": "hvp-004", "seq": 1, "goal": "SVA from B型を「分離」系と「区別」系の2パターンに分類できる"},
    {"node_id": "hvp-004", "seq": 2, "goal": "prevent/keep/stop/prohibitを見たらO from -ingの型を予測し「Sのせいで O が～できない」と解釈できる"},
    {"node_id": "hvp-004", "seq": 3, "goal": "distinguish/know/tellを見たらA from Bの型を予測し「AをBと区別する」と解釈できる"},
    # hvp-005: SVA of B型
    {"node_id": "hvp-005", "seq": 1, "goal": "SVA of B型を「伝達」系と「略奪」系の2パターンに分類できる"},
    {"node_id": "hvp-005", "seq": 2, "goal": "inform/remind/convince/warnを見たらA of Bの型を予測し「AにBを伝える」と解釈できる"},
    {"node_id": "hvp-005", "seq": 3, "goal": "rob/deprive/cure/relieveを見たらA of Bの型を予測し「AからBを奪う」と解釈できる"},
    # hvp-006: SVA with B型
    {"node_id": "hvp-006", "seq": 1, "goal": "SVA with B型を「与える」系と「つなぐ」系の2パターンに分類できる"},
    {"node_id": "hvp-006", "seq": 2, "goal": "provide/present/supplyを見たらA with Bの型を予測し「AにBを与える」と解釈できる"},
    {"node_id": "hvp-006", "seq": 3, "goal": "provide A with B = provide B for Aの書き換えを理解している"},
    {"node_id": "hvp-006", "seq": 4, "goal": "associate/combine/compare/connect/shareを見たらA with Bの型を予測し「AをBとつなげる」と解釈できる"},
]

# ============================================================
# 3. CHECK_POINTS
# ============================================================

CHECK_POINTS = [
    # hvp-001: 第4文型 SVOO
    {"node_id": "hvp-001", "seq": 1, "question": "第4文型の「与える」系動詞を5つ挙げよ。", "answer": "give / tell / show / lend / teach。すべて「O1にO2を与える」という意味。"},
    {"node_id": "hvp-001", "seq": 2, "question": "第4文型の「してあげる」系動詞を5つ挙げよ。", "answer": "buy / cook / make / get / leave。すべて「O1にO2をしてあげる」という意味。"},
    {"node_id": "hvp-001", "seq": 3, "question": "It took him ten minutes to solve the problem. の文型と意味は？", "answer": "形式主語itの第4文型。take O1 O2「O1からO2の時間を奪う」= 「彼がその問題を解くのに10分かかった」。"},
    {"node_id": "hvp-001", "seq": 4, "question": "save O1 O2 はどういう意味か？", "answer": "「O1からO2の手間を奪う」=「O1のO2を省く」。奪う系の第4文型。"},
    # hvp-002: 第5文型 SVOC
    {"node_id": "hvp-002", "seq": 1, "question": "第5文型の補語にV原形をとる動詞を3種類挙げよ。", "answer": "使役動詞（make/let/have）、知覚動詞（see/hear/feel）、help。"},
    {"node_id": "hvp-002", "seq": 2, "question": "make/let/haveのニュアンスの違いは？", "answer": "make「無理やり～させる」（強制）、let「～させてあげる」（許可）、have「～してもらう」（依頼）。"},
    {"node_id": "hvp-002", "seq": 3, "question": "keep O CとLeave O Cの違いは？", "answer": "keepは「維持」（わざとその状態を保つ）、leaveは「放置」（単に忘れている）。どちらも「OをCのままにする」。"},
    {"node_id": "hvp-002", "seq": 4, "question": "第5文型の補語に形容詞・名詞をとる動詞を2種類挙げよ。", "answer": "「認識」系（think/believe/consider/find）「OをCと思う」、「命名」系（call/name）「OをCとよぶ」。"},
    # hvp-003: SVO to do型
    {"node_id": "hvp-003", "seq": 1, "question": "SVO to do型の「伝達」系動詞を4つ挙げ、ニュアンスを述べよ。", "answer": "tell（命令）、advise（助言）、ask（依頼）、remind（義務）。すべて「Oに～するように伝える」。"},
    {"node_id": "hvp-003", "seq": 2, "question": "SVO to do型の「因果」系動詞を5つ挙げよ。", "answer": "enable / allow / cause / encourage / persuade。すべて「Sが原因でOが～する」という因果関係。"},
    {"node_id": "hvp-003", "seq": 3, "question": "expect O to doの意味は？", "answer": "「Oが～すると予期する」。「認識」系の動詞で、O to doの型を予測する。"},
    # hvp-004: SVA from B型
    {"node_id": "hvp-004", "seq": 1, "question": "SVA from B型の「分離」系動詞を4つ挙げよ。", "answer": "prevent / keep / stop / prohibit。すべてO from -ing「Oが～するのを妨げる」。"},
    {"node_id": "hvp-004", "seq": 2, "question": "distinguish A from Bの意味は？同じ型をとる動詞を他に2つ挙げよ。", "answer": "「AをBと区別する」。know A from B、tell A from B。"},
    {"node_id": "hvp-004", "seq": 3, "question": "prevent O from -ingとenable O to doはどういう関係か？", "answer": "正反対の関係。enableは「Sのおかげで O が～できる」、preventは「Sのせいで O が～できない」。"},
    # hvp-005: SVA of B型
    {"node_id": "hvp-005", "seq": 1, "question": "SVA of B型の「伝達」系動詞を4つ挙げ、伝達内容を述べよ。", "answer": "inform（情報）、remind（記憶）、convince（確信）、warn（警告）。すべて「AにBを伝える」。"},
    {"node_id": "hvp-005", "seq": 2, "question": "robとdepriveの違いは？", "answer": "robはおもに金品などをむりやり奪う。depriveは必ずしも違法性をともなわず権利や自由などを奪う。"},
    {"node_id": "hvp-005", "seq": 3, "question": "cure A of Bの意味は？", "answer": "「AからB（病気）を奪う」=「AのB（病気）を治す」。略奪系の動詞。"},
    # hvp-006: SVA with B型
    {"node_id": "hvp-006", "seq": 1, "question": "provide A with Bのwithの意味は？書き換えは？", "answer": "所有のwith「～をもって」。provide A with B = provide B for A。"},
    {"node_id": "hvp-006", "seq": 2, "question": "SVA with B型の「つなぐ」系動詞を5つ挙げよ。", "answer": "associate / combine / compare / connect / share。すべて「AをBとつなげる」系の意味。"},
    {"node_id": "hvp-006", "seq": 3, "question": "share A with Bの意味は？", "answer": "「AをBとつなげて持つ」=「AをBと共有する」。"},
]

# ============================================================
# 4. NODE_PREREQUISITES
# ============================================================

NODE_PREREQUISITES = [
    {"node_id": "hvp-002", "prerequisite_id": "hvp-001"},
    {"node_id": "hvp-003", "prerequisite_id": "hvp-002"},
    {"node_id": "hvp-004", "prerequisite_id": "hvp-003"},
    {"node_id": "hvp-005", "prerequisite_id": "hvp-004"},
    {"node_id": "hvp-006", "prerequisite_id": "hvp-005"},
]

# ============================================================
# 5. KNOWLEDGE_REFERENCES
# ============================================================

KNOWLEDGE_REFERENCES = [
    {"node_id": "hvp-001", "book": "肘井の読解のための英文法", "section_id": "Hij_23", "pages": "p.158-163"},
    {"node_id": "hvp-002", "book": "肘井の読解のための英文法", "section_id": "Hij_24", "pages": "p.164-169"},
    {"node_id": "hvp-003", "book": "肘井の読解のための英文法", "section_id": "Hij_25", "pages": "p.170-175"},
    {"node_id": "hvp-004", "book": "肘井の読解のための英文法", "section_id": "Hij_26", "pages": "p.176-179"},
    {"node_id": "hvp-005", "book": "肘井の読解のための英文法", "section_id": "Hij_27", "pages": "p.180-183"},
    {"node_id": "hvp-006", "book": "肘井の読解のための英文法", "section_id": "Hij_28", "pages": "p.184-189"},
]

# ============================================================
# 6. SECTIONS
# ============================================================

SECTIONS = [
    {
        "id": "Hij_23",
        "book": "肘井の読解のための英文法",
        "title": "Theme 23 第4文型で英文が読める",
        "pages": "p.158-163",
        "type": "drill",
    },
    {
        "id": "Hij_24",
        "book": "肘井の読解のための英文法",
        "title": "Theme 24 第5文型で英文が読める",
        "pages": "p.164-169",
        "type": "drill",
    },
    {
        "id": "Hij_25",
        "book": "肘井の読解のための英文法",
        "title": "Theme 25 SVO to do型で英文が読める",
        "pages": "p.170-175",
        "type": "drill",
    },
    {
        "id": "Hij_26",
        "book": "肘井の読解のための英文法",
        "title": "Theme 26 SVA from B型で英文が読める",
        "pages": "p.176-179",
        "type": "drill",
    },
    {
        "id": "Hij_27",
        "book": "肘井の読解のための英文法",
        "title": "Theme 27 SVA of B型で英文が読める",
        "pages": "p.180-183",
        "type": "drill",
    },
    {
        "id": "Hij_28",
        "book": "肘井の読解のための英文法",
        "title": "Theme 28 SVA with B型で英文が読める",
        "pages": "p.184-189",
        "type": "drill",
    },
]

# ============================================================
# 7. SECTION_PREREQUISITES
# ============================================================

SECTION_PREREQUISITES = [
    {"section_id": "Hij_24", "prerequisite_id": "Hij_23"},
    {"section_id": "Hij_25", "prerequisite_id": "Hij_24"},
    {"section_id": "Hij_26", "prerequisite_id": "Hij_25"},
    {"section_id": "Hij_27", "prerequisite_id": "Hij_26"},
    {"section_id": "Hij_28", "prerequisite_id": "Hij_27"},
]

# ============================================================
# 8. SECTION_KNOWLEDGE_NODES
# ============================================================

SECTION_KNOWLEDGE_NODES = [
    {"section_id": "Hij_23", "node_id": "hvp-001", "seq": 1},
    {"section_id": "Hij_24", "node_id": "hvp-002", "seq": 1},
    {"section_id": "Hij_25", "node_id": "hvp-003", "seq": 1},
    {"section_id": "Hij_26", "node_id": "hvp-004", "seq": 1},
    {"section_id": "Hij_27", "node_id": "hvp-005", "seq": 1},
    {"section_id": "Hij_28", "node_id": "hvp-006", "seq": 1},
]

# ============================================================
# 9. SENTENCES
# ============================================================

SENTENCES = [
    # ==========================================================
    # Hij_23 — Theme 23 第4文型で英文が読める
    # ==========================================================
    # ----------------------------------------------------------
    # Hij_23 — 例題 (5問)
    # ----------------------------------------------------------
    {
        "id": "hij-23-e1-01",
        "section_id": "Hij_23",
        "drill": 1,
        "number": 1,
        "role": "example",
        "english": "He gave his sister a postcard and a stamp.",
        "japanese": "彼は妹にポストカードと切手をあげた。",
        "notes": None,
    },
    {
        "id": "hij-23-e1-02",
        "section_id": "Hij_23",
        "drill": 1,
        "number": 2,
        "role": "example",
        "english": "Moderate exercise will do you good.",
        "japanese": "適度な運動は、あなたに利益を与えてくれるだろう。",
        "notes": None,
    },
    {
        "id": "hij-23-e1-03",
        "section_id": "Hij_23",
        "drill": 1,
        "number": 3,
        "role": "example",
        "english": "Her father will buy Jane the computer.",
        "japanese": "ジェーンの父は、彼女にコンピュータを買ってあげるつもりだ。",
        "notes": None,
    },
    {
        "id": "hij-23-e1-04",
        "section_id": "Hij_23",
        "drill": 1,
        "number": 4,
        "role": "example",
        "english": "It took him ten minutes to solve the problem.",
        "japanese": "彼がその問題を解くのに10分かかった。",
        "notes": None,
    },
    {
        "id": "hij-23-e1-05",
        "section_id": "Hij_23",
        "drill": 1,
        "number": 5,
        "role": "example",
        "english": "It cost me five thousand dollars to buy the car.",
        "japanese": "私がその車を買うのに、5000ドルかかった。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_23 — ポイント例文 (3問)
    # ----------------------------------------------------------
    {
        "id": "hij-23-e1-06",
        "section_id": "Hij_23",
        "drill": 1,
        "number": 6,
        "role": "example",
        "english": "My parents lent me the car to go there.",
        "japanese": "両親が、私にそこに行くための車を貸してくれた。",
        "notes": None,
    },
    {
        "id": "hij-23-e1-07",
        "section_id": "Hij_23",
        "drill": 1,
        "number": 7,
        "role": "example",
        "english": "Could you get me some water?",
        "japanese": "私に水をとってくださいますか。",
        "notes": None,
    },
    {
        "id": "hij-23-e1-08",
        "section_id": "Hij_23",
        "drill": 1,
        "number": 8,
        "role": "example",
        "english": "His e-mail saved me the trouble of going there.",
        "japanese": "彼のEメールのおかげで、私がそこに行く手間が省けた。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_23 — 確認問題 (4問)
    # ----------------------------------------------------------
    {
        "id": "hij-23-c1-01",
        "section_id": "Hij_23",
        "drill": 2,
        "number": 1,
        "role": "practice",
        "english": "These books do young people great harm.",
        "japanese": "これらの本は、若者に大きな害を与える。",
        "notes": None,
    },
    {
        "id": "hij-23-c1-02",
        "section_id": "Hij_23",
        "drill": 2,
        "number": 2,
        "role": "practice",
        "english": "I'll show you some pictures I took in Japan.",
        "japanese": "私は日本で撮った写真数枚をあなたに見せるつもりです。",
        "notes": None,
    },
    {
        "id": "hij-23-c1-03",
        "section_id": "Hij_23",
        "drill": 2,
        "number": 3,
        "role": "practice",
        "english": "It costs me 5,000 yen to go to Nagoya from here by train.",
        "japanese": "私がここから名古屋に電車で行くには5000円かかる。",
        "notes": None,
    },
    {
        "id": "hij-23-c1-04",
        "section_id": "Hij_23",
        "drill": 2,
        "number": 4,
        "role": "practice",
        "english": "It takes three hours to walk from here to the station.",
        "japanese": "ここから駅まで歩いて行くのに3時間かかる。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_23 — 発展問題 (1問)
    # ----------------------------------------------------------
    {
        "id": "hij-23-a1-01",
        "section_id": "Hij_23",
        "drill": 3,
        "number": 1,
        "role": "advanced",
        "english": "Common sense tells us that all of us would notice such a big change in the outcome of a choice.",
        "japanese": "私たちのだれもが、ある選択の結果が、そのように大きく変化すれば気づくだろうということは、常識によってわかる。",
        "notes": "京都大",
    },
    # ==========================================================
    # Hij_24 — Theme 24 第5文型で英文が読める
    # ==========================================================
    # ----------------------------------------------------------
    # Hij_24 — 例題 (5問)
    # ----------------------------------------------------------
    {
        "id": "hij-24-e1-01",
        "section_id": "Hij_24",
        "drill": 1,
        "number": 1,
        "role": "example",
        "english": "My brother made me clean his room.",
        "japanese": "私の兄は、私に彼の部屋を掃除させた。",
        "notes": None,
    },
    {
        "id": "hij-24-e1-02",
        "section_id": "Hij_24",
        "drill": 1,
        "number": 2,
        "role": "example",
        "english": "Mary saw her mother enter the house.",
        "japanese": "メアリーは、彼女の母親がその家に入るのを見た。",
        "notes": None,
    },
    {
        "id": "hij-24-e1-03",
        "section_id": "Hij_24",
        "drill": 1,
        "number": 3,
        "role": "example",
        "english": "Being clearer will help you write a better essay.",
        "japanese": "もっと明確化すると、あなたがよりよい論文を書くのに役立つだろう。",
        "notes": None,
    },
    {
        "id": "hij-24-e1-04",
        "section_id": "Hij_24",
        "drill": 1,
        "number": 4,
        "role": "example",
        "english": "I must get this refrigerator repaired.",
        "japanese": "私はこの冷蔵庫を修理してもらわなければならない。",
        "notes": None,
    },
    {
        "id": "hij-24-e1-05",
        "section_id": "Hij_24",
        "drill": 1,
        "number": 5,
        "role": "example",
        "english": "I found San Francisco very cool.",
        "japanese": "私は、サンフランシスコがとても涼しいと思った。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_24 — ポイント例文 (4問)
    # ----------------------------------------------------------
    {
        "id": "hij-24-e1-06",
        "section_id": "Hij_24",
        "drill": 1,
        "number": 6,
        "role": "example",
        "english": "You left the door unlocked last night.",
        "japanese": "あなたは昨晩そのドアの鍵をあけっぱなしにした。",
        "notes": "leave O C「OをCのままにする」（放置）",
    },
    {
        "id": "hij-24-e1-07",
        "section_id": "Hij_24",
        "drill": 1,
        "number": 7,
        "role": "example",
        "english": "You kept the door unlocked last night.",
        "japanese": "あなたは昨晩そのドアの鍵をあけっぱなしにした。",
        "notes": "keep O C「OをCのままにする」（維持、わざと）",
    },
    {
        "id": "hij-24-e1-08",
        "section_id": "Hij_24",
        "drill": 1,
        "number": 8,
        "role": "example",
        "english": "I thought it wrong to do such a thing.",
        "japanese": "私は、そのようなことをするのは間違っていると思った。",
        "notes": None,
    },
    {
        "id": "hij-24-e1-09",
        "section_id": "Hij_24",
        "drill": 1,
        "number": 9,
        "role": "example",
        "english": "They called the baby Thomas.",
        "japanese": "彼らは、その赤ん坊をトーマスと名付けた。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_24 — 確認問題 (4問)
    # ----------------------------------------------------------
    {
        "id": "hij-24-c1-01",
        "section_id": "Hij_24",
        "drill": 2,
        "number": 1,
        "role": "practice",
        "english": "I made him understand the message.",
        "japanese": "私は、彼にその伝言を理解させた。",
        "notes": None,
    },
    {
        "id": "hij-24-c1-02",
        "section_id": "Hij_24",
        "drill": 2,
        "number": 2,
        "role": "practice",
        "english": "I heard a funny noise coming from the back of my car.",
        "japanese": "私は、おかしな音が車のうしろからしているのが聞こえた。",
        "notes": None,
    },
    {
        "id": "hij-24-c1-03",
        "section_id": "Hij_24",
        "drill": 2,
        "number": 3,
        "role": "practice",
        "english": "They had their sister clean their room for the party.",
        "japanese": "その人たちは、妹にパーティーの部屋を掃除してもらった。",
        "notes": None,
    },
    {
        "id": "hij-24-c1-04",
        "section_id": "Hij_24",
        "drill": 2,
        "number": 4,
        "role": "practice",
        "english": "You'd better keep the door locked when you are out.",
        "japanese": "あなたが外に出るときは、ドアに鍵をかけたままにしたほうがよい。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_24 — 発展問題 (1問)
    # ----------------------------------------------------------
    {
        "id": "hij-24-a1-01",
        "section_id": "Hij_24",
        "drill": 3,
        "number": 1,
        "role": "advanced",
        "english": "I smile and keep quiet, running the risk of letting her think that I agree with her.",
        "japanese": "私は微笑んで何も言わず、彼女に同意していると思わせるリスクをおかしている。",
        "notes": "東京大",
    },
    # ==========================================================
    # Hij_25 — Theme 25 SVO to do型で英文が読める
    # ==========================================================
    # ----------------------------------------------------------
    # Hij_25 — 例題 (5問)
    # ----------------------------------------------------------
    {
        "id": "hij-25-e1-01",
        "section_id": "Hij_25",
        "drill": 1,
        "number": 1,
        "role": "example",
        "english": "He told me to wait in the room.",
        "japanese": "彼は、私にその部屋で待つように言った。",
        "notes": None,
    },
    {
        "id": "hij-25-e1-02",
        "section_id": "Hij_25",
        "drill": 1,
        "number": 2,
        "role": "example",
        "english": "His mother advised him to become a doctor.",
        "japanese": "彼の母は、彼に医者になるように助言した。",
        "notes": None,
    },
    {
        "id": "hij-25-e1-03",
        "section_id": "Hij_25",
        "drill": 1,
        "number": 3,
        "role": "example",
        "english": "Her help will enable me to do the job sooner.",
        "japanese": "彼女の助けのおかげで、私はその仕事をもっと早くできるだろう。",
        "notes": None,
    },
    {
        "id": "hij-25-e1-04",
        "section_id": "Hij_25",
        "drill": 1,
        "number": 4,
        "role": "example",
        "english": "The salesperson persuaded me to buy a computer.",
        "japanese": "そのセールスマンは私を説得して、コンピュータを買わせた。",
        "notes": None,
    },
    {
        "id": "hij-25-e1-05",
        "section_id": "Hij_25",
        "drill": 1,
        "number": 5,
        "role": "example",
        "english": "I expect it to rain heavily tomorrow.",
        "japanese": "私は明日ひどい雨が降ると予期する。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_25 — ポイント例文 (2問)
    # ----------------------------------------------------------
    {
        "id": "hij-25-e1-06",
        "section_id": "Hij_25",
        "drill": 1,
        "number": 6,
        "role": "example",
        "english": "She reminded me to turn off all the lights.",
        "japanese": "彼女は、私にすべての電気を消すことを思い出させてくれた。",
        "notes": None,
    },
    {
        "id": "hij-25-e1-07",
        "section_id": "Hij_25",
        "drill": 1,
        "number": 7,
        "role": "example",
        "english": "I wanted my mother to praise me for my hard work.",
        "japanese": "私は、母が私の一生懸命さをほめてくれることを望んでいた。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_25 — 確認問題 (4問)
    # ----------------------------------------------------------
    {
        "id": "hij-25-c1-01",
        "section_id": "Hij_25",
        "drill": 2,
        "number": 1,
        "role": "practice",
        "english": "He asked his mother to wake him up at seven.",
        "japanese": "彼は彼の母に、7時に彼を起こすように頼んだ。",
        "notes": None,
    },
    {
        "id": "hij-25-c1-02",
        "section_id": "Hij_25",
        "drill": 2,
        "number": 2,
        "role": "practice",
        "english": "My father wouldn't allow me to borrow his car.",
        "japanese": "私の父は、私が彼の車を借りるのをどうしても許してくれないだろう。",
        "notes": None,
    },
    {
        "id": "hij-25-c1-03",
        "section_id": "Hij_25",
        "drill": 2,
        "number": 3,
        "role": "practice",
        "english": "His mother advised him to be more careful in his choice of words.",
        "japanese": "彼の母は彼に、言葉を選ぶのにもっと注意深くなるように助言した。",
        "notes": None,
    },
    {
        "id": "hij-25-c1-04",
        "section_id": "Hij_25",
        "drill": 2,
        "number": 4,
        "role": "practice",
        "english": "His behavior caused me to laugh.",
        "japanese": "彼のふるまいが原因で、私は笑ってしまった。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_25 — 発展問題 (1問)
    # ----------------------------------------------------------
    {
        "id": "hij-25-a1-01",
        "section_id": "Hij_25",
        "drill": 3,
        "number": 1,
        "role": "advanced",
        "english": "She appealed to doctors in the USA to encourage parents to read to their young children.",
        "japanese": "彼女はアメリカの医師に、両親が幼い子どもたちに本を読んで聞かせるのを促すように、心からお願いをした。",
        "notes": "信州大",
    },
    # ==========================================================
    # Hij_26 — Theme 26 SVA from B型で英文が読める
    # ==========================================================
    # ----------------------------------------------------------
    # Hij_26 — 例題 (4問)
    # ----------------------------------------------------------
    {
        "id": "hij-26-e1-01",
        "section_id": "Hij_26",
        "drill": 1,
        "number": 1,
        "role": "example",
        "english": "Living in the city prevents people from becoming rich.",
        "japanese": "その町に住んでいるせいで、人びとは裕福になれない。",
        "notes": None,
    },
    {
        "id": "hij-26-e1-02",
        "section_id": "Hij_26",
        "drill": 1,
        "number": 2,
        "role": "example",
        "english": "The train's delay kept me from arriving there in time.",
        "japanese": "電車が遅れたせいで、私は時間内にそこに着けなかった。",
        "notes": None,
    },
    {
        "id": "hij-26-e1-03",
        "section_id": "Hij_26",
        "drill": 1,
        "number": 3,
        "role": "example",
        "english": "Children can't distinguish good from evil.",
        "japanese": "子どもたちは、善悪を区別できない。",
        "notes": None,
    },
    {
        "id": "hij-26-e1-04",
        "section_id": "Hij_26",
        "drill": 1,
        "number": 4,
        "role": "example",
        "english": "I can't tell a genuine pearl from an imitation.",
        "japanese": "私は、本物の真珠と模造品を区別できない。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_26 — 確認問題 (3問)
    # ----------------------------------------------------------
    {
        "id": "hij-26-c1-01",
        "section_id": "Hij_26",
        "drill": 2,
        "number": 1,
        "role": "practice",
        "english": "Sickness prevented her from going on a picnic.",
        "japanese": "病気のせいで、彼女はピクニックに行けなかった。",
        "notes": None,
    },
    {
        "id": "hij-26-c1-02",
        "section_id": "Hij_26",
        "drill": 2,
        "number": 2,
        "role": "practice",
        "english": "Her parents prohibited her from staying out after ten.",
        "japanese": "彼女の両親は、彼女が10時以降外出するのを禁止した。",
        "notes": None,
    },
    {
        "id": "hij-26-c1-03",
        "section_id": "Hij_26",
        "drill": 2,
        "number": 3,
        "role": "practice",
        "english": "We want our children to know right from wrong.",
        "japanese": "私たちは、子どもたちに善悪を区別してもらいたい。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_26 — 発展問題 (1問)
    # ----------------------------------------------------------
    {
        "id": "hij-26-a1-01",
        "section_id": "Hij_26",
        "drill": 3,
        "number": 1,
        "role": "advanced",
        "english": "Later in childhood, no doubt, they learn to distinguish fiction from fact.",
        "japanese": "幼児期の後期になると、間違いなく、子どもはつくり話と事実を区別できるようになる。",
        "notes": "上智大／改",
    },
    # ==========================================================
    # Hij_27 — Theme 27 SVA of B型で英文が読める
    # ==========================================================
    # ----------------------------------------------------------
    # Hij_27 — 例題 (4問)
    # ----------------------------------------------------------
    {
        "id": "hij-27-e1-01",
        "section_id": "Hij_27",
        "drill": 1,
        "number": 1,
        "role": "example",
        "english": "The police informed us of the traffic accident.",
        "japanese": "警察は私たちにその交通事故を知らせてくれた。",
        "notes": None,
    },
    {
        "id": "hij-27-e1-02",
        "section_id": "Hij_27",
        "drill": 1,
        "number": 2,
        "role": "example",
        "english": "Talking with you reminds me of your father.",
        "japanese": "あなたと話すと、私はあなたのお父さんを思い出す。",
        "notes": None,
    },
    {
        "id": "hij-27-e1-03",
        "section_id": "Hij_27",
        "drill": 1,
        "number": 3,
        "role": "example",
        "english": "They robbed her of her money on her way home.",
        "japanese": "その人たちは、彼女が家へ帰る途中に彼女からお金を奪った。",
        "notes": None,
    },
    {
        "id": "hij-27-e1-04",
        "section_id": "Hij_27",
        "drill": 1,
        "number": 4,
        "role": "example",
        "english": "They deprived him of his liberty.",
        "japanese": "その人たちは、彼から自由を奪った。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_27 — 確認問題 (3問)
    # ----------------------------------------------------------
    {
        "id": "hij-27-c1-01",
        "section_id": "Hij_27",
        "drill": 2,
        "number": 1,
        "role": "practice",
        "english": "They robbed him of his money on his way home from the office.",
        "japanese": "その人たちは、彼が事務所から家に帰る途中、お金を奪った。",
        "notes": None,
    },
    {
        "id": "hij-27-c1-02",
        "section_id": "Hij_27",
        "drill": 2,
        "number": 2,
        "role": "practice",
        "english": "They convinced us of their innocence.",
        "japanese": "その人たちは私たちに、自分たちの無実を納得させた。",
        "notes": None,
    },
    {
        "id": "hij-27-c1-03",
        "section_id": "Hij_27",
        "drill": 2,
        "number": 3,
        "role": "practice",
        "english": "This medicine will cure your father of that disease.",
        "japanese": "この薬は、あなたのお父さんのその病気を治すだろう。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_27 — 発展問題 (1問)
    # ----------------------------------------------------------
    {
        "id": "hij-27-a1-01",
        "section_id": "Hij_27",
        "drill": 3,
        "number": 1,
        "role": "advanced",
        "english": "The appointment of another doctor to help me has relieved me of a lot of work.",
        "japanese": "私を助けてくれるもう一人別の医者が任命されたことで、私のたくさんの労力が取り除かれた。",
        "notes": "大阪産業大／改",
    },
    # ==========================================================
    # Hij_28 — Theme 28 SVA with B型で英文が読める
    # ==========================================================
    # ----------------------------------------------------------
    # Hij_28 — 例題 (5問)
    # ----------------------------------------------------------
    {
        "id": "hij-28-e1-01",
        "section_id": "Hij_28",
        "drill": 1,
        "number": 1,
        "role": "example",
        "english": "Parents should provide their children with decent clothing.",
        "japanese": "両親は子どもたちに、きちんとした服を与えるべきだ。",
        "notes": None,
    },
    {
        "id": "hij-28-e1-02",
        "section_id": "Hij_28",
        "drill": 1,
        "number": 2,
        "role": "example",
        "english": "We will supply the villagers with food.",
        "japanese": "私たちは村人に、食料を供給するつもりだ。",
        "notes": None,
    },
    {
        "id": "hij-28-e1-03",
        "section_id": "Hij_28",
        "drill": 1,
        "number": 3,
        "role": "example",
        "english": "He often compares himself with his colleagues.",
        "japanese": "彼はよく、自分を同僚と比較する。",
        "notes": None,
    },
    {
        "id": "hij-28-e1-04",
        "section_id": "Hij_28",
        "drill": 1,
        "number": 4,
        "role": "example",
        "english": "Doctors associate smoking with lung cancer.",
        "japanese": "医者は、喫煙を肺がんと関連づける。",
        "notes": None,
    },
    {
        "id": "hij-28-e1-05",
        "section_id": "Hij_28",
        "drill": 1,
        "number": 5,
        "role": "example",
        "english": "Human beings share many features with monkeys.",
        "japanese": "人間は多くの特徴を、サルと共有している。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_28 — ポイント例文 (4問)
    # ----------------------------------------------------------
    {
        "id": "hij-28-e1-06",
        "section_id": "Hij_28",
        "drill": 1,
        "number": 6,
        "role": "example",
        "english": "The president presented him with a good picture.",
        "japanese": "社長は彼にすてきな絵を贈った。",
        "notes": None,
    },
    {
        "id": "hij-28-e1-07",
        "section_id": "Hij_28",
        "drill": 1,
        "number": 7,
        "role": "example",
        "english": "It is important to combine theory with practice.",
        "japanese": "理論を実践と結びつけることが重要だ。",
        "notes": None,
    },
    {
        "id": "hij-28-e1-08",
        "section_id": "Hij_28",
        "drill": 1,
        "number": 8,
        "role": "example",
        "english": "Many people often connect Japan with Mt. Fuji.",
        "japanese": "多くの人がよく、日本を富士山と関連づける。",
        "notes": None,
    },
    {
        "id": "hij-28-e1-09",
        "section_id": "Hij_28",
        "drill": 1,
        "number": 9,
        "role": "example",
        "english": "Parents should provide decent clothing for their children.",
        "japanese": "両親は子どもたちに、きちんとした服を与えるべきだ。",
        "notes": "provide A with B = provide B for A の書き換え",
    },
    # ----------------------------------------------------------
    # Hij_28 — 確認問題 (3問)
    # ----------------------------------------------------------
    {
        "id": "hij-28-c1-01",
        "section_id": "Hij_28",
        "drill": 2,
        "number": 1,
        "role": "practice",
        "english": "The manager presented Henry with a gold watch.",
        "japanese": "その経営者は、ヘンリーに金時計を贈った。",
        "notes": None,
    },
    {
        "id": "hij-28-c1-02",
        "section_id": "Hij_28",
        "drill": 2,
        "number": 2,
        "role": "practice",
        "english": "I make it a rule to share information with my colleagues.",
        "japanese": "私は情報を、同僚と共有することにしている。",
        "notes": None,
    },
    {
        "id": "hij-28-c1-03",
        "section_id": "Hij_28",
        "drill": 2,
        "number": 3,
        "role": "practice",
        "english": "It is wrong to compare your child with other children.",
        "japanese": "自分の子どもをほかの子どもと比べることは、間違っている。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_28 — 発展問題 (1問)
    # ----------------------------------------------------------
    {
        "id": "hij-28-a1-01",
        "section_id": "Hij_28",
        "drill": 3,
        "number": 1,
        "role": "advanced",
        "english": "Modern parents provide their children with far too many passive amusements, such as shows and good things to eat.",
        "japanese": "現代の親は、子どもたちにテレビ番組やおいしい食べ物のような、受動的な楽しみをあまりにも多く与えている。",
        "notes": "青山学院大",
    },
]

# ============================================================
# 10. SENTENCE_STRUCTURES
# ============================================================

SENTENCE_STRUCTURES = [
    # --- Hij_23 例題 ---
    {"sentence_id": "hij-23-e1-01", "label": "overall", "value": "S V O1 O2"},
    {"sentence_id": "hij-23-e1-01", "label": "details", "value": "He(S) gave(V) his sister(O1) a postcard and a stamp(O2)"},
    {"sentence_id": "hij-23-e1-02", "label": "overall", "value": "S V O1 O2"},
    {"sentence_id": "hij-23-e1-02", "label": "details", "value": "Moderate exercise(S) will do(V) you(O1) good(O2)"},
    {"sentence_id": "hij-23-e1-03", "label": "overall", "value": "S V O1 O2"},
    {"sentence_id": "hij-23-e1-03", "label": "details", "value": "Her father(S) will buy(V) Jane(O1) the computer(O2)"},
    {"sentence_id": "hij-23-e1-04", "label": "overall", "value": "S V O1 O2 S'"},
    {"sentence_id": "hij-23-e1-04", "label": "details", "value": "It(S:形式主語) took(V) him(O1) ten minutes(O2) <to solve the problem>(S':真主語)"},
    {"sentence_id": "hij-23-e1-05", "label": "overall", "value": "S V O1 O2 S'"},
    {"sentence_id": "hij-23-e1-05", "label": "details", "value": "It(S:形式主語) cost(V) me(O1) five thousand dollars(O2) <to buy the car>(S':真主語)"},
    # --- Hij_23 ポイント例文 ---
    {"sentence_id": "hij-23-e1-06", "label": "overall", "value": "S V O1 O2 M"},
    {"sentence_id": "hij-23-e1-06", "label": "details", "value": "My parents(S) lent(V) me(O1) the car(O2) <to go there>(M)"},
    {"sentence_id": "hij-23-e1-07", "label": "overall", "value": "S V O1 O2"},
    {"sentence_id": "hij-23-e1-07", "label": "details", "value": "you(S) get(V) me(O1) some water(O2)"},
    {"sentence_id": "hij-23-e1-08", "label": "overall", "value": "S V O1 O2 M"},
    {"sentence_id": "hij-23-e1-08", "label": "details", "value": "His e-mail(S) saved(V) me(O1) the trouble(O2) (of going there)(M)"},
    # --- Hij_23 確認問題 ---
    {"sentence_id": "hij-23-c1-01", "label": "overall", "value": "S V O1 O2"},
    {"sentence_id": "hij-23-c1-01", "label": "details", "value": "These books(S) do(V) young people(O1) great harm(O2)"},
    {"sentence_id": "hij-23-c1-02", "label": "overall", "value": "S V O1 O2 (M)"},
    {"sentence_id": "hij-23-c1-02", "label": "details", "value": "I(S) 'll show(V) you(O1) some pictures(O2) ((which) I took in Japan)(M:関係代名詞省略)"},
    {"sentence_id": "hij-23-c1-03", "label": "overall", "value": "S V O1 O2 S'"},
    {"sentence_id": "hij-23-c1-03", "label": "details", "value": "It(S:形式主語) costs(V) me(O1) 5,000 yen(O2) <to go to Nagoya from here by train>(S':真主語)"},
    {"sentence_id": "hij-23-c1-04", "label": "overall", "value": "S V O2 S'"},
    {"sentence_id": "hij-23-c1-04", "label": "details", "value": "It(S:形式主語) takes(V) (you:O1省略) three hours(O2) <to walk from here to the station>(S':真主語)"},
    # --- Hij_23 発展問題 ---
    {"sentence_id": "hij-23-a1-01", "label": "overall", "value": "S V O1 O2"},
    {"sentence_id": "hij-23-a1-01", "label": "details", "value": "Common sense(S) tells(V) us(O1) <that all of us would notice such a big change in the outcome of a choice>(O2:名詞節)"},
    # --- Hij_24 例題 ---
    {"sentence_id": "hij-24-e1-01", "label": "overall", "value": "S V O C"},
    {"sentence_id": "hij-24-e1-01", "label": "details", "value": "My brother(S) made(V) me(O) clean his room(C:V原形)"},
    {"sentence_id": "hij-24-e1-02", "label": "overall", "value": "S V O C"},
    {"sentence_id": "hij-24-e1-02", "label": "details", "value": "Mary(S) saw(V) her mother(O) enter the house(C:V原形)"},
    {"sentence_id": "hij-24-e1-03", "label": "overall", "value": "S V O C"},
    {"sentence_id": "hij-24-e1-03", "label": "details", "value": "Being clearer(S) will help(V) you(O) write a better essay(C:V原形)"},
    {"sentence_id": "hij-24-e1-04", "label": "overall", "value": "S V O C"},
    {"sentence_id": "hij-24-e1-04", "label": "details", "value": "I(S) must get(V) this refrigerator(O) repaired(C:p.p.)"},
    {"sentence_id": "hij-24-e1-05", "label": "overall", "value": "S V O C"},
    {"sentence_id": "hij-24-e1-05", "label": "details", "value": "I(S) found(V) San Francisco(O) very cool(C:形容詞)"},
    # --- Hij_24 ポイント例文 ---
    {"sentence_id": "hij-24-e1-06", "label": "overall", "value": "S V O C M"},
    {"sentence_id": "hij-24-e1-06", "label": "details", "value": "You(S) left(V) the door(O) unlocked(C:p.p.) [last night](M)"},
    {"sentence_id": "hij-24-e1-07", "label": "overall", "value": "S V O C M"},
    {"sentence_id": "hij-24-e1-07", "label": "details", "value": "You(S) kept(V) the door(O) unlocked(C:p.p.) [last night](M)"},
    {"sentence_id": "hij-24-e1-08", "label": "overall", "value": "S V O C O'"},
    {"sentence_id": "hij-24-e1-08", "label": "details", "value": "I(S) thought(V) it(O:形式目的語) wrong(C:形容詞) <to do such a thing>(O':真目的語)"},
    {"sentence_id": "hij-24-e1-09", "label": "overall", "value": "S V O C"},
    {"sentence_id": "hij-24-e1-09", "label": "details", "value": "They(S) called(V) the baby(O) Thomas(C:名詞)"},
    # --- Hij_24 確認問題 ---
    {"sentence_id": "hij-24-c1-01", "label": "overall", "value": "S V O C"},
    {"sentence_id": "hij-24-c1-01", "label": "details", "value": "I(S) made(V) him(O) understand the message(C:V原形)"},
    {"sentence_id": "hij-24-c1-02", "label": "overall", "value": "S V O C"},
    {"sentence_id": "hij-24-c1-02", "label": "details", "value": "I(S) heard(V) a funny noise(O) coming from the back of my car(C:-ing)"},
    {"sentence_id": "hij-24-c1-03", "label": "overall", "value": "S V O C M"},
    {"sentence_id": "hij-24-c1-03", "label": "details", "value": "They(S) had(V) their sister(O) clean their room(C:V原形) [for the party](M)"},
    {"sentence_id": "hij-24-c1-04", "label": "overall", "value": "S V O C M"},
    {"sentence_id": "hij-24-c1-04", "label": "details", "value": "You(S) 'd better keep(V) the door(O) locked(C:p.p.) [when you are out](M)"},
    # --- Hij_24 発展問題 ---
    {"sentence_id": "hij-24-a1-01", "label": "overall", "value": "S V1 V2 C M"},
    {"sentence_id": "hij-24-a1-01", "label": "details", "value": "I(S) smile(V1) and keep(V2) quiet(C), [running the risk of letting her think that I agree with her](M:分詞構文)"},
    # --- Hij_25 例題 ---
    {"sentence_id": "hij-25-e1-01", "label": "overall", "value": "S V O to do"},
    {"sentence_id": "hij-25-e1-01", "label": "details", "value": "He(S) told(V) me(O) <to wait in the room>(to do)"},
    {"sentence_id": "hij-25-e1-02", "label": "overall", "value": "S V O to do"},
    {"sentence_id": "hij-25-e1-02", "label": "details", "value": "His mother(S) advised(V) him(O) <to become a doctor>(to do)"},
    {"sentence_id": "hij-25-e1-03", "label": "overall", "value": "S V O to do"},
    {"sentence_id": "hij-25-e1-03", "label": "details", "value": "Her help(S) will enable(V) me(O) <to do the job sooner>(to do)"},
    {"sentence_id": "hij-25-e1-04", "label": "overall", "value": "S V O to do"},
    {"sentence_id": "hij-25-e1-04", "label": "details", "value": "The salesperson(S) persuaded(V) me(O) <to buy a computer>(to do)"},
    {"sentence_id": "hij-25-e1-05", "label": "overall", "value": "S V O to do"},
    {"sentence_id": "hij-25-e1-05", "label": "details", "value": "I(S) expect(V) it(O:天候のit) <to rain heavily tomorrow>(to do)"},
    # --- Hij_25 ポイント例文 ---
    {"sentence_id": "hij-25-e1-06", "label": "overall", "value": "S V O to do"},
    {"sentence_id": "hij-25-e1-06", "label": "details", "value": "She(S) reminded(V) me(O) <to turn off all the lights>(to do)"},
    {"sentence_id": "hij-25-e1-07", "label": "overall", "value": "S V O to do"},
    {"sentence_id": "hij-25-e1-07", "label": "details", "value": "I(S) wanted(V) my mother(O) <to praise me for my hard work>(to do)"},
    # --- Hij_25 確認問題 ---
    {"sentence_id": "hij-25-c1-01", "label": "overall", "value": "S V O to do"},
    {"sentence_id": "hij-25-c1-01", "label": "details", "value": "He(S) asked(V) his mother(O) <to wake him up at seven>(to do)"},
    {"sentence_id": "hij-25-c1-02", "label": "overall", "value": "S V O to do"},
    {"sentence_id": "hij-25-c1-02", "label": "details", "value": "My father(S) wouldn't allow(V) me(O) <to borrow his car>(to do)"},
    {"sentence_id": "hij-25-c1-03", "label": "overall", "value": "S V O to do"},
    {"sentence_id": "hij-25-c1-03", "label": "details", "value": "His mother(S) advised(V) him(O) <to be more careful in his choice of words>(to do)"},
    {"sentence_id": "hij-25-c1-04", "label": "overall", "value": "S V O to do"},
    {"sentence_id": "hij-25-c1-04", "label": "details", "value": "His behavior(S) caused(V) me(O) <to laugh>(to do)"},
    # --- Hij_25 発展問題 ---
    {"sentence_id": "hij-25-a1-01", "label": "overall", "value": "S V M O to do"},
    {"sentence_id": "hij-25-a1-01", "label": "details", "value": "She(S) appealed(V) [to doctors in the USA](M) <to encourage parents to read to their young children>(to do)"},
    # --- Hij_26 例題 ---
    {"sentence_id": "hij-26-e1-01", "label": "overall", "value": "S V O from -ing"},
    {"sentence_id": "hij-26-e1-01", "label": "details", "value": "Living in the city(S) prevents(V) people(O) from becoming rich(-ing)"},
    {"sentence_id": "hij-26-e1-02", "label": "overall", "value": "S V O from -ing"},
    {"sentence_id": "hij-26-e1-02", "label": "details", "value": "The train's delay(S) kept(V) me(O) from arriving there in time(-ing)"},
    {"sentence_id": "hij-26-e1-03", "label": "overall", "value": "S V A from B"},
    {"sentence_id": "hij-26-e1-03", "label": "details", "value": "Children(S) can't distinguish(V) good(A) from evil(B)"},
    {"sentence_id": "hij-26-e1-04", "label": "overall", "value": "S V A from B"},
    {"sentence_id": "hij-26-e1-04", "label": "details", "value": "I(S) can't tell(V) a genuine pearl(A) from an imitation(B)"},
    # --- Hij_26 確認問題 ---
    {"sentence_id": "hij-26-c1-01", "label": "overall", "value": "S V O from -ing"},
    {"sentence_id": "hij-26-c1-01", "label": "details", "value": "Sickness(S) prevented(V) her(O) from going on a picnic(-ing)"},
    {"sentence_id": "hij-26-c1-02", "label": "overall", "value": "S V O from -ing"},
    {"sentence_id": "hij-26-c1-02", "label": "details", "value": "Her parents(S) prohibited(V) her(O) from staying out after ten(-ing)"},
    {"sentence_id": "hij-26-c1-03", "label": "overall", "value": "S V O to do"},
    {"sentence_id": "hij-26-c1-03", "label": "details", "value": "We(S) want(V) our children(O) <to know right from wrong>(to do)"},
    # --- Hij_26 発展問題 ---
    {"sentence_id": "hij-26-a1-01", "label": "overall", "value": "M M S V to do"},
    {"sentence_id": "hij-26-a1-01", "label": "details", "value": "[Later in childhood](M) no doubt(M) they(S) learn(V) <to distinguish fiction from fact>(to do)"},
    # --- Hij_27 例題 ---
    {"sentence_id": "hij-27-e1-01", "label": "overall", "value": "S V A of B"},
    {"sentence_id": "hij-27-e1-01", "label": "details", "value": "The police(S) informed(V) us(A) of the traffic accident(B)"},
    {"sentence_id": "hij-27-e1-02", "label": "overall", "value": "S V A of B"},
    {"sentence_id": "hij-27-e1-02", "label": "details", "value": "Talking with you(S) reminds(V) me(A) of your father(B)"},
    {"sentence_id": "hij-27-e1-03", "label": "overall", "value": "S V A of B M"},
    {"sentence_id": "hij-27-e1-03", "label": "details", "value": "They(S) robbed(V) her(A) of her money(B) [on her way home](M)"},
    {"sentence_id": "hij-27-e1-04", "label": "overall", "value": "S V A of B"},
    {"sentence_id": "hij-27-e1-04", "label": "details", "value": "They(S) deprived(V) him(A) of his liberty(B)"},
    # --- Hij_27 確認問題 ---
    {"sentence_id": "hij-27-c1-01", "label": "overall", "value": "S V A of B M"},
    {"sentence_id": "hij-27-c1-01", "label": "details", "value": "They(S) robbed(V) him(A) of his money(B) [on his way home from the office](M)"},
    {"sentence_id": "hij-27-c1-02", "label": "overall", "value": "S V A of B"},
    {"sentence_id": "hij-27-c1-02", "label": "details", "value": "They(S) convinced(V) us(A) of their innocence(B)"},
    {"sentence_id": "hij-27-c1-03", "label": "overall", "value": "S V A of B"},
    {"sentence_id": "hij-27-c1-03", "label": "details", "value": "This medicine(S) will cure(V) your father(A) of that disease(B)"},
    # --- Hij_27 発展問題 ---
    {"sentence_id": "hij-27-a1-01", "label": "overall", "value": "S (M) V A of B"},
    {"sentence_id": "hij-27-a1-01", "label": "details", "value": "The appointment(S) (of another doctor to help me)(M) has relieved(V) me(A) of a lot of work(B)"},
    # --- Hij_28 例題 ---
    {"sentence_id": "hij-28-e1-01", "label": "overall", "value": "S V A with B"},
    {"sentence_id": "hij-28-e1-01", "label": "details", "value": "Parents(S) should provide(V) their children(A) with decent clothing(B)"},
    {"sentence_id": "hij-28-e1-02", "label": "overall", "value": "S V A with B"},
    {"sentence_id": "hij-28-e1-02", "label": "details", "value": "We(S) will supply(V) the villagers(A) with food(B)"},
    {"sentence_id": "hij-28-e1-03", "label": "overall", "value": "S M V A with B"},
    {"sentence_id": "hij-28-e1-03", "label": "details", "value": "He(S) often(M) compares(V) himself(A) with his colleagues(B)"},
    {"sentence_id": "hij-28-e1-04", "label": "overall", "value": "S V A with B"},
    {"sentence_id": "hij-28-e1-04", "label": "details", "value": "Doctors(S) associate(V) smoking(A) with lung cancer(B)"},
    {"sentence_id": "hij-28-e1-05", "label": "overall", "value": "S V A with B"},
    {"sentence_id": "hij-28-e1-05", "label": "details", "value": "Human beings(S) share(V) many features(A) with monkeys(B)"},
    # --- Hij_28 ポイント例文 ---
    {"sentence_id": "hij-28-e1-06", "label": "overall", "value": "S V A with B"},
    {"sentence_id": "hij-28-e1-06", "label": "details", "value": "The president(S) presented(V) him(A) with a good picture(B)"},
    {"sentence_id": "hij-28-e1-07", "label": "overall", "value": "S V C S'"},
    {"sentence_id": "hij-28-e1-07", "label": "details", "value": "It(S:形式主語) is(V) important(C) <to combine theory(A) with practice(B)>(S':真主語)"},
    {"sentence_id": "hij-28-e1-08", "label": "overall", "value": "S M V A with B"},
    {"sentence_id": "hij-28-e1-08", "label": "details", "value": "Many people(S) often(M) connect(V) Japan(A) with Mt. Fuji(B)"},
    {"sentence_id": "hij-28-e1-09", "label": "overall", "value": "S V B for A"},
    {"sentence_id": "hij-28-e1-09", "label": "details", "value": "Parents(S) should provide(V) decent clothing(B) for their children(A)"},
    # --- Hij_28 確認問題 ---
    {"sentence_id": "hij-28-c1-01", "label": "overall", "value": "S V A with B"},
    {"sentence_id": "hij-28-c1-01", "label": "details", "value": "The manager(S) presented(V) Henry(A) with a gold watch(B)"},
    {"sentence_id": "hij-28-c1-02", "label": "overall", "value": "S V O C S'"},
    {"sentence_id": "hij-28-c1-02", "label": "details", "value": "I(S) make(V) it(O:形式目的語) a rule(C) <to share information(A) with my colleagues(B)>(S':真目的語)"},
    {"sentence_id": "hij-28-c1-03", "label": "overall", "value": "S V C S'"},
    {"sentence_id": "hij-28-c1-03", "label": "details", "value": "It(S:形式主語) is(V) wrong(C) <to compare your child(A) with other children(B)>(S':真主語)"},
    # --- Hij_28 発展問題 ---
    {"sentence_id": "hij-28-a1-01", "label": "overall", "value": "S V A with B M"},
    {"sentence_id": "hij-28-a1-01", "label": "details", "value": "Modern parents(S) provide(V) their children(A) with far too many passive amusements(B), [such as shows and good things to eat](M)"},
]

# ============================================================
# 11. SENTENCE_KNOWLEDGE_TAGS
# ============================================================

SENTENCE_KNOWLEDGE_TAGS = [
    # --- Hij_23 例題 ---
    {"sentence_id": "hij-23-e1-01", "node_id": "hvp-001"},
    {"sentence_id": "hij-23-e1-02", "node_id": "hvp-001"},
    {"sentence_id": "hij-23-e1-03", "node_id": "hvp-001"},
    {"sentence_id": "hij-23-e1-04", "node_id": "hvp-001"},
    {"sentence_id": "hij-23-e1-05", "node_id": "hvp-001"},
    # --- Hij_23 ポイント例文 ---
    {"sentence_id": "hij-23-e1-06", "node_id": "hvp-001"},
    {"sentence_id": "hij-23-e1-07", "node_id": "hvp-001"},
    {"sentence_id": "hij-23-e1-08", "node_id": "hvp-001"},
    # --- Hij_23 確認問題 ---
    {"sentence_id": "hij-23-c1-01", "node_id": "hvp-001"},
    {"sentence_id": "hij-23-c1-02", "node_id": "hvp-001"},
    {"sentence_id": "hij-23-c1-03", "node_id": "hvp-001"},
    {"sentence_id": "hij-23-c1-04", "node_id": "hvp-001"},
    # --- Hij_23 発展問題 ---
    {"sentence_id": "hij-23-a1-01", "node_id": "hvp-001"},
    # --- Hij_24 例題 ---
    {"sentence_id": "hij-24-e1-01", "node_id": "hvp-002"},
    {"sentence_id": "hij-24-e1-02", "node_id": "hvp-002"},
    {"sentence_id": "hij-24-e1-03", "node_id": "hvp-002"},
    {"sentence_id": "hij-24-e1-04", "node_id": "hvp-002"},
    {"sentence_id": "hij-24-e1-05", "node_id": "hvp-002"},
    # --- Hij_24 ポイント例文 ---
    {"sentence_id": "hij-24-e1-06", "node_id": "hvp-002"},
    {"sentence_id": "hij-24-e1-07", "node_id": "hvp-002"},
    {"sentence_id": "hij-24-e1-08", "node_id": "hvp-002"},
    {"sentence_id": "hij-24-e1-09", "node_id": "hvp-002"},
    # --- Hij_24 確認問題 ---
    {"sentence_id": "hij-24-c1-01", "node_id": "hvp-002"},
    {"sentence_id": "hij-24-c1-02", "node_id": "hvp-002"},
    {"sentence_id": "hij-24-c1-03", "node_id": "hvp-002"},
    {"sentence_id": "hij-24-c1-04", "node_id": "hvp-002"},
    # --- Hij_24 発展問題 ---
    {"sentence_id": "hij-24-a1-01", "node_id": "hvp-002"},
    # --- Hij_25 例題 ---
    {"sentence_id": "hij-25-e1-01", "node_id": "hvp-003"},
    {"sentence_id": "hij-25-e1-02", "node_id": "hvp-003"},
    {"sentence_id": "hij-25-e1-03", "node_id": "hvp-003"},
    {"sentence_id": "hij-25-e1-04", "node_id": "hvp-003"},
    {"sentence_id": "hij-25-e1-05", "node_id": "hvp-003"},
    # --- Hij_25 ポイント例文 ---
    {"sentence_id": "hij-25-e1-06", "node_id": "hvp-003"},
    {"sentence_id": "hij-25-e1-07", "node_id": "hvp-003"},
    # --- Hij_25 確認問題 ---
    {"sentence_id": "hij-25-c1-01", "node_id": "hvp-003"},
    {"sentence_id": "hij-25-c1-02", "node_id": "hvp-003"},
    {"sentence_id": "hij-25-c1-03", "node_id": "hvp-003"},
    {"sentence_id": "hij-25-c1-04", "node_id": "hvp-003"},
    # --- Hij_25 発展問題 ---
    {"sentence_id": "hij-25-a1-01", "node_id": "hvp-003"},
    # --- Hij_26 例題 ---
    {"sentence_id": "hij-26-e1-01", "node_id": "hvp-004"},
    {"sentence_id": "hij-26-e1-02", "node_id": "hvp-004"},
    {"sentence_id": "hij-26-e1-03", "node_id": "hvp-004"},
    {"sentence_id": "hij-26-e1-04", "node_id": "hvp-004"},
    # --- Hij_26 確認問題 ---
    {"sentence_id": "hij-26-c1-01", "node_id": "hvp-004"},
    {"sentence_id": "hij-26-c1-02", "node_id": "hvp-004"},
    {"sentence_id": "hij-26-c1-03", "node_id": "hvp-004"},
    # --- Hij_26 発展問題 ---
    {"sentence_id": "hij-26-a1-01", "node_id": "hvp-004"},
    # --- Hij_27 例題 ---
    {"sentence_id": "hij-27-e1-01", "node_id": "hvp-005"},
    {"sentence_id": "hij-27-e1-02", "node_id": "hvp-005"},
    {"sentence_id": "hij-27-e1-03", "node_id": "hvp-005"},
    {"sentence_id": "hij-27-e1-04", "node_id": "hvp-005"},
    # --- Hij_27 確認問題 ---
    {"sentence_id": "hij-27-c1-01", "node_id": "hvp-005"},
    {"sentence_id": "hij-27-c1-02", "node_id": "hvp-005"},
    {"sentence_id": "hij-27-c1-03", "node_id": "hvp-005"},
    # --- Hij_27 発展問題 ---
    {"sentence_id": "hij-27-a1-01", "node_id": "hvp-005"},
    # --- Hij_28 例題 ---
    {"sentence_id": "hij-28-e1-01", "node_id": "hvp-006"},
    {"sentence_id": "hij-28-e1-02", "node_id": "hvp-006"},
    {"sentence_id": "hij-28-e1-03", "node_id": "hvp-006"},
    {"sentence_id": "hij-28-e1-04", "node_id": "hvp-006"},
    {"sentence_id": "hij-28-e1-05", "node_id": "hvp-006"},
    # --- Hij_28 ポイント例文 ---
    {"sentence_id": "hij-28-e1-06", "node_id": "hvp-006"},
    {"sentence_id": "hij-28-e1-07", "node_id": "hvp-006"},
    {"sentence_id": "hij-28-e1-08", "node_id": "hvp-006"},
    {"sentence_id": "hij-28-e1-09", "node_id": "hvp-006"},
    # --- Hij_28 確認問題 ---
    {"sentence_id": "hij-28-c1-01", "node_id": "hvp-006"},
    {"sentence_id": "hij-28-c1-02", "node_id": "hvp-006"},
    {"sentence_id": "hij-28-c1-03", "node_id": "hvp-006"},
    # --- Hij_28 発展問題 ---
    {"sentence_id": "hij-28-a1-01", "node_id": "hvp-006"},
]
