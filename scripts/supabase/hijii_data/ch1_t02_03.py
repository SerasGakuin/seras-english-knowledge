"""第1章: 意味のカタマリ編 Theme 02-03（名詞句・名詞節）"""

# ============================================================
# 1. KNOWLEDGE_NODES
# ============================================================

KNOWLEDGE_NODES = [
    {
        "id": "hch-001",
        "name": "名詞句（動名詞・不定詞の名詞的用法）",
        "category": "意味のカタマリ",
        "priority": "P1",
        "notes": "動名詞(-ing)・不定詞の名詞的用法(to do)の2パターンで名詞句をつくり、文のS・O・Cになる。句のなかにSVが入らないことを根拠に名詞句の範囲を決定する。",
    },
    {
        "id": "hch-008",
        "name": "名詞句（疑問詞+to不定詞）",
        "category": "意味のカタマリ",
        "priority": "P1",
        "notes": "疑問詞+to不定詞（what to do / how to do / when to do / where to do / who to do / whether to do）が名詞句をつくり、文のS・O・Cになる。すべてにshould「〜すべき」のニュアンスがある。why to doの形は存在しない。",
    },
    {
        "id": "hch-002",
        "name": "名詞節（what/that/疑問詞の名詞節）",
        "category": "意味のカタマリ",
        "priority": "P1",
        "notes": "関係代名詞what「〜こと」・名詞節のthat「〜ということ」・疑問詞の名詞節「疑問詞+〜か」の3パターンで名詞節をつくり、文のS・O・Cになる。「1つの節にSVは1つ」を根拠に名詞節の範囲を決定する。名詞句との違いはSVがあること。",
    },
    {
        "id": "hch-009",
        "name": "名詞節（whether/ifの識別）",
        "category": "意味のカタマリ",
        "priority": "P1",
        "notes": "whether/ifが「〜かどうか」の名詞節をつくるパターン。whetherのカタマリがS・O・Cになっていれば名詞節「〜かどうか」、それ以外は副詞節「〜だろうとそうでなかろうと」。ifがOの位置に来ると名詞節「〜かどうか」、副詞節のifは「もし〜なら」。名詞節と副詞節の識別が独立したスキル。",
    },
]

# ============================================================
# 2. UNDERSTANDING_GOALS
# ============================================================

UNDERSTANDING_GOALS = [
    # hch-001
    {"node_id": "hch-001", "seq": 1, "goal": "動名詞が他の単語をともなって名詞句をつくり、文のS・O・Cになることを説明できる"},
    {"node_id": "hch-001", "seq": 2, "goal": "不定詞の名詞的用法(to+動詞の原形)が名詞句をつくり、文のS・O・Cになることを説明できる"},
    {"node_id": "hch-001", "seq": 3, "goal": "句のなかにSVが入らないことを根拠に名詞句の範囲を正確に決定できる"},
    # hch-008
    {"node_id": "hch-008", "seq": 1, "goal": "疑問詞+to不定詞が名詞句をつくり、すべてにshouldの意味があることを説明できる"},
    {"node_id": "hch-008", "seq": 2, "goal": "what/how/when/where/who/whetherの6種の疑問詞+to不定詞を列挙し、それぞれの意味を説明できる"},
    {"node_id": "hch-008", "seq": 3, "goal": "疑問詞+to不定詞の名詞句が文のS・O・Cのどれになるか判定できる"},
    # hch-002
    {"node_id": "hch-002", "seq": 1, "goal": "関係代名詞whatが名詞節「〜こと［もの］」をつくることを説明できる"},
    {"node_id": "hch-002", "seq": 2, "goal": "名詞節のthatが「〜ということ」という名詞節をつくることを説明できる"},
    {"node_id": "hch-002", "seq": 3, "goal": "疑問詞(how/when/where/who/which/what/why)が名詞節をつくることを説明できる"},
    {"node_id": "hch-002", "seq": 4, "goal": "「1つの節にSVは1つ」を根拠に名詞節の範囲を正確に決定できる"},
    # hch-009
    {"node_id": "hch-009", "seq": 1, "goal": "whether/ifが「〜かどうか」という名詞節をつくることを説明できる"},
    {"node_id": "hch-009", "seq": 2, "goal": "whetherのカタマリがS・O・Cなら名詞節、それ以外は副詞節と識別できる"},
    {"node_id": "hch-009", "seq": 3, "goal": "ifが名詞節「〜かどうか」か副詞節「もし〜なら」かを文脈で識別できる"},
]

