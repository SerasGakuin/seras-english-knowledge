"""第1章: 意味のカタマリ編 Theme 06-07（副詞句・副詞節）"""

# ============================================================
# 1. KNOWLEDGE_NODES
# ============================================================

KNOWLEDGE_NODES = [
    {
        "id": "hch-005",
        "name": "副詞句（前置詞句・時の副詞句・不定詞の副詞的用法）",
        "category": "意味のカタマリ",
        "priority": "P1",
        "notes": "副詞句の3パターン: (1)前置詞の副詞句 — 文頭・文尾で動詞を修飾、(2)時の副詞句 — 文頭・文尾で動詞を修飾、(3)不定詞の副詞的用法 — 動詞と目的・手段の関係。副詞句は2語以上からなる副詞のカタマリで、SVの前やうしろでVを修飾する。句のなかにSVは入らないことを根拠に範囲を確定する。",
    },
    {
        "id": "hch-012",
        "name": "副詞句（分詞構文）",
        "category": "意味のカタマリ",
        "priority": "P1",
        "notes": "分詞構文が文頭・文中・文尾で副詞句をつくり、動詞を修飾するパターン。文頭の分詞構文（-ing/p.p.〜, SV.）は時「〜して（すると）」か理由「〜なので」と訳す。文尾の分詞構文（SV〜, -ing.）は「そして〜」「〜しながら」と訳す。現在分詞(-ing)と過去分詞(p.p.)の両方が分詞構文をつくる。",
    },
    {
        "id": "hch-006",
        "name": "副詞節①（時・条件・譲歩の接続詞）",
        "category": "意味のカタマリ",
        "priority": "P1",
        "notes": "接続詞がつくるSVのある副詞のカタマリ。文頭・文尾でVを修飾する。譲歩の接続詞: although(though)「〜だけれども」/ while「〜だけれども」/ whether〜or not「〜だろうとそうでなかろうと」。条件の接続詞: if「もし〜なら」/ unless「〜しない限り」。理由の接続詞: because「〜だから」/ as「〜なので」/ since「〜なので」。時の接続詞: before/after「〜する前[あと]に」/ while「〜する間」/ since「〜して以来」/ until「〜まで」。「1つの節にSVは1つ」を根拠に副詞節の範囲を確定する。sinceは完了形とセットなら時「〜以来」、それ以外は理由「〜なので」。",
    },
    {
        "id": "hch-007",
        "name": "副詞節②（転用接続詞）",
        "category": "意味のカタマリ",
        "priority": "P1",
        "notes": "副詞・前置詞句・比較表現から転用された接続詞が副詞節をつくるパターン。(1)副詞から転用: every time「〜するたびに」/ once「一度〜すると」、(2)前置詞句から転用: by the time「〜するときまでには」/ in case「〜する場合に備えて」、(3)比較表現から転用: as soon as「〜するとすぐに」。いずれもSVの前・うしろで副詞節をつくり、動詞を修飾する。",
    },
]

# ============================================================
# 2. UNDERSTANDING_GOALS
# ============================================================

UNDERSTANDING_GOALS = [
    # hch-005
    {"node_id": "hch-005", "seq": 1, "goal": "前置詞が文頭・文尾で副詞句をつくり、動詞を修飾するパターンを認識できる"},
    {"node_id": "hch-005", "seq": 2, "goal": "時の副詞句（Last summer等）が文頭・文尾でVを修飾するパターンを認識できる"},
    {"node_id": "hch-005", "seq": 3, "goal": "不定詞の副詞的用法が動詞と目的・手段の関係にあることを説明できる"},
    {"node_id": "hch-005", "seq": 4, "goal": "「句のなかにSVは入らない」ことを根拠に副詞句の範囲を確定できる"},
    # hch-012
    {"node_id": "hch-012", "seq": 1, "goal": "分詞構文が副詞句をつくり、文頭・文中・文尾で動詞を修飾することを説明できる"},
    {"node_id": "hch-012", "seq": 2, "goal": "文頭の分詞構文（-ing/p.p.〜, SV.）を時「〜して（すると）」か理由「〜なので」と訳し分けられる"},
    {"node_id": "hch-012", "seq": 3, "goal": "文尾の分詞構文（SV〜, -ing.）を「そして〜」「〜しながら」と訳せる"},
    # hch-006
    {"node_id": "hch-006", "seq": 1, "goal": "接続詞が文頭で副詞節をつくり、カンマまでの範囲でVを修飾するパターンを認識できる"},
    {"node_id": "hch-006", "seq": 2, "goal": "接続詞が文尾で副詞節をつくり、Vを修飾するパターンを認識できる"},
    {"node_id": "hch-006", "seq": 3, "goal": "譲歩(although/while/whether)・条件(if/unless)・理由(because/as/since)・時(before/after/while/since/until)の接続詞を分類できる"},
    {"node_id": "hch-006", "seq": 4, "goal": "「1つの節にSVは1つ」を根拠に副詞節の範囲を確定できる"},
    {"node_id": "hch-006", "seq": 5, "goal": "sinceが完了形とセットなら時「〜以来」、それ以外なら理由「〜なので」と識別できる"},
    # hch-007
    {"node_id": "hch-007", "seq": 1, "goal": "every time / once が副詞から転用された接続詞として副詞節をつくることを理解している"},
    {"node_id": "hch-007", "seq": 2, "goal": "by the time / in case が前置詞句から転用された接続詞として副詞節をつくることを理解している"},
    {"node_id": "hch-007", "seq": 3, "goal": "as soon as が比較表現から転用された接続詞として副詞節をつくることを理解している"},
    {"node_id": "hch-007", "seq": 4, "goal": "転用接続詞を見たら副詞節の範囲を決定して意味のカタマリをつかめる"},
]

