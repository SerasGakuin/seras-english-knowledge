"""第2章: 識別編 Theme 08-10（to do / -ing / 過去分詞の識別）"""

# ============================================================
# 1. KNOWLEDGE_NODES
# ============================================================

KNOWLEDGE_NODES = [
    {
        "id": "hid-001",
        "name": "to doの識別（名詞的/形容詞的/副詞的用法）",
        "category": "識別",
        "priority": "P1",
        "notes": "文中でto+動詞の原形を見たら不定詞と特定し、名詞的用法・形容詞的用法・副詞的用法の3パターンを識別する。S・O・Cなら名詞的用法「～すること」、前の名詞を修飾するなら形容詞的用法「～するための」、動詞と目的・手段の関係なら副詞的用法「～するために」。",
    },
    {
        "id": "hid-007",
        "name": "to doの識別（be to不定詞）",
        "category": "識別",
        "priority": "P1",
        "notes": "be動詞のうしろにto doがくるとき、S=Cにならなければbe to不定詞。be to不定詞は文脈により予定(be going to)・義務(should)・可能(can)・意志(will)・運命(shall)の5つの意味を持つ「万能助動詞」。未来の副詞(next year等)とセットなら予定、if節中ならwillと同じ意志、否定文ならcanと同じ可能。",
    },
    {
        "id": "hid-002",
        "name": "-ingの識別（動名詞/進行形）",
        "category": "識別",
        "priority": "P1",
        "notes": "文中で-ingを見つけたら動名詞か進行形かを識別する。S・O・Cなら動名詞「～すること」。be動詞のうしろでS=Cが成り立たないなら現在分詞で進行形。be動詞のうしろの-ingはS=Cなら動名詞（SVC）、成り立たないなら進行形。文頭の-ingは名詞句をつくり主語なら動名詞。",
    },
    {
        "id": "hid-008",
        "name": "-ingの識別（現在分詞の形容詞用法/分詞構文）",
        "category": "識別",
        "priority": "P1",
        "notes": "形容詞句をつくってうしろから名詞を修飾するなら現在分詞の形容詞用法。-ing～,SV. / S,-ing～,V. / SV,-ing～. の型なら分詞構文。文頭の-ingが-ing～,SV.の型なら分詞構文で「時」か「理由」、文尾の分詞構文は「そして～」。文頭の-ingが動名詞か分詞構文かは、名詞句をつくり主語なら動名詞、-ing～,SV.の型なら分詞構文で識別する。",
    },
    {
        "id": "hid-003",
        "name": "過去分詞の識別（受動態/完了形/名詞修飾/分詞構文）",
        "category": "識別",
        "priority": "P1",
        "notes": "文中で過去分詞を見つけたら4パターンを識別する。be動詞とセットなら受動態「～れる・～られる」。haveとセットなら完了形（現在完了have p.p./過去完了had p.p./未来完了will have p.p.）。名詞のうしろで形容詞句をつくっていれば名詞修飾。-ing(p.p.)～,SV.の型にあてはまれば分詞構文で、文頭なら「時」か「理由」。受動態で「～れる・～られる」が不自然な場合は能動態になおして訳す。",
    },
]

# ============================================================
# 2. UNDERSTANDING_GOALS
# ============================================================

UNDERSTANDING_GOALS = [
    # hid-001: to doの識別（3用法）
    {"node_id": "hid-001", "seq": 1, "goal": "to+動詞の原形を見たら不定詞と特定し、名詞的・形容詞的・副詞的用法の3パターンを意識できる"},
    {"node_id": "hid-001", "seq": 2, "goal": "不定詞がS・O・Cの位置にあれば名詞的用法「～すること」と判断できる"},
    {"node_id": "hid-001", "seq": 3, "goal": "「名詞 to do」の形で前の名詞を修飾していれば形容詞的用法「～するための」と判断できる"},
    {"node_id": "hid-001", "seq": 4, "goal": "動詞とto doが目的と手段の関係であれば副詞的用法「～するために」と判断できる"},
    # hid-007: to doの識別（be to不定詞）
    {"node_id": "hid-007", "seq": 1, "goal": "be動詞のうしろのto doがS=Cにならないことを根拠にbe to不定詞と識別できる"},
    {"node_id": "hid-007", "seq": 2, "goal": "be to不定詞の5つの意味（予定・義務・可能・意志・運命）を文脈から判断できる"},
    {"node_id": "hid-007", "seq": 3, "goal": "文脈指標（未来の副詞=予定、if節=意志、否定=可能など）からbe to不定詞の意味を特定できる"},
    # hid-002: -ingの識別（動名詞/進行形）
    {"node_id": "hid-002", "seq": 1, "goal": "-ingを見つけたら動名詞か進行形かの識別を意識できる"},
    {"node_id": "hid-002", "seq": 2, "goal": "be動詞のうしろの-ingでS=Cが成り立つなら動名詞（SVC）、成り立たないなら進行形と判断できる"},
    {"node_id": "hid-002", "seq": 3, "goal": "文頭の-ingが名詞句をつくり文の主語になっていれば動名詞「～すること」と判断できる"},
    # hid-008: -ingの識別（現在分詞の形容詞用法/分詞構文）
    {"node_id": "hid-008", "seq": 1, "goal": "現在分詞が形容詞句をつくってうしろから名詞を修飾するパターンを認識できる"},
    {"node_id": "hid-008", "seq": 2, "goal": "分詞構文の3つの型（文頭・文中・文尾）を認識し、文頭なら「時」か「理由」、文尾なら「そして～」と訳せる"},
    {"node_id": "hid-008", "seq": 3, "goal": "文頭の-ingが-ing～,SV.の型にあてはまれば分詞構文と識別し、動名詞と区別できる"},
    # hid-003: 過去分詞の識別
    {"node_id": "hid-003", "seq": 1, "goal": "過去分詞を見つけたら受動態・完了形・名詞修飾・分詞構文の4パターンを意識できる"},
    {"node_id": "hid-003", "seq": 2, "goal": "be動詞+p.p.で受動態、have+p.p.で完了形と識別できる"},
    {"node_id": "hid-003", "seq": 3, "goal": "名詞のうしろの過去分詞が形容詞句をつくって前の名詞を修飾するパターンを認識できる"},
    {"node_id": "hid-003", "seq": 4, "goal": "-ing(p.p.)～,SV.の型で過去分詞の分詞構文と識別し、文頭なら「時」か「理由」と訳せる"},
]