# ============================================================
# 3. CHECK_POINTS
# ============================================================

CHECK_POINTS = [
    # hch-001
    {"node_id": "hch-001", "seq": 1, "question": "名詞句をつくる2つのパターンは何か？", "answer": "(1)動名詞（-ingで「〜すること」）、(2)不定詞の名詞的用法（to+動詞の原形で「〜すること」）。いずれも文のS・O・Cになる。"},
    {"node_id": "hch-001", "seq": 2, "question": "名詞句の範囲を決定する根拠は？", "answer": "句のなかにSVが入らないこと。SVが現れる手前までが名詞句の範囲。"},
    {"node_id": "hch-001", "seq": 3, "question": "My hobby is collecting stamps. のcollecting stampsは何か？", "answer": "動名詞collectingが名詞句をつくり、文のC（補語）。「切手を集めること」。"},
    # hch-008
    {"node_id": "hch-008", "seq": 1, "question": "疑問詞+to不定詞にはどんなニュアンスがあるか？", "answer": "すべてにshould「〜すべき」のニュアンスがある。what to do「何を〜すべきか」、how to do「どのように〜すべきか」等。"},
    {"node_id": "hch-008", "seq": 2, "question": "疑問詞+to不定詞の6種を列挙せよ。", "answer": "what to do, how to do, when to do, where to do, who to do, whether to do。why to doは存在しない。"},
    {"node_id": "hch-008", "seq": 3, "question": "What to read is less important than how to read it. のWhat to readの役割は？", "answer": "疑問詞+to不定詞の名詞句で、文のS。「何を読むべきか」。"},
    # hch-002
    {"node_id": "hch-002", "seq": 1, "question": "名詞節をつくる3つのパターン（what/that/疑問詞）は何か？", "answer": "(1)関係代名詞what「〜こと」、(2)名詞節のthat「〜ということ」、(3)疑問詞の名詞節「疑問詞+〜か」。"},
    {"node_id": "hch-002", "seq": 2, "question": "名詞句と名詞節の違いは？", "answer": "名詞句はSVの文構造がない名詞のカタマリ、名詞節はSVの文構造がある名詞のカタマリ。"},
    {"node_id": "hch-002", "seq": 3, "question": "名詞節の範囲を確定する根拠は？", "answer": "「1つの節にSVは1つ」なので、2個目の動詞の手前で名詞節の範囲が終わる。"},
    # hch-009
    {"node_id": "hch-009", "seq": 1, "question": "whetherが名詞節か副詞節かを識別する方法は？", "answer": "whetherのカタマリがS・O・Cになっていれば名詞節「〜かどうか」、それ以外は副詞節「〜だろうとそうでなかろうと」。"},
    {"node_id": "hch-009", "seq": 2, "question": "ifの名詞節と副詞節の違いは？", "answer": "ifがO（目的語）の位置に来ると名詞節「〜かどうか」、その他の位置では副詞節「もし〜なら」。"},
    {"node_id": "hch-009", "seq": 3, "question": "Whether he wrote this poem or not is a mystery. のwhetherは名詞節か副詞節か？", "answer": "Sの位置なので名詞節。「彼がこの詩を書いたかどうかは謎だ。」"},
]

# ============================================================
# 4. NODE_PREREQUISITES
# ============================================================

NODE_PREREQUISITES = [
    {"node_id": "hch-001", "prerequisite_id": "hsv-000"},
    {"node_id": "hch-008", "prerequisite_id": "hch-001"},
    {"node_id": "hch-002", "prerequisite_id": "hch-001"},
    {"node_id": "hch-009", "prerequisite_id": "hch-002"},
]