# ============================================================
# 3. CHECK_POINTS
# ============================================================

CHECK_POINTS = [
    # hch-005
    {"node_id": "hch-005", "seq": 1, "question": "副詞句の3パターン（前置詞句・時の副詞句・不定詞の副詞的用法）は何か？", "answer": "(1)前置詞の副詞句、(2)時の副詞句、(3)不定詞の副詞的用法。いずれもSVの前やうしろでVを修飾する。"},
    {"node_id": "hch-005", "seq": 2, "question": "不定詞の副詞的用法は動詞とどのような関係にあるか？", "answer": "目的と手段の関係。to不定詞が「〜するために」という目的を、修飾される動詞が手段を表す。"},
    {"node_id": "hch-005", "seq": 3, "question": "時の副詞句の例を2つ挙げよ。", "answer": "Last summer「昨年の夏」、Next month「来月」など、時を示す語句が文頭・文尾でVを修飾する。"},
    # hch-012
    {"node_id": "hch-012", "seq": 1, "question": "文頭の分詞構文（-ing/p.p. 〜, SV.）はどのように訳すか？", "answer": "時「〜して（すると）」か、理由「〜なので」と訳す。"},
    {"node_id": "hch-012", "seq": 2, "question": "文尾の分詞構文（SV〜, -ing.）はどのように訳すか？", "answer": "「そして〜」または「〜しながら」と訳す。"},
    {"node_id": "hch-012", "seq": 3, "question": "Seen from a distance, the hill looks like a man's face. のSeen from a distanceは何か？", "answer": "分詞構文。過去分詞で始まる文頭の分詞構文。「遠くから見ると」と訳す。"},
    # hch-006
    {"node_id": "hch-006", "seq": 1, "question": "副詞節と副詞句の違いは何か？", "answer": "副詞節は接続詞がつくるSVのある副詞のカタマリ、副詞句はSVのない副詞のカタマリ。"},
    {"node_id": "hch-006", "seq": 2, "question": "譲歩の接続詞を3つ挙げよ。", "answer": "although（though）、while、whether〜or not。"},
    {"node_id": "hch-006", "seq": 3, "question": "理由の接続詞を3つ挙げよ。", "answer": "because、as、since。"},
    {"node_id": "hch-006", "seq": 4, "question": "sinceには2つの意味があるが、時のsinceと理由のsinceをどう見分けるか？", "answer": "完了形とセットで使われるsinceは時のsince「〜以来」、それ以外は理由のsince「〜なので」。"},
    {"node_id": "hch-006", "seq": 5, "question": "条件の接続詞を2つ挙げよ。", "answer": "if「もし〜なら」、unless「〜しない限り」。"},
    # hch-007
    {"node_id": "hch-007", "seq": 1, "question": "every time, once, by the time, in case, as soon asの元の品詞・表現は何か？", "answer": "every time・onceは副詞、by the time・in caseは前置詞句、as soon asは比較表現から転用された接続詞。"},
    {"node_id": "hch-007", "seq": 2, "question": "by the time SV の意味は？", "answer": "「SがVするときまでには」。"},
    {"node_id": "hch-007", "seq": 3, "question": "in case SV の意味は？", "answer": "「SがVする場合に備えて」。"},
]

# ============================================================
# 4. NODE_PREREQUISITES
# ============================================================

NODE_PREREQUISITES = [
    {"node_id": "hch-005", "prerequisite_id": "hsv-000"},
    {"node_id": "hch-012", "prerequisite_id": "hsv-000"},
    {"node_id": "hch-006", "prerequisite_id": "hch-005"},
    {"node_id": "hch-007", "prerequisite_id": "hch-006"},
]

# ============================================================
# 5. KNOWLEDGE_REFERENCES
# ============================================================

KNOWLEDGE_REFERENCES = [
    {"node_id": "hch-005", "book": "肘井の読解のための英文法", "section_id": "Hij_06", "pages": "p.48-51"},
    {"node_id": "hch-012", "book": "肘井の読解のための英文法", "section_id": "Hij_06", "pages": "p.49-51"},
    {"node_id": "hch-006", "book": "肘井の読解のための英文法", "section_id": "Hij_07_1", "pages": "p.52-57"},
    {"node_id": "hch-007", "book": "肘井の読解のための英文法", "section_id": "Hij_07_2", "pages": "p.58-62"},
]