# ============================================================
# 3. CHECK_POINTS
# ============================================================

CHECK_POINTS = [
    # hid-001: to doの識別（3用法）
    {"node_id": "hid-001", "seq": 1, "question": "不定詞の3用法は何か？", "answer": "(1)名詞的用法（S・O・Cになる）、(2)形容詞的用法（名詞 to doの形で前の名詞を修飾）、(3)副詞的用法（動詞と目的・手段の関係）。"},
    {"node_id": "hid-001", "seq": 2, "question": "I would like to take advantage of the opportunity to visit the museum. のto takeとto visitの用法は？", "answer": "to takeは名詞的用法でlikeの目的語。to visitは形容詞的用法で前のthe opportunityを修飾する。"},
    {"node_id": "hid-001", "seq": 3, "question": "In summer, we usually go to the pool to swim. のto swimはどの用法か？", "answer": "副詞的用法。to swim「泳ぐために」が目的で、go to the pool「プールに行く」が手段。動詞と目的・手段の関係。"},
    # hid-007: to doの識別（be to不定詞）
    {"node_id": "hid-007", "seq": 1, "question": "be to不定詞と不定詞の名詞的用法を区別する方法は？", "answer": "be動詞のうしろのto doが文のCならば名詞的用法（S=Cが成り立つ）、Cでなければbe to不定詞。"},
    {"node_id": "hid-007", "seq": 2, "question": "be to不定詞の5つの意味は？", "answer": "予定（be going to）、義務（should）、可能（can）、意志（will）、運命（shall）。文脈により使い分ける。"},
    {"node_id": "hid-007", "seq": 3, "question": "A new store is to be built next year. のis toは何の意味か？", "answer": "予定。未来の副詞next yearと一緒で「～する予定だ」（be going to）の意味。"},
    # hid-002: -ingの識別（動名詞/進行形）
    {"node_id": "hid-002", "seq": 1, "question": "-ingが動名詞になるのはどのパターンか？", "answer": "S・O・Cの位置にあれば動名詞「～すること」。文頭の-ingが名詞句をつくり主語なら動名詞。"},
    {"node_id": "hid-002", "seq": 2, "question": "be動詞のうしろの-ingが動名詞か進行形かを見分ける方法は？", "answer": "S=Cが成り立てば動名詞（第2文型のC）、成り立たなければ進行形の現在分詞。"},
    {"node_id": "hid-002", "seq": 3, "question": "My hobby is writing a novel. と She is writing a novel. の-ingの違いは？", "answer": "前者は動名詞（My hobby = writing a novelでS=C）、後者は進行形（She ≠ writingでS≠C）。"},
    # hid-008: -ingの識別（現在分詞の形容詞用法/分詞構文）
    {"node_id": "hid-008", "seq": 1, "question": "現在分詞の形容詞用法はどのような形で名詞を修飾するか？", "answer": "名詞+-ingの形でうしろから名詞を修飾する。例: an article questioning the cause「原因を疑う記事」。"},
    {"node_id": "hid-008", "seq": 2, "question": "分詞構文の3つの型と訳し方は？", "answer": "文頭: -ing(p.p.)～, SV.（「時」か「理由」）、文中: S, -ing(p.p.)～, V.、文尾: SV, -ing(p.p.)～.（「そして～」）。"},
    {"node_id": "hid-008", "seq": 3, "question": "文頭の-ingが動名詞か分詞構文かを見分ける方法は？", "answer": "名詞句をつくり文の主語になっていれば動名詞「～すること」、-ing～, SV.の型にあてはまれば分詞構文。"},
    # hid-003: 過去分詞の識別
    {"node_id": "hid-003", "seq": 1, "question": "過去分詞の4パターンは？", "answer": "(1)受動態（be動詞+p.p.）、(2)完了形（have+p.p.）、(3)名詞修飾（名詞+p.p.）、(4)分詞構文（文頭・文中・文尾で動詞を修飾）。"},
    {"node_id": "hid-003", "seq": 2, "question": "受動態を訳すとき「～れる・～られる」で不自然な場合の対処法は？", "answer": "能動態になおして訳す。受動態の主語は能動態の目的語なので、目的語を主語にした能動態で考える。"},
    {"node_id": "hid-003", "seq": 3, "question": "I received a letter written in English. のwrittenの役割は？", "answer": "過去分詞で、written in Englishまでの形容詞句をつくりa letterを修飾する。「英語で書かれた手紙」。"},
    {"node_id": "hid-003", "seq": 4, "question": "過去分詞の分詞構文と現在分詞の分詞構文は同じ型か？", "answer": "同じ型。-ing(p.p.)～, SV. の型で、-ingでも過去分詞(p.p.)でも分詞構文になる。文頭なら「時」か「理由」で訳す。"},
]