# ============================================================
# 5. KNOWLEDGE_REFERENCES
# ============================================================

KNOWLEDGE_REFERENCES = [
    {"node_id": "hch-001", "book": "肘井の読解のための英文法", "section_id": "Hij_02", "pages": "p.26-29"},
    {"node_id": "hch-008", "book": "肘井の読解のための英文法", "section_id": "Hij_02", "pages": "p.29-31"},
    {"node_id": "hch-002", "book": "肘井の読解のための英文法", "section_id": "Hij_03", "pages": "p.32-37"},
    {"node_id": "hch-009", "book": "肘井の読解のための英文法", "section_id": "Hij_03", "pages": "p.35-37"},
]

# ============================================================
# 6. SECTIONS
# ============================================================

SECTIONS = [
    {
        "id": "Hij_02",
        "book": "肘井の読解のための英文法",
        "title": "Theme 02 名詞句で英文が読める",
        "pages": "p.26-31",
        "type": "drill",
    },
    {
        "id": "Hij_03",
        "book": "肘井の読解のための英文法",
        "title": "Theme 03 名詞節で英文が読める",
        "pages": "p.32-37",
        "type": "drill",
    },
]

# ============================================================
# 7. SECTION_PREREQUISITES
# ============================================================

SECTION_PREREQUISITES = [
    {"section_id": "Hij_02", "prerequisite_id": "Hij_01_2"},
    {"section_id": "Hij_03", "prerequisite_id": "Hij_02"},
]

# ============================================================
# 8. SECTION_KNOWLEDGE_NODES
# ============================================================

SECTION_KNOWLEDGE_NODES = [
    {"section_id": "Hij_02", "node_id": "hch-001", "seq": 1},
    {"section_id": "Hij_02", "node_id": "hch-008", "seq": 2},
    {"section_id": "Hij_03", "node_id": "hch-002", "seq": 1},
    {"section_id": "Hij_03", "node_id": "hch-009", "seq": 2},
]

# ============================================================
# 9. SENTENCES
# ============================================================