# ============================================================
# 6. SECTIONS
# ============================================================

SECTIONS = [
    {
        "id": "Hij_06",
        "book": "肘井の読解のための英文法",
        "title": "Theme 06 副詞句で英文が読める",
        "pages": "p.48-51",
        "type": "drill",
    },
    {
        "id": "Hij_07_1",
        "book": "肘井の読解のための英文法",
        "title": "Theme 07 副詞節で英文が読める①",
        "pages": "p.52-57",
        "type": "drill",
    },
    {
        "id": "Hij_07_2",
        "book": "肘井の読解のための英文法",
        "title": "Theme 07 副詞節で英文が読める②",
        "pages": "p.58-62",
        "type": "drill",
    },
]

# ============================================================
# 7. SECTION_PREREQUISITES
# ============================================================

SECTION_PREREQUISITES = [
    {"section_id": "Hij_06", "prerequisite_id": "Hij_05"},
    {"section_id": "Hij_07_1", "prerequisite_id": "Hij_06"},
    {"section_id": "Hij_07_2", "prerequisite_id": "Hij_07_1"},
]

# ============================================================
# 8. SECTION_KNOWLEDGE_NODES
# ============================================================

SECTION_KNOWLEDGE_NODES = [
    {"section_id": "Hij_06", "node_id": "hch-005", "seq": 1},
    {"section_id": "Hij_06", "node_id": "hch-012", "seq": 2},
    {"section_id": "Hij_07_1", "node_id": "hch-006", "seq": 1},
    {"section_id": "Hij_07_2", "node_id": "hch-007", "seq": 1},
]

# ============================================================
# 9. SENTENCES
# ============================================================