# ============================================================
# 4. NODE_PREREQUISITES
# ============================================================

NODE_PREREQUISITES = [
    {"node_id": "hid-001", "prerequisite_id": "hch-001"},
    {"node_id": "hid-007", "prerequisite_id": "hid-001"},
    {"node_id": "hid-002", "prerequisite_id": "hid-001"},
    {"node_id": "hid-008", "prerequisite_id": "hid-002"},
    {"node_id": "hid-003", "prerequisite_id": "hid-002"},
    {"node_id": "hid-003", "prerequisite_id": "hid-008"},
]

# ============================================================
# 5. KNOWLEDGE_REFERENCES
# ============================================================

KNOWLEDGE_REFERENCES = [
    {"node_id": "hid-001", "book": "肘井の読解のための英文法", "section_id": "Hij_08", "pages": "p.64-69"},
    {"node_id": "hid-007", "book": "肘井の読解のための英文法", "section_id": "Hij_08", "pages": "p.64-69"},
    {"node_id": "hid-002", "book": "肘井の読解のための英文法", "section_id": "Hij_09", "pages": "p.70-75"},
    {"node_id": "hid-008", "book": "肘井の読解のための英文法", "section_id": "Hij_09", "pages": "p.70-75"},
    {"node_id": "hid-003", "book": "肘井の読解のための英文法", "section_id": "Hij_10", "pages": "p.76-79"},
]

# ============================================================
# 6. SECTIONS
# ============================================================

SECTIONS = [
    {
        "id": "Hij_08",
        "book": "肘井の読解のための英文法",
        "title": "Theme 08 to doの識別で英文が読める",
        "pages": "p.64-69",
        "type": "drill",
    },
    {
        "id": "Hij_09",
        "book": "肘井の読解のための英文法",
        "title": "Theme 09 -ingの識別で英文が読める",
        "pages": "p.70-75",
        "type": "drill",
    },
    {
        "id": "Hij_10",
        "book": "肘井の読解のための英文法",
        "title": "Theme 10 過去分詞の識別で英文が読める",
        "pages": "p.76-79",
        "type": "drill",
    },
]

# ============================================================
# 7. SECTION_PREREQUISITES
# ============================================================

SECTION_PREREQUISITES = [
    {"section_id": "Hij_08", "prerequisite_id": "Hij_07_2"},
    {"section_id": "Hij_09", "prerequisite_id": "Hij_08"},
    {"section_id": "Hij_10", "prerequisite_id": "Hij_09"},
]

# ============================================================
# 8. SECTION_KNOWLEDGE_NODES
# ============================================================

SECTION_KNOWLEDGE_NODES = [
    {"section_id": "Hij_08", "node_id": "hid-001", "seq": 1},
    {"section_id": "Hij_08", "node_id": "hid-007", "seq": 2},
    {"section_id": "Hij_09", "node_id": "hid-002", "seq": 1},
    {"section_id": "Hij_09", "node_id": "hid-008", "seq": 2},
    {"section_id": "Hij_10", "node_id": "hid-003", "seq": 1},
]

# ============================================================
# 9. SENTENCES
# ============================================================