SENTENCES = [
    # ==========================================================
    # Hij_02 — 例題 (6問) + ポイント例文 (1問) = 7文
    # ==========================================================
    {
        "id": "hij-02-e1-01",
        "section_id": "Hij_02",
        "drill": 1,
        "number": 1,
        "role": "example",
        "english": "Riding a bike is different from driving a car.",
        "japanese": "自転車に乗ることは、車を運転することとは違う。",
        "notes": None,
    },
    {
        "id": "hij-02-e1-02",
        "section_id": "Hij_02",
        "drill": 1,
        "number": 2,
        "role": "example",
        "english": "He enjoys taking care of small children.",
        "japanese": "彼は、幼い子どもの面倒を見て楽しむ。",
        "notes": None,
    },
    {
        "id": "hij-02-e1-03",
        "section_id": "Hij_02",
        "drill": 1,
        "number": 3,
        "role": "example",
        "english": "My hobby is collecting stamps.",
        "japanese": "私の趣味は、切手を集めることです。",
        "notes": None,
    },
    {
        "id": "hij-02-e1-04",
        "section_id": "Hij_02",
        "drill": 1,
        "number": 4,
        "role": "example",
        "english": "Americans like to be different from others.",
        "japanese": "アメリカ人は、他人と違うことを好む。",
        "notes": None,
    },
    {
        "id": "hij-02-e1-05",
        "section_id": "Hij_02",
        "drill": 1,
        "number": 5,
        "role": "example",
        "english": "In Japan to be different is to invite suspicion.",
        "japanese": "日本では、違っていることは疑いを招くことである。",
        "notes": None,
    },
    {
        "id": "hij-02-e1-06",
        "section_id": "Hij_02",
        "drill": 1,
        "number": 6,
        "role": "example",
        "english": "What to read is less important than how to read it.",
        "japanese": "何を読むべきかは、それをどのように読むべきかより重要ではない。",
        "notes": None,
    },
    # ポイント6 例文
    {
        "id": "hij-02-e1-07",
        "section_id": "Hij_02",
        "drill": 1,
        "number": 7,
        "role": "example",
        "english": "The question is when to meet him.",
        "japanese": "問題は、いつ彼と会うべきかだ。",
        "notes": "ポイント6 例文",
    },
    # ==========================================================
    # Hij_02 — 確認問題 (3問)
    # ==========================================================
    {
        "id": "hij-02-c1-01",
        "section_id": "Hij_02",
        "drill": 2,
        "number": 1,
        "role": "practice",
        "english": "Learning a foreign language is important for understanding cultural differences.",
        "japanese": "外国語を学習することは、文化的違いを理解するのに重要だ。",
        "notes": None,
    },
    {
        "id": "hij-02-c1-02",
        "section_id": "Hij_02",
        "drill": 2,
        "number": 2,
        "role": "practice",
        "english": "To keep early hours is good for the health.",
        "japanese": "早寝早起きをすることは、健康によい。",
        "notes": None,
    },
    {
        "id": "hij-02-c1-03",
        "section_id": "Hij_02",
        "drill": 2,
        "number": 3,
        "role": "practice",
        "english": "When to start the project should be discussed more seriously.",
        "japanese": "いつその計画を始めるべきかを、もっと真剣に話し合うべきだ。",
        "notes": None,
    },
    # ==========================================================
    # Hij_02 — 発展問題 (1問)
    # ==========================================================
    {
        "id": "hij-02-a1-01",
        "section_id": "Hij_02",
        "drill": 3,
        "number": 1,
        "role": "advanced",
        "english": "When making progress becomes difficult, taking a break allows the unconscious processes to operate.",
        "japanese": "前進するのが難しいとき、休憩をとることで、無意識の作用をはたらかせることができる。",
        "notes": "滋賀県立大",
    },
    # ==========================================================
    # Hij_03 — 例題 (5問) + ポイント例文 (3問) = 8文
    # ==========================================================
    {
        "id": "hij-03-e1-01",
        "section_id": "Hij_03",
        "drill": 1,
        "number": 1,
        "role": "example",
        "english": "No student could understand what the teacher meant.",
        "japanese": "どの生徒も、その先生が意図したことが理解できなかった。",
        "notes": None,
    },
    {
        "id": "hij-03-e1-02",
        "section_id": "Hij_03",
        "drill": 1,
        "number": 2,
        "role": "example",
        "english": "What I don't understand is that he refused my offer.",
        "japanese": "私がわからないことは、彼が私の申し出を断ったということだ。",
        "notes": None,
    },
    {
        "id": "hij-03-e1-03",
        "section_id": "Hij_03",
        "drill": 1,
        "number": 3,
        "role": "example",
        "english": "I don't know how he opened the window.",
        "japanese": "私は、彼がどのようにその窓を開けたのかわからない。",
        "notes": None,
    },
    {
        "id": "hij-03-e1-04",
        "section_id": "Hij_03",
        "drill": 1,
        "number": 4,
        "role": "example",
        "english": "Whether he wrote this poem or not is a mystery.",
        "japanese": "彼がこの詩を書いたかどうかは謎だ。",
        "notes": None,
    },
    {
        "id": "hij-03-e1-05",
        "section_id": "Hij_03",
        "drill": 1,
        "number": 5,
        "role": "example",
        "english": "My friend asked me if he could borrow the book.",
        "japanese": "私の友人が、私にその本を借りられるかどうかを尋ねた。",
        "notes": None,
    },
    # ポイント7 例文
    {
        "id": "hij-03-e1-06",
        "section_id": "Hij_03",
        "drill": 1,
        "number": 6,
        "role": "example",
        "english": "Do you know why he lost his job?",
        "japanese": "あなたは、なぜ彼が仕事を失ったか知っていますか。",
        "notes": "ポイント7 例文",
    },
    # ポイント8 例文1
    {
        "id": "hij-03-e1-07",
        "section_id": "Hij_03",
        "drill": 1,
        "number": 7,
        "role": "example",
        "english": "The question is whether he will support you.",
        "japanese": "問題は、彼があなたを支えてくれるかどうかだ。",
        "notes": "ポイント8 例文1（whetherの名詞節）",
    },
    # ポイント8 例文2
    {
        "id": "hij-03-e1-08",
        "section_id": "Hij_03",
        "drill": 1,
        "number": 8,
        "role": "example",
        "english": "Whether we win or not, we will never forget you.",
        "japanese": "私たちが勝とうとそうでなかろうと、あなたのことを決して忘れない。",
        "notes": "ポイント8 例文2（whetherの副詞節）",
    },
    # ==========================================================
    # Hij_03 — 確認問題 (3問)
    # ==========================================================
    {
        "id": "hij-03-c1-01",
        "section_id": "Hij_03",
        "drill": 2,
        "number": 1,
        "role": "practice",
        "english": "What matters is whether you do your best or not.",
        "japanese": "重要なことは、最善をつくすかどうかだ。",
        "notes": None,
    },
    {
        "id": "hij-03-c1-02",
        "section_id": "Hij_03",
        "drill": 2,
        "number": 2,
        "role": "practice",
        "english": "New information shows us that what many people think is correct.",
        "japanese": "新しい情報が、私たちに多くの人が考えていることが正しいと示している。",
        "notes": None,
    },
    {
        "id": "hij-03-c1-03",
        "section_id": "Hij_03",
        "drill": 2,
        "number": 3,
        "role": "practice",
        "english": "I think that it is difficult to judge if she really meant what she said.",
        "japanese": "私は彼女が本気で言ったのかどうかを判断することは難しいと思う。",
        "notes": None,
    },
    # ==========================================================
    # Hij_03 — 発展問題 (1問)
    # ==========================================================
    {
        "id": "hij-03-a1-01",
        "section_id": "Hij_03",
        "drill": 3,
        "number": 1,
        "role": "advanced",
        "english": "Computers do what they are told to do, whether we meant it or not.",
        "japanese": "コンピュータは、私たちが本気で意図していようといまいと、やるように言われたことをやる。",
        "notes": "東京大",
    },
]