SENTENCES = [
    # ==========================================================
    # Hij_06 -- 例題 (5問)
    # ==========================================================
    {
        "id": "hij-06-e1-01",
        "section_id": "Hij_06",
        "drill": 1,
        "number": 1,
        "role": "example",
        "english": "Within the time you must find time to sleep.",
        "japanese": "その時間のなかで、あなたは眠る時間を見つけなければならない。",
        "notes": None,
    },
    {
        "id": "hij-06-e1-02",
        "section_id": "Hij_06",
        "drill": 1,
        "number": 2,
        "role": "example",
        "english": "Last summer my sister traveled around Japan.",
        "japanese": "昨年の夏、私の姉は日本中を旅した。",
        "notes": None,
    },
    {
        "id": "hij-06-e1-03",
        "section_id": "Hij_06",
        "drill": 1,
        "number": 3,
        "role": "example",
        "english": "I am going to take the bus to save money.",
        "japanese": "私はお金を節約するために、そのバスに乗る予定だ。",
        "notes": None,
    },
    {
        "id": "hij-06-e1-04",
        "section_id": "Hij_06",
        "drill": 1,
        "number": 4,
        "role": "example",
        "english": "Seen from a distance, the hill looks like a man's face.",
        "japanese": "遠くから見ると、その丘は人の顔のように見える。",
        "notes": None,
    },
    {
        "id": "hij-06-e1-05",
        "section_id": "Hij_06",
        "drill": 1,
        "number": 5,
        "role": "example",
        "english": "Several accidents happened, causing a lot of delays.",
        "japanese": "複数の事故が起きて、（そして）たくさんの遅れを引き起こした。",
        "notes": None,
    },
    # ==========================================================
    # Hij_06 -- 確認問題 (4問)
    # ==========================================================
    {
        "id": "hij-06-c1-01",
        "section_id": "Hij_06",
        "drill": 2,
        "number": 1,
        "role": "practice",
        "english": "Next month they will have been married for 20 years.",
        "japanese": "来月その2人は、結婚して20年になるだろう。",
        "notes": None,
    },
    {
        "id": "hij-06-c1-02",
        "section_id": "Hij_06",
        "drill": 2,
        "number": 2,
        "role": "practice",
        "english": "Thanks to the company we can do the job we know best.",
        "japanese": "その会社のおかげで、私たちは最もよく知っている仕事をすることができる。",
        "notes": None,
    },
    {
        "id": "hij-06-c1-03",
        "section_id": "Hij_06",
        "drill": 2,
        "number": 3,
        "role": "practice",
        "english": "I'll go to the store to buy some books.",
        "japanese": "私は数冊本を買うために、そのお店に行くつもりだ。",
        "notes": None,
    },
    {
        "id": "hij-06-c1-04",
        "section_id": "Hij_06",
        "drill": 2,
        "number": 4,
        "role": "practice",
        "english": "Persuaded by his friends, he decided to divorce her.",
        "japanese": "友人に説得されたので、彼は彼女と離婚することに決めた。",
        "notes": None,
    },
    # ==========================================================
    # Hij_06 -- 発展問題 (1問)
    # ==========================================================
    {
        "id": "hij-06-a1-01",
        "section_id": "Hij_06",
        "drill": 3,
        "number": 1,
        "role": "advanced",
        "english": "By its very nature much of medical practice is done without supervision.",
        "japanese": "まさにその性質上、医療の多くは監督なしで行われている。",
        "notes": "奈良県立医科大",
    },
    # ==========================================================
    # Hij_07_1 -- 例題 (4問) + ポイント例文 (5問) = 9文
    # ==========================================================
    {
        "id": "hij-07_1-e1-01",
        "section_id": "Hij_07_1",
        "drill": 1,
        "number": 1,
        "role": "example",
        "english": "While I like the color of the bag, I don't like its size.",
        "japanese": "私はそのバッグの色は好きだけれども、その大きさは好きではない。",
        "notes": None,
    },
    {
        "id": "hij-07_1-e1-02",
        "section_id": "Hij_07_1",
        "drill": 1,
        "number": 2,
        "role": "example",
        "english": "Unless you drive faster, you will be late for the concert.",
        "japanese": "あなたがもっと速く運転しない限り、コンサートに遅刻するだろう。",
        "notes": None,
    },
    {
        "id": "hij-07_1-e1-03",
        "section_id": "Hij_07_1",
        "drill": 1,
        "number": 3,
        "role": "example",
        "english": "He was absent because he caught a cold.",
        "japanese": "彼は風邪をひいたから、欠席していた。",
        "notes": None,
    },
    {
        "id": "hij-07_1-e1-04",
        "section_id": "Hij_07_1",
        "drill": 1,
        "number": 4,
        "role": "example",
        "english": "I'll be at home until you come back.",
        "japanese": "あなたがもどってくるまで、私は家にいるだろう。",
        "notes": None,
    },
    # ポイント10 例文（譲歩の接続詞）
    {
        "id": "hij-07_1-e1-05",
        "section_id": "Hij_07_1",
        "drill": 1,
        "number": 5,
        "role": "example",
        "english": "Although she can read English, she can't speak it.",
        "japanese": "彼女は英語を読めるけれども、話せない。",
        "notes": "ポイント10 例文",
    },
    # ポイント11 例文（条件の接続詞）
    {
        "id": "hij-07_1-e1-06",
        "section_id": "Hij_07_1",
        "drill": 1,
        "number": 6,
        "role": "example",
        "english": "If it rains tomorrow, the tennis match will be postponed.",
        "japanese": "明日雨が降るなら、そのテニスの試合は延期されるだろう。",
        "notes": "ポイント11 例文",
    },
    # ポイント12 例文1（理由の接続詞 as）
    {
        "id": "hij-07_1-e1-07",
        "section_id": "Hij_07_1",
        "drill": 1,
        "number": 7,
        "role": "example",
        "english": "As I had no money, I couldn't go there.",
        "japanese": "私にはお金がなかったので、そこに行けなかった。",
        "notes": "ポイント12 例文1",
    },
    # ポイント12 例文2（理由の接続詞 since）
    {
        "id": "hij-07_1-e1-08",
        "section_id": "Hij_07_1",
        "drill": 1,
        "number": 8,
        "role": "example",
        "english": "Since I am ill, I can't go there.",
        "japanese": "私は病気なので、そこには行けない。",
        "notes": "ポイント12 例文2",
    },
    # ポイント13 例文（時の接続詞 while）
    {
        "id": "hij-07_1-e1-09",
        "section_id": "Hij_07_1",
        "drill": 1,
        "number": 9,
        "role": "example",
        "english": "My mother visited me while I was not at home.",
        "japanese": "私が家にいない間に、母が私を訪ねてきた。",
        "notes": "ポイント13 例文",
    },
    # ==========================================================
    # Hij_07_1 -- 確認問題 (4問)
    # ==========================================================
    {
        "id": "hij-07_1-c1-01",
        "section_id": "Hij_07_1",
        "drill": 2,
        "number": 1,
        "role": "practice",
        "english": "We shouldn't keep dogs unless we can take care of them.",
        "japanese": "私たちは犬を世話できない限り、飼うべきではない。",
        "notes": None,
    },
    {
        "id": "hij-07_1-c1-02",
        "section_id": "Hij_07_1",
        "drill": 2,
        "number": 2,
        "role": "practice",
        "english": "She likes to tell jokes whether they are funny or not.",
        "japanese": "彼女は、おもしろかろうとそうでなかろうと、冗談を言うのが好きだ。",
        "notes": None,
    },
    {
        "id": "hij-07_1-c1-03",
        "section_id": "Hij_07_1",
        "drill": 2,
        "number": 3,
        "role": "practice",
        "english": "Many years have passed since I saw you last time.",
        "japanese": "最後にあなたに会って以来、多くの年数が経過した。",
        "notes": None,
    },
    {
        "id": "hij-07_1-c1-04",
        "section_id": "Hij_07_1",
        "drill": 2,
        "number": 4,
        "role": "practice",
        "english": "As she is a mother, she has to think of her children.",
        "japanese": "彼女は母親なので、子どもたちのことを考えなければならない。",
        "notes": None,
    },
    # ==========================================================
    # Hij_07_1 -- 発展問題 (1問)
    # ==========================================================
    {
        "id": "hij-07_1-a1-01",
        "section_id": "Hij_07_1",
        "drill": 3,
        "number": 1,
        "role": "advanced",
        "english": "The star's presence in a film is a promise of what you will see if you go to see the film.",
        "japanese": "映画におけるスターの存在は、映画を見に行く場合に目にするものを約束してくれるものだ。",
        "notes": "東京大",
    },
    # ==========================================================
    # Hij_07_2 -- 例題 (5問)
    # ==========================================================
    {
        "id": "hij-07_2-e1-01",
        "section_id": "Hij_07_2",
        "drill": 1,
        "number": 1,
        "role": "example",
        "english": "He complains every time I go to his house.",
        "japanese": "私が彼の家に行くたびに、彼は文句を言う。",
        "notes": None,
    },
    {
        "id": "hij-07_2-e1-02",
        "section_id": "Hij_07_2",
        "drill": 1,
        "number": 2,
        "role": "example",
        "english": "Once you begin, you must continue.",
        "japanese": "一度始めたら、続けなければならない。",
        "notes": None,
    },
    {
        "id": "hij-07_2-e1-03",
        "section_id": "Hij_07_2",
        "drill": 1,
        "number": 3,
        "role": "example",
        "english": "She had left there by the time I went back there.",
        "japanese": "私がそこにもどるまでには、彼女はそこを離れていた。",
        "notes": None,
    },
    {
        "id": "hij-07_2-e1-04",
        "section_id": "Hij_07_2",
        "drill": 1,
        "number": 4,
        "role": "example",
        "english": "You should take a map with you in case you get lost on the way.",
        "japanese": "あなたは途中で道に迷った場合に備えて、地図を持っていくべきだ。",
        "notes": None,
    },
    {
        "id": "hij-07_2-e1-05",
        "section_id": "Hij_07_2",
        "drill": 1,
        "number": 5,
        "role": "example",
        "english": "As soon as I arrived in the town, I visited her.",
        "japanese": "私はその町に着くとすぐに、彼女のもとを訪ねた。",
        "notes": None,
    },
    # ==========================================================
    # Hij_07_2 -- 確認問題 (5問)
    # ==========================================================
    {
        "id": "hij-07_2-c1-01",
        "section_id": "Hij_07_2",
        "drill": 2,
        "number": 1,
        "role": "practice",
        "english": "Once you get used to our system, you should have no problems.",
        "japanese": "一度あなたが私たちの制度に慣れると、問題ないはずだ。",
        "notes": None,
    },
    {
        "id": "hij-07_2-c1-02",
        "section_id": "Hij_07_2",
        "drill": 2,
        "number": 2,
        "role": "practice",
        "english": "He gets into trouble every time he opens his mouth.",
        "japanese": "彼は口を開くたびに、問題を起こす。",
        "notes": None,
    },
    {
        "id": "hij-07_2-c1-03",
        "section_id": "Hij_07_2",
        "drill": 2,
        "number": 3,
        "role": "practice",
        "english": "As soon as he arrives, you can leave.",
        "japanese": "彼が到着するとすぐに、あなたは出発してもよい。",
        "notes": None,
    },
    {
        "id": "hij-07_2-c1-04",
        "section_id": "Hij_07_2",
        "drill": 2,
        "number": 4,
        "role": "practice",
        "english": "I'll have finished this book by the time I see you again.",
        "japanese": "私があなたに再び会うときまでには、この本を読み終えているだろう。",
        "notes": None,
    },
    {
        "id": "hij-07_2-c1-05",
        "section_id": "Hij_07_2",
        "drill": 2,
        "number": 5,
        "role": "practice",
        "english": "In case you miss the meeting, you'll be fired.",
        "japanese": "あなたがその会議を欠席する場合には、解雇されるだろう。",
        "notes": None,
    },
    # ==========================================================
    # Hij_07_2 -- 発展問題 (1問)
    # ==========================================================
    {
        "id": "hij-07_2-a1-01",
        "section_id": "Hij_07_2",
        "drill": 3,
        "number": 1,
        "role": "advanced",
        "english": "Once I'd learned that skill, the first task was to begin imagining the vision of who I wanted to be.",
        "japanese": "一度私がその技術を身につけると、最初にやるべきことは、私がだれになりたいかというイメージを想像し始めることだった。",
        "notes": "岩手大",
    },
]