SENTENCES = [
    # ==========================================================
    # Hij_08 -- Theme 08 to doの識別で英文が読める
    # ==========================================================
    # ----------------------------------------------------------
    # Hij_08 -- 例題 (4問)
    # ----------------------------------------------------------
    {
        "id": "hij-08-e1-01",
        "section_id": "Hij_08",
        "drill": 1,
        "number": 1,
        "role": "example",
        "english": "To know the temperature of the Earth is important.",
        "japanese": "地球の気温を知ることは重要だ。",
        "notes": None,
    },
    {
        "id": "hij-08-e1-02",
        "section_id": "Hij_08",
        "drill": 1,
        "number": 2,
        "role": "example",
        "english": "I would like to take advantage of the opportunity to visit the museum.",
        "japanese": "私はその博物館を訪ねる機会を利用したい。",
        "notes": None,
    },
    {
        "id": "hij-08-e1-03",
        "section_id": "Hij_08",
        "drill": 1,
        "number": 3,
        "role": "example",
        "english": "In summer, we usually go to the pool to swim.",
        "japanese": "夏には、私たちはたいていプールに泳ぎに行く。",
        "notes": None,
    },
    {
        "id": "hij-08-e1-04",
        "section_id": "Hij_08",
        "drill": 1,
        "number": 4,
        "role": "example",
        "english": "A new store is to be built next year.",
        "japanese": "新しい店が来年建てられる予定だ。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_08 -- ポイント14 例文 (2問)
    # ----------------------------------------------------------
    {
        "id": "hij-08-e1-05",
        "section_id": "Hij_08",
        "drill": 1,
        "number": 5,
        "role": "example",
        "english": "I promise to write to you.",
        "japanese": "私はあなたに手紙を書くことを約束します。",
        "notes": "ポイント14 例文1",
    },
    {
        "id": "hij-08-e1-06",
        "section_id": "Hij_08",
        "drill": 1,
        "number": 6,
        "role": "example",
        "english": "I intend to finish the book in a day.",
        "japanese": "私は、その本を一日で読み終えるつもりだ。",
        "notes": "ポイント14 例文2",
    },
    # ----------------------------------------------------------
    # Hij_08 -- ポイント15 例文 (2問)
    # ----------------------------------------------------------
    {
        "id": "hij-08-e1-07",
        "section_id": "Hij_08",
        "drill": 1,
        "number": 7,
        "role": "example",
        "english": "You must keep learning if you are to succeed.",
        "japanese": "もし成功するつもりなら、学び続けなければいけない。",
        "notes": "ポイント15 例文1",
    },
    {
        "id": "hij-08-e1-08",
        "section_id": "Hij_08",
        "drill": 1,
        "number": 8,
        "role": "example",
        "english": "The ring was not to be found.",
        "japanese": "その指輪は発見できなかった。",
        "notes": "ポイント15 例文2",
    },
    # ----------------------------------------------------------
    # Hij_08 -- 確認問題 (4問)
    # ----------------------------------------------------------
    {
        "id": "hij-08-c1-01",
        "section_id": "Hij_08",
        "drill": 2,
        "number": 1,
        "role": "practice",
        "english": "The most effective way to develop self-esteem is to have faith in yourself.",
        "japanese": "自尊心を発達させる最も効果的な方法は、自分自身を信じることだ。",
        "notes": None,
    },
    {
        "id": "hij-08-c1-02",
        "section_id": "Hij_08",
        "drill": 2,
        "number": 2,
        "role": "practice",
        "english": "The President is to visit Japan next month.",
        "japanese": "大統領は、来月日本を訪れる予定だ。",
        "notes": None,
    },
    {
        "id": "hij-08-c1-03",
        "section_id": "Hij_08",
        "drill": 2,
        "number": 3,
        "role": "practice",
        "english": "He went to the store to buy a present for her.",
        "japanese": "彼は彼女にプレゼントを買うためにそのお店に行った。",
        "notes": None,
    },
    {
        "id": "hij-08-c1-04",
        "section_id": "Hij_08",
        "drill": 2,
        "number": 4,
        "role": "practice",
        "english": "Do you have anything to say about this opinion?",
        "japanese": "あなたはこの意見について何か言うことがありますか。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_08 -- 発展問題 (1問)
    # ----------------------------------------------------------
    {
        "id": "hij-08-a1-01",
        "section_id": "Hij_08",
        "drill": 3,
        "number": 1,
        "role": "advanced",
        "english": "To keep this newly competitive labor market fair and open, equality of educational opportunities is necessary.",
        "japanese": "この新しい競争の激しい労働市場を公平かつオープンにしておくために、教育の機会均等が必要だ。",
        "notes": "北海道大",
    },
    # ==========================================================
    # Hij_09 -- Theme 09 -ingの識別で英文が読める
    # ==========================================================
    # ----------------------------------------------------------
    # Hij_09 -- 例題 (4問)
    # ----------------------------------------------------------
    {
        "id": "hij-09-e1-01",
        "section_id": "Hij_09",
        "drill": 1,
        "number": 1,
        "role": "example",
        "english": "Learning to read a language is best taught in the classroom.",
        "japanese": "言語を読めるようになることは、教室で最もよく教えられる。",
        "notes": None,
    },
    {
        "id": "hij-09-e1-02",
        "section_id": "Hij_09",
        "drill": 1,
        "number": 2,
        "role": "example",
        "english": "The telephone rang when I was taking a shower.",
        "japanese": "私がシャワーを浴びている最中に、電話が鳴った。",
        "notes": None,
    },
    {
        "id": "hij-09-e1-03",
        "section_id": "Hij_09",
        "drill": 1,
        "number": 3,
        "role": "example",
        "english": "She published an article questioning the cause of the accident.",
        "japanese": "彼女は、その事故の原因を疑う記事を公表した。",
        "notes": None,
    },
    {
        "id": "hij-09-e1-04",
        "section_id": "Hij_09",
        "drill": 1,
        "number": 4,
        "role": "example",
        "english": "Realizing that he had a talent for languages, he decided to train as an interpreter.",
        "japanese": "彼は言語の才能があると悟ったので、通訳の訓練をすることにした。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_09 -- ポイント16 例文 (2問)
    # ----------------------------------------------------------
    {
        "id": "hij-09-e1-05",
        "section_id": "Hij_09",
        "drill": 1,
        "number": 5,
        "role": "example",
        "english": "My hobby is writing a novel.",
        "japanese": "私の趣味は、小説を書くことです。",
        "notes": "ポイント16 例文1",
    },
    {
        "id": "hij-09-e1-06",
        "section_id": "Hij_09",
        "drill": 1,
        "number": 6,
        "role": "example",
        "english": "She is writing a novel.",
        "japanese": "彼女は、小説を書いている最中だ。",
        "notes": "ポイント16 例文2",
    },
    # ----------------------------------------------------------
    # Hij_09 -- ポイント17 例文 (2問)
    # ----------------------------------------------------------
    {
        "id": "hij-09-e1-07",
        "section_id": "Hij_09",
        "drill": 1,
        "number": 7,
        "role": "example",
        "english": "Maintaining the web page is one of the most important parts of her job.",
        "japanese": "そのホームページをメンテナンスすることは、彼女の仕事の最も重要な一部だ。",
        "notes": "ポイント17 例文1",
    },
    {
        "id": "hij-09-e1-08",
        "section_id": "Hij_09",
        "drill": 1,
        "number": 8,
        "role": "example",
        "english": "Living here for many years, I know many sightseeing spots.",
        "japanese": "何年もここに住んでいるので、私は多くの観光スポットを知っている。",
        "notes": "ポイント17 例文2",
    },
    # ----------------------------------------------------------
    # Hij_09 -- 確認問題 (4問)
    # ----------------------------------------------------------
    {
        "id": "hij-09-c1-01",
        "section_id": "Hij_09",
        "drill": 2,
        "number": 1,
        "role": "practice",
        "english": "Tempura is a word coming from Portuguese.",
        "japanese": "天ぷらはポルトガル語に由来する言葉だ。",
        "notes": None,
    },
    {
        "id": "hij-09-c1-02",
        "section_id": "Hij_09",
        "drill": 2,
        "number": 2,
        "role": "practice",
        "english": "Playing video games is fun.",
        "japanese": "テレビゲームをすることは楽しい。",
        "notes": None,
    },
    {
        "id": "hij-09-c1-03",
        "section_id": "Hij_09",
        "drill": 2,
        "number": 3,
        "role": "practice",
        "english": "He studied hard, becoming a lawyer.",
        "japanese": "彼は一生懸命勉強して、そして弁護士になった。",
        "notes": None,
    },
    {
        "id": "hij-09-c1-04",
        "section_id": "Hij_09",
        "drill": 2,
        "number": 4,
        "role": "practice",
        "english": "My wallet was stolen when I was shopping yesterday.",
        "japanese": "私が昨日買い物をしている間に、私の財布が盗まれた。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_09 -- 発展問題 (1問)
    # ----------------------------------------------------------
    {
        "id": "hij-09-a1-01",
        "section_id": "Hij_09",
        "drill": 3,
        "number": 1,
        "role": "advanced",
        "english": "There are significant differences between learning and teaching existing mathematics and creating new mathematics.",
        "japanese": "既存の数学を学び教えることと新しい数学をつくることには重大な違いがある。",
        "notes": "京都大",
    },
    # ==========================================================
    # Hij_10 -- Theme 10 過去分詞の識別で英文が読める
    # ==========================================================
    # ----------------------------------------------------------
    # Hij_10 -- 例題 (4問)
    # ----------------------------------------------------------
    {
        "id": "hij-10-e1-01",
        "section_id": "Hij_10",
        "drill": 1,
        "number": 1,
        "role": "example",
        "english": "Nothing will be gained by just waiting.",
        "japanese": "待っているだけでは、何も手に入らないだろう。",
        "notes": None,
    },
    {
        "id": "hij-10-e1-02",
        "section_id": "Hij_10",
        "drill": 1,
        "number": 2,
        "role": "example",
        "english": "I have lived here for more than 10 years.",
        "japanese": "私は10年以上の間、ここに住んでいる。",
        "notes": None,
    },
    {
        "id": "hij-10-e1-03",
        "section_id": "Hij_10",
        "drill": 1,
        "number": 3,
        "role": "example",
        "english": "I received a letter written in English.",
        "japanese": "私は英語で書かれた手紙を受け取った。",
        "notes": None,
    },
    {
        "id": "hij-10-e1-04",
        "section_id": "Hij_10",
        "drill": 1,
        "number": 4,
        "role": "example",
        "english": "Compared with that company, our company gives longer holidays.",
        "japanese": "その会社と比べると、私たちの会社はより長い休日をくれる。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_10 -- 確認問題 (4問)
    # ----------------------------------------------------------
    {
        "id": "hij-10-c1-01",
        "section_id": "Hij_10",
        "drill": 2,
        "number": 1,
        "role": "practice",
        "english": "The languages spoken in Canada are English and French.",
        "japanese": "カナダで話されている言語は、英語とフランス語です。",
        "notes": None,
    },
    {
        "id": "hij-10-c1-02",
        "section_id": "Hij_10",
        "drill": 2,
        "number": 2,
        "role": "practice",
        "english": "No foreign language can be mastered without effort.",
        "japanese": "どんな外国語も努力なしでは習得できない。",
        "notes": None,
    },
    {
        "id": "hij-10-c1-03",
        "section_id": "Hij_10",
        "drill": 2,
        "number": 3,
        "role": "practice",
        "english": "Next Sunday Ichiro will have stayed in Kobe for three years.",
        "japanese": "来週の日曜日でイチロウは、3年間神戸に滞在していることになるだろう。",
        "notes": None,
    },
    {
        "id": "hij-10-c1-04",
        "section_id": "Hij_10",
        "drill": 2,
        "number": 4,
        "role": "practice",
        "english": "Written in easy Japanese, this textbook is good for school children.",
        "japanese": "やさしい日本語で書かれているので、この教科書は学童にもよい。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_10 -- 発展問題 (1問)
    # ----------------------------------------------------------
    {
        "id": "hij-10-a1-01",
        "section_id": "Hij_10",
        "drill": 3,
        "number": 1,
        "role": "advanced",
        "english": "Although the responses to it may differ, concern about the changes brought on by technology continues.",
        "japanese": "科学技術への反応はさまざまかもしれないが、科学技術によってもたらされる変化に関する懸念は続いている。",
        "notes": "香川大",
    },
]

# ============================================================
# 10. SENTENCE_STRUCTURES
# ============================================================

SENTENCE_STRUCTURES = [
    # ==========================================================
    # Hij_08 -- Theme 08
    # ==========================================================
    # --- hij-08-e1-01 ---
    {"sentence_id": "hij-08-e1-01", "label": "overall", "value": "S V C"},
    {"sentence_id": "hij-08-e1-01", "label": "details", "value": "<To know the temperature of the Earth>(S:名詞句) is(V) important(C)"},
    # --- hij-08-e1-02 ---
    {"sentence_id": "hij-08-e1-02", "label": "overall", "value": "S V O"},
    {"sentence_id": "hij-08-e1-02", "label": "details", "value": "I(S) would like(V) <to take advantage of the opportunity {to visit the museum}>(O:名詞句)"},
    # --- hij-08-e1-03 ---
    {"sentence_id": "hij-08-e1-03", "label": "overall", "value": "M S M V M M"},
    {"sentence_id": "hij-08-e1-03", "label": "details", "value": "[In summer](M) we(S) usually(M) go(V) [to the pool](M) [to swim](M:副詞的用法)"},
    # --- hij-08-e1-04 ---
    {"sentence_id": "hij-08-e1-04", "label": "overall", "value": "S V M"},
    {"sentence_id": "hij-08-e1-04", "label": "details", "value": "A new store(S) is to be built(V:be to不定詞=予定) [next year](M)"},
    # --- hij-08-e1-05 ---
    {"sentence_id": "hij-08-e1-05", "label": "overall", "value": "S V O"},
    {"sentence_id": "hij-08-e1-05", "label": "details", "value": "I(S) promise(V) <to write to you>(O:名詞的用法)"},
    # --- hij-08-e1-06 ---
    {"sentence_id": "hij-08-e1-06", "label": "overall", "value": "S V O"},
    {"sentence_id": "hij-08-e1-06", "label": "details", "value": "I(S) intend(V) <to finish the book in a day>(O:名詞的用法)"},
    # --- hij-08-e1-07 ---
    {"sentence_id": "hij-08-e1-07", "label": "overall", "value": "S V O M"},
    {"sentence_id": "hij-08-e1-07", "label": "details", "value": "You(S) must keep(V) learning(O) [if you are to succeed](M:be to不定詞=意志)"},
    # --- hij-08-e1-08 ---
    {"sentence_id": "hij-08-e1-08", "label": "overall", "value": "S V"},
    {"sentence_id": "hij-08-e1-08", "label": "details", "value": "The ring(S) was not to be found(V:be to不定詞=可能)"},
    # --- hij-08-c1-01 ---
    {"sentence_id": "hij-08-c1-01", "label": "overall", "value": "S {M} V C"},
    {"sentence_id": "hij-08-c1-01", "label": "details", "value": "The most effective way(S) {to develop self-esteem}(形容詞的用法) is(V) <to have faith in yourself>(C:名詞的用法)"},
    # --- hij-08-c1-02 ---
    {"sentence_id": "hij-08-c1-02", "label": "overall", "value": "S V O M"},
    {"sentence_id": "hij-08-c1-02", "label": "details", "value": "The President(S) is to visit(V:be to不定詞=予定) Japan(O) [next month](M)"},
    # --- hij-08-c1-03 ---
    {"sentence_id": "hij-08-c1-03", "label": "overall", "value": "S V M M"},
    {"sentence_id": "hij-08-c1-03", "label": "details", "value": "He(S) went(V) [to the store](M) [to buy a present for her](M:副詞的用法)"},
    # --- hij-08-c1-04 ---
    {"sentence_id": "hij-08-c1-04", "label": "overall", "value": "S V O {M}"},
    {"sentence_id": "hij-08-c1-04", "label": "details", "value": "Do you(S) have(V) anything(O) {to say about this opinion}(形容詞的用法)"},
    # --- hij-08-a1-01 ---
    {"sentence_id": "hij-08-a1-01", "label": "overall", "value": "M S M V C"},
    {"sentence_id": "hij-08-a1-01", "label": "details", "value": "[To keep this newly competitive labor market fair and open](M:副詞的用法) equality(S) (of educational opportunities)(M) is(V) necessary(C)"},
    # ==========================================================
    # Hij_09 -- Theme 09
    # ==========================================================
    # --- hij-09-e1-01 ---
    {"sentence_id": "hij-09-e1-01", "label": "overall", "value": "S V M"},
    {"sentence_id": "hij-09-e1-01", "label": "details", "value": "<Learning to read a language>(S:動名詞句) is best taught(V) [in the classroom](M)"},
    # --- hij-09-e1-02 ---
    {"sentence_id": "hij-09-e1-02", "label": "overall", "value": "S V M"},
    {"sentence_id": "hij-09-e1-02", "label": "details", "value": "The telephone(S) rang(V) [when I was taking a shower](M:副詞節)"},
    # --- hij-09-e1-03 ---
    {"sentence_id": "hij-09-e1-03", "label": "overall", "value": "S V O {M}"},
    {"sentence_id": "hij-09-e1-03", "label": "details", "value": "She(S) published(V) an article(O) {questioning the cause of the accident}(現在分詞の形容詞用法)"},
    # --- hij-09-e1-04 ---
    {"sentence_id": "hij-09-e1-04", "label": "overall", "value": "M S V O"},
    {"sentence_id": "hij-09-e1-04", "label": "details", "value": "[Realizing that he had a talent for languages](M:分詞構文=理由) he(S) decided(V) <to train as an interpreter>(O)"},
    # --- hij-09-e1-05 ---
    {"sentence_id": "hij-09-e1-05", "label": "overall", "value": "S V C"},
    {"sentence_id": "hij-09-e1-05", "label": "details", "value": "My hobby(S) is(V) <writing a novel>(C:動名詞)"},
    # --- hij-09-e1-06 ---
    {"sentence_id": "hij-09-e1-06", "label": "overall", "value": "S V O"},
    {"sentence_id": "hij-09-e1-06", "label": "details", "value": "She(S) is writing(V:進行形) a novel(O)"},
    # --- hij-09-e1-07 ---
    {"sentence_id": "hij-09-e1-07", "label": "overall", "value": "S V C"},
    {"sentence_id": "hij-09-e1-07", "label": "details", "value": "<Maintaining the web page>(S:動名詞句) is(V) one of the most important parts of her job(C)"},
    # --- hij-09-e1-08 ---
    {"sentence_id": "hij-09-e1-08", "label": "overall", "value": "M S V O"},
    {"sentence_id": "hij-09-e1-08", "label": "details", "value": "[Living here for many years](M:分詞構文=理由) I(S) know(V) many sightseeing spots(O)"},
    # --- hij-09-c1-01 ---
    {"sentence_id": "hij-09-c1-01", "label": "overall", "value": "S V C {M}"},
    {"sentence_id": "hij-09-c1-01", "label": "details", "value": "Tempura(S) is(V) a word(C) {coming from Portuguese}(現在分詞の形容詞用法)"},
    # --- hij-09-c1-02 ---
    {"sentence_id": "hij-09-c1-02", "label": "overall", "value": "S V C"},
    {"sentence_id": "hij-09-c1-02", "label": "details", "value": "<Playing video games>(S:動名詞句) is(V) fun(C)"},
    # --- hij-09-c1-03 ---
    {"sentence_id": "hij-09-c1-03", "label": "overall", "value": "S V M M"},
    {"sentence_id": "hij-09-c1-03", "label": "details", "value": "He(S) studied(V) hard(M) [becoming a lawyer](M:分詞構文=結果)"},
    # --- hij-09-c1-04 ---
    {"sentence_id": "hij-09-c1-04", "label": "overall", "value": "S V M"},
    {"sentence_id": "hij-09-c1-04", "label": "details", "value": "My wallet(S) was stolen(V:受動態) [when I was shopping yesterday](M:副詞節)"},
    # --- hij-09-a1-01 ---
    {"sentence_id": "hij-09-a1-01", "label": "overall", "value": "M V S M"},
    {"sentence_id": "hij-09-a1-01", "label": "details", "value": "There(M) are(V) significant differences(S) [between <learning and teaching existing mathematics> and <creating new mathematics>](M)"},
    # ==========================================================
    # Hij_10 -- Theme 10
    # ==========================================================
    # --- hij-10-e1-01 ---
    {"sentence_id": "hij-10-e1-01", "label": "overall", "value": "S V M"},
    {"sentence_id": "hij-10-e1-01", "label": "details", "value": "Nothing(S) will be gained(V:受動態) [by just waiting](M)"},
    # --- hij-10-e1-02 ---
    {"sentence_id": "hij-10-e1-02", "label": "overall", "value": "S V M M"},
    {"sentence_id": "hij-10-e1-02", "label": "details", "value": "I(S) have lived(V:現在完了) here(M) [for more than 10 years](M)"},
    # --- hij-10-e1-03 ---
    {"sentence_id": "hij-10-e1-03", "label": "overall", "value": "S V O {M}"},
    {"sentence_id": "hij-10-e1-03", "label": "details", "value": "I(S) received(V) a letter(O) {written in English}(過去分詞の名詞修飾)"},
    # --- hij-10-e1-04 ---
    {"sentence_id": "hij-10-e1-04", "label": "overall", "value": "M S V O"},
    {"sentence_id": "hij-10-e1-04", "label": "details", "value": "[Compared with that company](M:分詞構文) our company(S) gives(V) longer holidays(O)"},
    # --- hij-10-c1-01 ---
    {"sentence_id": "hij-10-c1-01", "label": "overall", "value": "S {M} V C"},
    {"sentence_id": "hij-10-c1-01", "label": "details", "value": "The languages(S) {spoken in Canada}(過去分詞の名詞修飾) are(V) English and French(C)"},
    # --- hij-10-c1-02 ---
    {"sentence_id": "hij-10-c1-02", "label": "overall", "value": "S V M"},
    {"sentence_id": "hij-10-c1-02", "label": "details", "value": "No foreign language(S) can be mastered(V:受動態) [without effort](M)"},
    # --- hij-10-c1-03 ---
    {"sentence_id": "hij-10-c1-03", "label": "overall", "value": "M S V M M"},
    {"sentence_id": "hij-10-c1-03", "label": "details", "value": "[Next Sunday](M) Ichiro(S) will have stayed(V:未来完了) [in Kobe](M) [for three years](M)"},
    # --- hij-10-c1-04 ---
    {"sentence_id": "hij-10-c1-04", "label": "overall", "value": "M S V C M"},
    {"sentence_id": "hij-10-c1-04", "label": "details", "value": "[Written in easy Japanese](M:分詞構文=理由) this textbook(S) is(V) good(C) [for school children](M)"},
    # --- hij-10-a1-01 ---
    {"sentence_id": "hij-10-a1-01", "label": "overall", "value": "M S {M} V"},
    {"sentence_id": "hij-10-a1-01", "label": "details", "value": "[Although the responses to it may differ](M:副詞節) concern(S) {about the changes brought on by technology}(過去分詞の名詞修飾) continues(V)"},
]

# ============================================================
# 11. SENTENCE_KNOWLEDGE_TAGS
# ============================================================

SENTENCE_KNOWLEDGE_TAGS = [
    # ==========================================================
    # Hij_08 -- Theme 08
    # ==========================================================
    # --- 例題 ---
    {"sentence_id": "hij-08-e1-01", "node_id": "hid-001"},  # 名詞的用法(S)
    {"sentence_id": "hij-08-e1-02", "node_id": "hid-001"},  # 名詞的用法(O)+形容詞的用法
    {"sentence_id": "hij-08-e1-03", "node_id": "hid-001"},  # 副詞的用法
    {"sentence_id": "hij-08-e1-04", "node_id": "hid-007"},  # be to不定詞=予定
    # --- ポイント14 例文 ---
    {"sentence_id": "hij-08-e1-05", "node_id": "hid-001"},  # 名詞的用法(O)
    {"sentence_id": "hij-08-e1-06", "node_id": "hid-001"},  # 名詞的用法(O)
    # --- ポイント15 例文 ---
    {"sentence_id": "hij-08-e1-07", "node_id": "hid-007"},  # be to不定詞=意志
    {"sentence_id": "hij-08-e1-08", "node_id": "hid-007"},  # be to不定詞=可能
    # --- 確認問題 ---
    {"sentence_id": "hij-08-c1-01", "node_id": "hid-001"},  # 形容詞的用法+名詞的用法
    {"sentence_id": "hij-08-c1-02", "node_id": "hid-007"},  # be to不定詞=予定
    {"sentence_id": "hij-08-c1-03", "node_id": "hid-001"},  # 副詞的用法
    {"sentence_id": "hij-08-c1-04", "node_id": "hid-001"},  # 形容詞的用法
    # --- 発展問題 ---
    {"sentence_id": "hij-08-a1-01", "node_id": "hid-001"},  # 副詞的用法
    # ==========================================================
    # Hij_09 -- Theme 09
    # ==========================================================
    # --- 例題 ---
    {"sentence_id": "hij-09-e1-01", "node_id": "hid-002"},  # 動名詞(S)
    {"sentence_id": "hij-09-e1-02", "node_id": "hid-002"},  # 進行形
    {"sentence_id": "hij-09-e1-03", "node_id": "hid-008"},  # 現在分詞の形容詞用法
    {"sentence_id": "hij-09-e1-04", "node_id": "hid-008"},  # 分詞構文=理由
    # --- ポイント16 例文 ---
    {"sentence_id": "hij-09-e1-05", "node_id": "hid-002"},  # 動名詞(SVC)
    {"sentence_id": "hij-09-e1-06", "node_id": "hid-002"},  # 進行形
    # --- ポイント17 例文 ---
    {"sentence_id": "hij-09-e1-07", "node_id": "hid-002"},  # 動名詞(文頭)
    {"sentence_id": "hij-09-e1-08", "node_id": "hid-008"},  # 分詞構文(文頭)=理由
    # --- 確認問題 ---
    {"sentence_id": "hij-09-c1-01", "node_id": "hid-008"},  # 現在分詞の形容詞用法
    {"sentence_id": "hij-09-c1-02", "node_id": "hid-002"},  # 動名詞(S)
    {"sentence_id": "hij-09-c1-03", "node_id": "hid-008"},  # 分詞構文(文尾)=結果
    {"sentence_id": "hij-09-c1-04", "node_id": "hid-002"},  # 進行形
    # --- 発展問題 ---
    {"sentence_id": "hij-09-a1-01", "node_id": "hid-002"},  # 動名詞
    # ==========================================================
    # Hij_10 -- Theme 10
    # ==========================================================
    # --- 例題 ---
    {"sentence_id": "hij-10-e1-01", "node_id": "hid-003"},  # 受動態
    {"sentence_id": "hij-10-e1-02", "node_id": "hid-003"},  # 完了形
    {"sentence_id": "hij-10-e1-03", "node_id": "hid-003"},  # 名詞修飾
    {"sentence_id": "hij-10-e1-04", "node_id": "hid-003"},  # 分詞構文
    # --- 確認問題 ---
    {"sentence_id": "hij-10-c1-01", "node_id": "hid-003"},  # 名詞修飾
    {"sentence_id": "hij-10-c1-02", "node_id": "hid-003"},  # 受動態
    {"sentence_id": "hij-10-c1-03", "node_id": "hid-003"},  # 完了形(未来完了)
    {"sentence_id": "hij-10-c1-04", "node_id": "hid-003"},  # 分詞構文
    # --- 発展問題 ---
    {"sentence_id": "hij-10-a1-01", "node_id": "hid-003"},  # 名詞修飾
]