# ============================================================
# 10. SENTENCE_STRUCTURES
# ============================================================

SENTENCE_STRUCTURES = [
    # --- hij-02-e1-01 ---
    {"sentence_id": "hij-02-e1-01", "label": "overall", "value": "S V C M"},
    {"sentence_id": "hij-02-e1-01", "label": "details", "value": "<Riding a bike>(S:名詞句) is(V) different(C) [from driving a car](M)"},
    # --- hij-02-e1-02 ---
    {"sentence_id": "hij-02-e1-02", "label": "overall", "value": "S V O"},
    {"sentence_id": "hij-02-e1-02", "label": "details", "value": "He(S) enjoys(V) <taking care of small children>(O:名詞句)"},
    # --- hij-02-e1-03 ---
    {"sentence_id": "hij-02-e1-03", "label": "overall", "value": "S V C"},
    {"sentence_id": "hij-02-e1-03", "label": "details", "value": "My hobby(S) is(V) <collecting stamps>(C:名詞句)"},
    # --- hij-02-e1-04 ---
    {"sentence_id": "hij-02-e1-04", "label": "overall", "value": "S V O"},
    {"sentence_id": "hij-02-e1-04", "label": "details", "value": "Americans(S) like(V) <to be different from others>(O:名詞句)"},
    # --- hij-02-e1-05 ---
    {"sentence_id": "hij-02-e1-05", "label": "overall", "value": "M S V C"},
    {"sentence_id": "hij-02-e1-05", "label": "details", "value": "[In Japan](M) <to be different>(S:名詞句) is(V) <to invite suspicion>(C:名詞句)"},
    # --- hij-02-e1-06 ---
    {"sentence_id": "hij-02-e1-06", "label": "overall", "value": "S V C M"},
    {"sentence_id": "hij-02-e1-06", "label": "details", "value": "<What to read>(S:名詞句) is(V) less important(C) [than how to read it](M)"},
    # --- hij-02-e1-07 (ポイント6) ---
    {"sentence_id": "hij-02-e1-07", "label": "overall", "value": "S V C"},
    {"sentence_id": "hij-02-e1-07", "label": "details", "value": "The question(S) is(V) <when to meet him>(C:名詞句)"},
    # --- hij-02-c1-01 ---
    {"sentence_id": "hij-02-c1-01", "label": "overall", "value": "S V C M"},
    {"sentence_id": "hij-02-c1-01", "label": "details", "value": "<Learning a foreign language>(S:名詞句) is(V) important(C) [for understanding cultural differences](M)"},
    # --- hij-02-c1-02 ---
    {"sentence_id": "hij-02-c1-02", "label": "overall", "value": "S V C M"},
    {"sentence_id": "hij-02-c1-02", "label": "details", "value": "<To keep early hours>(S:名詞句) is(V) good(C) [for the health](M)"},
    # --- hij-02-c1-03 ---
    {"sentence_id": "hij-02-c1-03", "label": "overall", "value": "S V M"},
    {"sentence_id": "hij-02-c1-03", "label": "details", "value": "<When to start the project>(S:名詞句) should be discussed(V) [more seriously](M)"},
    # --- hij-02-a1-01 ---
    {"sentence_id": "hij-02-a1-01", "label": "overall", "value": "M S V O C"},
    {"sentence_id": "hij-02-a1-01", "label": "details", "value": "[When making progress becomes difficult](M:副詞節) <taking a break>(S:名詞句) allows(V) the unconscious processes(O) to operate(C)"},
    # --- hij-03-e1-01 ---
    {"sentence_id": "hij-03-e1-01", "label": "overall", "value": "S V O"},
    {"sentence_id": "hij-03-e1-01", "label": "details", "value": "No student(S) could understand(V) <what the teacher meant>(O:名詞節)"},
    # --- hij-03-e1-02 ---
    {"sentence_id": "hij-03-e1-02", "label": "overall", "value": "S V C"},
    {"sentence_id": "hij-03-e1-02", "label": "details", "value": "<What I don't understand>(S:名詞節) is(V) <that he refused my offer>(C:名詞節)"},
    # --- hij-03-e1-03 ---
    {"sentence_id": "hij-03-e1-03", "label": "overall", "value": "S V O"},
    {"sentence_id": "hij-03-e1-03", "label": "details", "value": "I(S) don't know(V) <how he opened the window>(O:名詞節)"},
    # --- hij-03-e1-04 ---
    {"sentence_id": "hij-03-e1-04", "label": "overall", "value": "S V C"},
    {"sentence_id": "hij-03-e1-04", "label": "details", "value": "<Whether he wrote this poem or not>(S:名詞節) is(V) a mystery(C)"},
    # --- hij-03-e1-05 ---
    {"sentence_id": "hij-03-e1-05", "label": "overall", "value": "S V O1 O2"},
    {"sentence_id": "hij-03-e1-05", "label": "details", "value": "My friend(S) asked(V) me(O1) <if he could borrow the book>(O2:名詞節)"},
    # --- hij-03-e1-06 (ポイント7) ---
    {"sentence_id": "hij-03-e1-06", "label": "overall", "value": "S V O"},
    {"sentence_id": "hij-03-e1-06", "label": "details", "value": "Do you(S) know(V) <why he lost his job>(O:名詞節)?"},
    # --- hij-03-e1-07 (ポイント8 例文1) ---
    {"sentence_id": "hij-03-e1-07", "label": "overall", "value": "S V C"},
    {"sentence_id": "hij-03-e1-07", "label": "details", "value": "The question(S) is(V) <whether he will support you>(C:名詞節)"},
    # --- hij-03-e1-08 (ポイント8 例文2) ---
    {"sentence_id": "hij-03-e1-08", "label": "overall", "value": "M S V O"},
    {"sentence_id": "hij-03-e1-08", "label": "details", "value": "[Whether we win or not](M:副詞節) we(S) will never forget(V) you(O)"},
    # --- hij-03-c1-01 ---
    {"sentence_id": "hij-03-c1-01", "label": "overall", "value": "S V C"},
    {"sentence_id": "hij-03-c1-01", "label": "details", "value": "<What matters>(S:名詞節) is(V) <whether you do your best or not>(C:名詞節)"},
    # --- hij-03-c1-02 ---
    {"sentence_id": "hij-03-c1-02", "label": "overall", "value": "S V O1 O2"},
    {"sentence_id": "hij-03-c1-02", "label": "details", "value": "New information(S) shows(V) us(O1) <that <what many people think> is correct>(O2:名詞節)"},
    # --- hij-03-c1-03 ---
    {"sentence_id": "hij-03-c1-03", "label": "overall", "value": "S V O"},
    {"sentence_id": "hij-03-c1-03", "label": "details", "value": "I(S) think(V) <that it is difficult to judge <if she really meant <what she said>>>(O:名詞節)"},
    # --- hij-03-a1-01 ---
    {"sentence_id": "hij-03-a1-01", "label": "overall", "value": "S V O M"},
    {"sentence_id": "hij-03-a1-01", "label": "details", "value": "Computers(S) do(V) <what they are told to do>(O:名詞節) [whether we meant it or not](M:副詞節)"},
]