# ============================================================
# 10. SENTENCE_STRUCTURES
# ============================================================

SENTENCE_STRUCTURES = [
    # --- hij-06-e1-01 ---
    {"sentence_id": "hij-06-e1-01", "label": "overall", "value": "M S V O"},
    {"sentence_id": "hij-06-e1-01", "label": "details", "value": "[Within the time](M:前置詞の副詞句) you(S) must find(V) time to sleep(O)"},
    # --- hij-06-e1-02 ---
    {"sentence_id": "hij-06-e1-02", "label": "overall", "value": "M S V M"},
    {"sentence_id": "hij-06-e1-02", "label": "details", "value": "[Last summer](M:時の副詞句) my sister(S) traveled(V) [around Japan](M)"},
    # --- hij-06-e1-03 ---
    {"sentence_id": "hij-06-e1-03", "label": "overall", "value": "S V O M"},
    {"sentence_id": "hij-06-e1-03", "label": "details", "value": "I(S) am going to take(V) the bus(O) [to save money](M:不定詞の副詞的用法)"},
    # --- hij-06-e1-04 ---
    {"sentence_id": "hij-06-e1-04", "label": "overall", "value": "M S V M"},
    {"sentence_id": "hij-06-e1-04", "label": "details", "value": "[Seen from a distance](M:分詞構文) the hill(S) looks(V) [like a man's face](M)"},
    # --- hij-06-e1-05 ---
    {"sentence_id": "hij-06-e1-05", "label": "overall", "value": "S V M"},
    {"sentence_id": "hij-06-e1-05", "label": "details", "value": "Several accidents(S) happened(V), [causing a lot of delays](M:分詞構文)"},
    # --- hij-06-c1-01 ---
    {"sentence_id": "hij-06-c1-01", "label": "overall", "value": "M S V M"},
    {"sentence_id": "hij-06-c1-01", "label": "details", "value": "[Next month](M:時の副詞句) they(S) will have been married(V) [for 20 years](M)"},
    # --- hij-06-c1-02 ---
    {"sentence_id": "hij-06-c1-02", "label": "overall", "value": "M S V O M"},
    {"sentence_id": "hij-06-c1-02", "label": "details", "value": "[Thanks to the company](M:群前置詞の副詞句) we(S) can do(V) the job(O) (we know best)(M:関係代名詞省略)"},
    # --- hij-06-c1-03 ---
    {"sentence_id": "hij-06-c1-03", "label": "overall", "value": "S V M M"},
    {"sentence_id": "hij-06-c1-03", "label": "details", "value": "I(S)'ll go(V) [to the store](M) [to buy some books](M:不定詞の副詞的用法)"},
    # --- hij-06-c1-04 ---
    {"sentence_id": "hij-06-c1-04", "label": "overall", "value": "M S V O"},
    {"sentence_id": "hij-06-c1-04", "label": "details", "value": "[Persuaded by his friends](M:分詞構文) he(S) decided(V) <to divorce her>(O)"},
    # --- hij-06-a1-01 ---
    {"sentence_id": "hij-06-a1-01", "label": "overall", "value": "M S M V M"},
    {"sentence_id": "hij-06-a1-01", "label": "details", "value": "[By its very nature](M:前置詞の副詞句) much(S) (of medical practice)(M) is done(V) [without supervision](M)"},
    # --- hij-07_1-e1-01 ---
    {"sentence_id": "hij-07_1-e1-01", "label": "overall", "value": "M S V O"},
    {"sentence_id": "hij-07_1-e1-01", "label": "details", "value": "[While I like the color of the bag](M:副詞節/譲歩) I(S) don't like(V) its size(O)"},
    # --- hij-07_1-e1-02 ---
    {"sentence_id": "hij-07_1-e1-02", "label": "overall", "value": "M S V C M"},
    {"sentence_id": "hij-07_1-e1-02", "label": "details", "value": "[Unless you drive faster](M:副詞節/条件) you(S) will be(V) late(C) [for the concert](M)"},
    # --- hij-07_1-e1-03 ---
    {"sentence_id": "hij-07_1-e1-03", "label": "overall", "value": "S V C M"},
    {"sentence_id": "hij-07_1-e1-03", "label": "details", "value": "He(S) was(V) absent(C) [because he caught a cold](M:副詞節/理由)"},
    # --- hij-07_1-e1-04 ---
    {"sentence_id": "hij-07_1-e1-04", "label": "overall", "value": "S V M M"},
    {"sentence_id": "hij-07_1-e1-04", "label": "details", "value": "I(S)'ll be(V) [at home](M) [until you come back](M:副詞節/時)"},
    # --- hij-07_1-e1-05 (ポイント10) ---
    {"sentence_id": "hij-07_1-e1-05", "label": "overall", "value": "M S V O"},
    {"sentence_id": "hij-07_1-e1-05", "label": "details", "value": "[Although she can read English](M:副詞節/譲歩) she(S) can't speak(V) it(O)"},
    # --- hij-07_1-e1-06 (ポイント11) ---
    {"sentence_id": "hij-07_1-e1-06", "label": "overall", "value": "M S V"},
    {"sentence_id": "hij-07_1-e1-06", "label": "details", "value": "[If it rains tomorrow](M:副詞節/条件) the tennis match(S) will be postponed(V)"},
    # --- hij-07_1-e1-07 (ポイント12 例文1) ---
    {"sentence_id": "hij-07_1-e1-07", "label": "overall", "value": "M S V M"},
    {"sentence_id": "hij-07_1-e1-07", "label": "details", "value": "[As I had no money](M:副詞節/理由) I(S) couldn't go(V) there(M)"},
    # --- hij-07_1-e1-08 (ポイント12 例文2) ---
    {"sentence_id": "hij-07_1-e1-08", "label": "overall", "value": "M S V M"},
    {"sentence_id": "hij-07_1-e1-08", "label": "details", "value": "[Since I am ill](M:副詞節/理由) I(S) can't go(V) there(M)"},
    # --- hij-07_1-e1-09 (ポイント13) ---
    {"sentence_id": "hij-07_1-e1-09", "label": "overall", "value": "S V O M"},
    {"sentence_id": "hij-07_1-e1-09", "label": "details", "value": "My mother(S) visited(V) me(O) [while I was not at home](M:副詞節/時)"},
    # --- hij-07_1-c1-01 ---
    {"sentence_id": "hij-07_1-c1-01", "label": "overall", "value": "S V O M"},
    {"sentence_id": "hij-07_1-c1-01", "label": "details", "value": "We(S) shouldn't keep(V) dogs(O) [unless we can take care of them](M:副詞節/条件)"},
    # --- hij-07_1-c1-02 ---
    {"sentence_id": "hij-07_1-c1-02", "label": "overall", "value": "S V O M"},
    {"sentence_id": "hij-07_1-c1-02", "label": "details", "value": "She(S) likes(V) to tell jokes(O) [whether they are funny or not](M:副詞節/譲歩)"},
    # --- hij-07_1-c1-03 ---
    {"sentence_id": "hij-07_1-c1-03", "label": "overall", "value": "S V M"},
    {"sentence_id": "hij-07_1-c1-03", "label": "details", "value": "Many years(S) have passed(V) [since I saw you last time](M:副詞節/時)"},
    # --- hij-07_1-c1-04 ---
    {"sentence_id": "hij-07_1-c1-04", "label": "overall", "value": "M S V O"},
    {"sentence_id": "hij-07_1-c1-04", "label": "details", "value": "[As she is a mother](M:副詞節/理由) she(S) has to think of(V) her children(O)"},
    # --- hij-07_1-a1-01 ---
    {"sentence_id": "hij-07_1-a1-01", "label": "overall", "value": "S M V C M"},
    {"sentence_id": "hij-07_1-a1-01", "label": "details", "value": "The star's presence(S) (in a film)(M) is(V) a promise(C) (of <what you will see [if you go to see the film]>)(M)"},
    # --- hij-07_2-e1-01 ---
    {"sentence_id": "hij-07_2-e1-01", "label": "overall", "value": "S V M"},
    {"sentence_id": "hij-07_2-e1-01", "label": "details", "value": "He(S) complains(V) [every time I go to his house](M:副詞節/転用接続詞)"},
    # --- hij-07_2-e1-02 ---
    {"sentence_id": "hij-07_2-e1-02", "label": "overall", "value": "M S V"},
    {"sentence_id": "hij-07_2-e1-02", "label": "details", "value": "[Once you begin](M:副詞節/転用接続詞) you(S) must continue(V)"},
    # --- hij-07_2-e1-03 ---
    {"sentence_id": "hij-07_2-e1-03", "label": "overall", "value": "S V M M"},
    {"sentence_id": "hij-07_2-e1-03", "label": "details", "value": "She(S) had left(V) there(M) [by the time I went back there](M:副詞節/転用接続詞)"},
    # --- hij-07_2-e1-04 ---
    {"sentence_id": "hij-07_2-e1-04", "label": "overall", "value": "S V O M M"},
    {"sentence_id": "hij-07_2-e1-04", "label": "details", "value": "You(S) should take(V) a map(O) [with you](M) [in case you get lost on the way](M:副詞節/転用接続詞)"},
    # --- hij-07_2-e1-05 ---
    {"sentence_id": "hij-07_2-e1-05", "label": "overall", "value": "M S V O"},
    {"sentence_id": "hij-07_2-e1-05", "label": "details", "value": "[As soon as I arrived in the town](M:副詞節/転用接続詞) I(S) visited(V) her(O)"},
    # --- hij-07_2-c1-01 ---
    {"sentence_id": "hij-07_2-c1-01", "label": "overall", "value": "M S V O"},
    {"sentence_id": "hij-07_2-c1-01", "label": "details", "value": "[Once you get used to our system](M:副詞節/転用接続詞) you(S) should have(V) no problems(O)"},
    # --- hij-07_2-c1-02 ---
    {"sentence_id": "hij-07_2-c1-02", "label": "overall", "value": "S V M M"},
    {"sentence_id": "hij-07_2-c1-02", "label": "details", "value": "He(S) gets(V) [into trouble](M) [every time he opens his mouth](M:副詞節/転用接続詞)"},
    # --- hij-07_2-c1-03 ---
    {"sentence_id": "hij-07_2-c1-03", "label": "overall", "value": "M S V"},
    {"sentence_id": "hij-07_2-c1-03", "label": "details", "value": "[As soon as he arrives](M:副詞節/転用接続詞) you(S) can leave(V)"},
    # --- hij-07_2-c1-04 ---
    {"sentence_id": "hij-07_2-c1-04", "label": "overall", "value": "S V O M"},
    {"sentence_id": "hij-07_2-c1-04", "label": "details", "value": "I(S)'ll have finished(V) this book(O) [by the time I see you again](M:副詞節/転用接続詞)"},
    # --- hij-07_2-c1-05 ---
    {"sentence_id": "hij-07_2-c1-05", "label": "overall", "value": "M S V"},
    {"sentence_id": "hij-07_2-c1-05", "label": "details", "value": "[In case you miss the meeting](M:副詞節/転用接続詞) you(S)'ll be fired(V)"},
    # --- hij-07_2-a1-01 ---
    {"sentence_id": "hij-07_2-a1-01", "label": "overall", "value": "M S V C"},
    {"sentence_id": "hij-07_2-a1-01", "label": "details", "value": "[Once I'd learned that skill](M:副詞節/転用接続詞) the first task(S) was(V) <to begin imagining the vision of who I wanted to be>(C:不定詞の名詞的用法)"},
]