# ============================================================
# 11. SENTENCE_KNOWLEDGE_TAGS
# ============================================================

SENTENCE_KNOWLEDGE_TAGS = [
    # --- Hij_02 例題（動名詞・不定詞 → hch-001） ---
    {"sentence_id": "hij-02-e1-01", "node_id": "hch-001"},
    {"sentence_id": "hij-02-e1-02", "node_id": "hch-001"},
    {"sentence_id": "hij-02-e1-03", "node_id": "hch-001"},
    {"sentence_id": "hij-02-e1-04", "node_id": "hch-001"},
    {"sentence_id": "hij-02-e1-05", "node_id": "hch-001"},
    # --- Hij_02 例題（疑問詞+to不定詞 → hch-008） ---
    {"sentence_id": "hij-02-e1-06", "node_id": "hch-008"},
    {"sentence_id": "hij-02-e1-07", "node_id": "hch-008"},
    # --- Hij_02 確認問題 ---
    {"sentence_id": "hij-02-c1-01", "node_id": "hch-001"},
    {"sentence_id": "hij-02-c1-02", "node_id": "hch-001"},
    {"sentence_id": "hij-02-c1-03", "node_id": "hch-008"},
    # --- Hij_02 発展問題 ---
    {"sentence_id": "hij-02-a1-01", "node_id": "hch-001"},
    # --- Hij_03 例題（what/that/疑問詞 → hch-002） ---
    {"sentence_id": "hij-03-e1-01", "node_id": "hch-002"},
    {"sentence_id": "hij-03-e1-02", "node_id": "hch-002"},
    {"sentence_id": "hij-03-e1-03", "node_id": "hch-002"},
    # --- Hij_03 例題（whether/if → hch-009） ---
    {"sentence_id": "hij-03-e1-04", "node_id": "hch-009"},
    {"sentence_id": "hij-03-e1-05", "node_id": "hch-009"},
    # --- Hij_03 例題（疑問詞 → hch-002） ---
    {"sentence_id": "hij-03-e1-06", "node_id": "hch-002"},
    # --- Hij_03 ポイント8（whether → hch-009） ---
    {"sentence_id": "hij-03-e1-07", "node_id": "hch-009"},
    {"sentence_id": "hij-03-e1-08", "node_id": "hch-009"},
    # --- Hij_03 確認問題（複合タグ） ---
    {"sentence_id": "hij-03-c1-01", "node_id": "hch-002"},
    {"sentence_id": "hij-03-c1-01", "node_id": "hch-009"},
    {"sentence_id": "hij-03-c1-02", "node_id": "hch-002"},
    {"sentence_id": "hij-03-c1-03", "node_id": "hch-002"},
    {"sentence_id": "hij-03-c1-03", "node_id": "hch-009"},
    # --- Hij_03 発展問題（複合タグ） ---
    {"sentence_id": "hij-03-a1-01", "node_id": "hch-002"},
    {"sentence_id": "hij-03-a1-01", "node_id": "hch-009"},
]