# ============================================================
# 11. SENTENCE_KNOWLEDGE_TAGS
# ============================================================

SENTENCE_KNOWLEDGE_TAGS = [
    # --- Hij_06 例題（前置詞句・時の副詞句・不定詞 → hch-005） ---
    {"sentence_id": "hij-06-e1-01", "node_id": "hch-005"},
    {"sentence_id": "hij-06-e1-02", "node_id": "hch-005"},
    {"sentence_id": "hij-06-e1-03", "node_id": "hch-005"},
    # --- Hij_06 例題（分詞構文 → hch-012） ---
    {"sentence_id": "hij-06-e1-04", "node_id": "hch-012"},
    {"sentence_id": "hij-06-e1-05", "node_id": "hch-012"},
    # --- Hij_06 確認問題 ---
    {"sentence_id": "hij-06-c1-01", "node_id": "hch-005"},
    {"sentence_id": "hij-06-c1-02", "node_id": "hch-005"},
    {"sentence_id": "hij-06-c1-03", "node_id": "hch-005"},
    {"sentence_id": "hij-06-c1-04", "node_id": "hch-012"},
    # --- Hij_06 発展問題 ---
    {"sentence_id": "hij-06-a1-01", "node_id": "hch-005"},
    # --- Hij_07_1 例題 ---
    {"sentence_id": "hij-07_1-e1-01", "node_id": "hch-006"},
    {"sentence_id": "hij-07_1-e1-02", "node_id": "hch-006"},
    {"sentence_id": "hij-07_1-e1-03", "node_id": "hch-006"},
    {"sentence_id": "hij-07_1-e1-04", "node_id": "hch-006"},
    {"sentence_id": "hij-07_1-e1-05", "node_id": "hch-006"},
    {"sentence_id": "hij-07_1-e1-06", "node_id": "hch-006"},
    {"sentence_id": "hij-07_1-e1-07", "node_id": "hch-006"},
    {"sentence_id": "hij-07_1-e1-08", "node_id": "hch-006"},
    {"sentence_id": "hij-07_1-e1-09", "node_id": "hch-006"},
    # --- Hij_07_1 確認問題 ---
    {"sentence_id": "hij-07_1-c1-01", "node_id": "hch-006"},
    {"sentence_id": "hij-07_1-c1-02", "node_id": "hch-006"},
    {"sentence_id": "hij-07_1-c1-03", "node_id": "hch-006"},
    {"sentence_id": "hij-07_1-c1-04", "node_id": "hch-006"},
    # --- Hij_07_1 発展問題 ---
    {"sentence_id": "hij-07_1-a1-01", "node_id": "hch-006"},
    # --- Hij_07_2 例題 ---
    {"sentence_id": "hij-07_2-e1-01", "node_id": "hch-007"},
    {"sentence_id": "hij-07_2-e1-02", "node_id": "hch-007"},
    {"sentence_id": "hij-07_2-e1-03", "node_id": "hch-007"},
    {"sentence_id": "hij-07_2-e1-04", "node_id": "hch-007"},
    {"sentence_id": "hij-07_2-e1-05", "node_id": "hch-007"},
    # --- Hij_07_2 確認問題 ---
    {"sentence_id": "hij-07_2-c1-01", "node_id": "hch-007"},
    {"sentence_id": "hij-07_2-c1-02", "node_id": "hch-007"},
    {"sentence_id": "hij-07_2-c1-03", "node_id": "hch-007"},
    {"sentence_id": "hij-07_2-c1-04", "node_id": "hch-007"},
    {"sentence_id": "hij-07_2-c1-05", "node_id": "hch-007"},
    # --- Hij_07_2 発展問題 ---
    {"sentence_id": "hij-07_2-a1-01", "node_id": "hch-007"},
]
