"""第3章: 構文編 Theme 14-17（接続詞・倒置・省略・強調構文）"""

# ============================================================
# 1. KNOWLEDGE_NODES
# ============================================================

KNOWLEDGE_NODES = [
    {
        "id": "hco-001",
        "name": "接続詞（等位接続詞の並列構造と3つの並列）",
        "category": "構文",
        "priority": "P1",
        "notes": "等位接続詞(and/but/or/nor)を見たら、うしろの形を確認し、前で同じ形を探して並列構造を把握する。3つ以上の並列は A, B(,) and[or] C の形で、最後の接続詞以外はカンマで代用する。andが何と何をつないでいるかの特定が読解の鍵。",
    },
    {
        "id": "hco-002",
        "name": "倒置（文型倒置・強制倒置）",
        "category": "構文",
        "priority": "P1",
        "notes": "倒置には大きく分けて文型倒置と強制倒置がある。文型倒置は第1文型(SVM)をMVS、第2文型(SVC)をCVSにしたもの。There be～構文もMVSの一種。強制倒置は否定の副詞(little/never/only等)が文頭に出てうしろが疑問文の語順になるもの。",
    },
    {
        "id": "hco-011",
        "name": "倒置（nor/soの倒置・仮定法if節の倒置）",
        "category": "構文",
        "priority": "P1",
        "notes": "nor/soのうしろが疑問文の語順になる倒置と、仮定法if節の倒置。否定文を受けてnor+疑問文の語順で「…もまた～ない」、肯定文を受けてso+疑問文の語順で「…もまた～だ」。仮定法のif節ではifを省略して疑問文の語順にする(Were I~/Had I~/Should you~)。As S1V1, so+倒置の比例表現もある。",
    },
    {
        "id": "hco-003",
        "name": "省略（SVの省略・比較の省略・thatの省略・代不定詞）",
        "category": "構文",
        "priority": "P1",
        "notes": "省略の4パターン。(1)SVの省略: 接続詞のうしろで主節と同じSとbe動詞が省略される(When young=When I was young)。(2)比較の省略: 2個目のas以下で前出の形容詞・副詞が省略される。(3)thatの省略: S1 V1 S2 V2の語順でV1とS2の間にthatが省略。(4)代不定詞: to 1語で不定詞句を代用する(told him not to=told him not to open the window)。",
    },
    {
        "id": "hco-004",
        "name": "強調構文（It is A that ～の識別と用法）",
        "category": "構文",
        "priority": "P1",
        "notes": "It is A that ～.の文は強調構文と形式主語に分かれる。Aに副詞・副詞節・前置詞句が入れば強調構文確定。Aに名詞が入りthat以下が不完全文(名詞が欠けている)なら強調構文、完全文なら形式主語。Aに形容詞が入れば形式主語。頻出表現: It is not until A that B「AしてはじめてBする」。",
    },
]

# ============================================================
# 2. UNDERSTANDING_GOALS
# ============================================================

UNDERSTANDING_GOALS = [
    # hco-001: 接続詞
    {"node_id": "hco-001", "seq": 1, "goal": "等位接続詞(and/but/or)を見たらうしろの形を確認し、前で同じ形を探して並列構造を特定できる"},
    {"node_id": "hco-001", "seq": 2, "goal": "3つ以上の並列が A, B(,) and[or] C の形になることを理解し、並列要素を正確に特定できる"},
    {"node_id": "hco-001", "seq": 3, "goal": "andが文中の複数の箇所に現れるとき、それぞれのandが何と何をつないでいるか識別できる"},
    {"node_id": "hco-001", "seq": 4, "goal": "that節・関係代名詞節・-ing形・前置詞句など、多様な形の並列構造を正確に把握できる"},
    # hco-002: 倒置（文型倒置・強制倒置）
    {"node_id": "hco-002", "seq": 1, "goal": "第1文型の倒置(MVS)をThere be～構文を含めて識別し、SVを正確に特定できる"},
    {"node_id": "hco-002", "seq": 2, "goal": "第2文型の倒置(CVS)を識別し、文頭の形容詞が補語であることを見抜ける"},
    {"node_id": "hco-002", "seq": 3, "goal": "否定の副詞(little/never/only等)が文頭に出たら強制倒置と判断し、疑問文の語順からSVを特定できる"},
    # hco-011: 倒置（nor/soの倒置・仮定法if節の倒置）
    {"node_id": "hco-011", "seq": 1, "goal": "nor/soのうしろが疑問文の語順になる倒置を識別できる"},
    {"node_id": "hco-011", "seq": 2, "goal": "仮定法if節の倒置(Were I~/Had I~/Should you~)を見抜き、ifが省略されていることを復元できる"},
    {"node_id": "hco-011", "seq": 3, "goal": "As S1V1, so+疑問文の語順 の比例のas＋so倒置を識別できる"},
    # hco-003: 省略
    {"node_id": "hco-003", "seq": 1, "goal": "接続詞のうしろで主節と同じS+be動詞が省略されていることを見抜ける"},
    {"node_id": "hco-003", "seq": 2, "goal": "比較表現(as~as/than)のうしろで前出の形容詞・副詞が省略されていることを補える"},
    {"node_id": "hco-003", "seq": 3, "goal": "S1 V1 S2 V2の語順からV1とS2の間に接続詞thatが省略されていることに気づける"},
    {"node_id": "hco-003", "seq": 4, "goal": "代不定詞(to 1語で不定詞句を代用)を識別し、省略された動詞句を復元できる"},
    # hco-004: 強調構文
    {"node_id": "hco-004", "seq": 1, "goal": "It is A that ～.の文でAに副詞・副詞節・前置詞句が入れば強調構文と判断できる"},
    {"node_id": "hco-004", "seq": 2, "goal": "Aに名詞が入る場合、that以下が不完全文なら強調構文、完全文なら形式主語と識別できる"},
    {"node_id": "hco-004", "seq": 3, "goal": "It is not until A that B「AしてはじめてBする」の強調構文を正確に訳せる"},
    {"node_id": "hco-004", "seq": 4, "goal": "強調構文からIt is ... that を取り除いて元の文に復元し、強調されている要素を特定できる"},
]

# ============================================================
# 3. CHECK_POINTS
# ============================================================

CHECK_POINTS = [
    # hco-001: 接続詞
    {"node_id": "hco-001", "seq": 1, "question": "等位接続詞(and/but/or)を見たとき、並列構造を把握する手順は？", "answer": "接続詞のうしろの形を確認し、前で同じ形を探す。"},
    {"node_id": "hco-001", "seq": 2, "question": "3つ以上の並列はどのような形でつなぐか？", "answer": "A, B(,) and[or] C の形。最後の接続詞以外はカンマで代用する。"},
    {"node_id": "hco-001", "seq": 3, "question": "She said that it was my mistake and that I must not do it again. のandは何をつないでいるか？", "answer": "She saidの目的語であるthat節同士をつないでいる。that it was my mistakeとthat I must not do it againの並列。"},
    # hco-002: 倒置（文型倒置・強制倒置）
    {"node_id": "hco-002", "seq": 1, "question": "文型倒置の2つの型は？", "answer": "第1文型の倒置MVS(例: There be～、場所の副詞+V+S)と、第2文型の倒置CVS(例: More important is the experience)。"},
    {"node_id": "hco-002", "seq": 2, "question": "強制倒置が起きる条件は？", "answer": "否定の副詞(little/never/only等)が文頭に出ると、うしろが疑問文の語順になる。"},
    {"node_id": "hco-002", "seq": 3, "question": "There was a low wall between our garden and the field. の文型は？", "answer": "第1文型の倒置(MVS)。There(M) was(V) a low wall(S)。Thereは副詞で、実際の主語はa low wallである。"},
    # hco-011: 倒置（nor/soの倒置・仮定法if節の倒置）
    {"node_id": "hco-011", "seq": 1, "question": "nor/soの倒置のルールは？", "answer": "否定文を受けてnorのうしろが疑問文の語順「…もまた～ない」。肯定文を受けてsoのうしろが疑問文の語順「…もまた～だ」。"},
    {"node_id": "hco-011", "seq": 2, "question": "仮定法if節の倒置の手順は？", "answer": "ifを省略し、うしろを疑問文の語順にする。Were I～(=If I were～)、Had I～(=If I had～)、Should you～(=If you should～)。"},
    {"node_id": "hco-011", "seq": 3, "question": "Were I in your position, I would not do that. のifを復元すると？", "answer": "If I were in your position, I would not do that. Were I~はIf I were~の仮定法倒置。"},
    # hco-003: 省略
    {"node_id": "hco-003", "seq": 1, "question": "接続詞のうしろのSVの省略が起きる条件は？", "answer": "主節と同じ主語で、動詞がbe動詞のとき。When young = When I was young。"},
    {"node_id": "hco-003", "seq": 2, "question": "比較の省略とはどのような省略か？", "answer": "比較のas~as.../than...のうしろで、前出の形容詞・副詞が省略される。as he used to be (energetic)のように比較の判断内容が省略される。"},
    {"node_id": "hco-003", "seq": 3, "question": "代不定詞とは何か？", "answer": "to 1語で不定詞句のカタマリを代用する用法。told him not to = told him not to open the windowのように、すでに出た動詞句をto 1語で代用する。"},
    # hco-004: 強調構文
    {"node_id": "hco-004", "seq": 1, "question": "It is A that ～.が強調構文になる条件は？", "answer": "Aに副詞・副詞節・前置詞句が入る場合は強調構文確定。Aに名詞が入る場合はthat以下が不完全文なら強調構文。"},
    {"node_id": "hco-004", "seq": 2, "question": "It is A that ～.が形式主語構文になる条件は？", "answer": "Aに形容詞が入る場合、またはAに名詞が入りthat以下が完全文の場合。"},
    {"node_id": "hco-004", "seq": 3, "question": "It is not until A that B の訳し方は？", "answer": "直訳「AまでBしない」、意訳「AしてはじめてBする」。"},
]

# ============================================================
# 4. NODE_PREREQUISITES
# ============================================================

NODE_PREREQUISITES = [
    {"node_id": "hco-001", "prerequisite_id": "hsv-000"},
    {"node_id": "hco-002", "prerequisite_id": "hco-001"},
    {"node_id": "hco-011", "prerequisite_id": "hco-002"},
    {"node_id": "hco-003", "prerequisite_id": "hco-002"},
    {"node_id": "hco-004", "prerequisite_id": "hid-004"},
]

# ============================================================
# 5. KNOWLEDGE_REFERENCES
# ============================================================

KNOWLEDGE_REFERENCES = [
    {"node_id": "hco-001", "book": "肘井の読解のための英文法", "section_id": "Hij_14", "pages": "p.106-109"},
    {"node_id": "hco-002", "book": "肘井の読解のための英文法", "section_id": "Hij_15_1", "pages": "p.110-113"},
    {"node_id": "hco-011", "book": "肘井の読解のための英文法", "section_id": "Hij_15_2", "pages": "p.114-117"},
    {"node_id": "hco-003", "book": "肘井の読解のための英文法", "section_id": "Hij_16", "pages": "p.118-121"},
    {"node_id": "hco-004", "book": "肘井の読解のための英文法", "section_id": "Hij_17", "pages": "p.122-125"},
]

# ============================================================
# 6. SECTIONS
# ============================================================

SECTIONS = [
    {
        "id": "Hij_14",
        "book": "肘井の読解のための英文法",
        "title": "Theme 14 接続詞で英文が読める",
        "pages": "p.106-109",
        "type": "drill",
    },
    {
        "id": "Hij_15_1",
        "book": "肘井の読解のための英文法",
        "title": "Theme 15 倒置で英文が読める①",
        "pages": "p.110-113",
        "type": "drill",
    },
    {
        "id": "Hij_15_2",
        "book": "肘井の読解のための英文法",
        "title": "Theme 15 倒置で英文が読める②",
        "pages": "p.114-117",
        "type": "drill",
    },
    {
        "id": "Hij_16",
        "book": "肘井の読解のための英文法",
        "title": "Theme 16 省略で英文が読める",
        "pages": "p.118-121",
        "type": "drill",
    },
    {
        "id": "Hij_17",
        "book": "肘井の読解のための英文法",
        "title": "Theme 17 強調構文で英文が読める",
        "pages": "p.122-125",
        "type": "drill",
    },
]

# ============================================================
# 7. SECTION_PREREQUISITES
# ============================================================

SECTION_PREREQUISITES = [
    {"section_id": "Hij_14", "prerequisite_id": "Hij_13"},
    {"section_id": "Hij_15_1", "prerequisite_id": "Hij_14"},
    {"section_id": "Hij_15_2", "prerequisite_id": "Hij_15_1"},
    {"section_id": "Hij_16", "prerequisite_id": "Hij_15_2"},
    {"section_id": "Hij_17", "prerequisite_id": "Hij_16"},
]

# ============================================================
# 8. SECTION_KNOWLEDGE_NODES
# ============================================================

SECTION_KNOWLEDGE_NODES = [
    {"section_id": "Hij_14", "node_id": "hco-001", "seq": 1},
    {"section_id": "Hij_15_1", "node_id": "hco-002", "seq": 1},
    {"section_id": "Hij_15_2", "node_id": "hco-011", "seq": 1},
    {"section_id": "Hij_16", "node_id": "hco-003", "seq": 1},
    {"section_id": "Hij_17", "node_id": "hco-004", "seq": 1},
]

# ============================================================
# 9. SENTENCES
# ============================================================

SENTENCES = [
    # ==========================================================
    # Hij_14 -- Theme 14 接続詞で英文が読める
    # ==========================================================
    # ----------------------------------------------------------
    # Hij_14 -- 例題 (4問)
    # ----------------------------------------------------------
    {
        "id": "hij-14-e1-01",
        "section_id": "Hij_14",
        "drill": 1,
        "number": 1,
        "role": "example",
        "english": "She said that it was my mistake and that I must not do it again.",
        "japanese": "彼女は、それは私の間違いで、二度とやってはいけないと言った。",
        "notes": None,
    },
    {
        "id": "hij-14-e1-02",
        "section_id": "Hij_14",
        "drill": 1,
        "number": 2,
        "role": "example",
        "english": "This poses a threat to agriculture and the food chain, and to human health.",
        "japanese": "このことは、農業と食物連鎖への脅威と、人間の健康への脅威を提示している。",
        "notes": None,
    },
    {
        "id": "hij-14-e1-03",
        "section_id": "Hij_14",
        "drill": 1,
        "number": 3,
        "role": "example",
        "english": "I like watching TV, playing video games, and wasting time.",
        "japanese": "私はテレビを見て、テレビゲームをして、時間をむだにすることが好きだ。",
        "notes": None,
    },
    {
        "id": "hij-14-e1-04",
        "section_id": "Hij_14",
        "drill": 1,
        "number": 4,
        "role": "example",
        "english": "In Africa there are many people who do not have enough food, clothing or shelter.",
        "japanese": "アフリカでは、十分な衣食住をもたない多くの人がいる。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_14 -- 確認問題 (3問)
    # ----------------------------------------------------------
    {
        "id": "hij-14-c1-01",
        "section_id": "Hij_14",
        "drill": 2,
        "number": 1,
        "role": "practice",
        "english": "Kids who learn that books are wonderful, and who think of reading books as special are wonderful.",
        "japanese": "本がすばらしいとわかり、本を読むことを特別とみなす子どもたちは、すばらしい。",
        "notes": None,
    },
    {
        "id": "hij-14-c1-02",
        "section_id": "Hij_14",
        "drill": 2,
        "number": 2,
        "role": "practice",
        "english": "Some people are giving up highly paid but stressful jobs and becoming self-employed.",
        "japanese": "人びとのなかには、給料が高いが、ストレスの多い仕事を辞めて、自営業になりつつある人もいる。",
        "notes": None,
    },
    {
        "id": "hij-14-c1-03",
        "section_id": "Hij_14",
        "drill": 2,
        "number": 3,
        "role": "practice",
        "english": "They played games, made good friends, and enjoyed themselves very much.",
        "japanese": "その人たちは、ゲームをして、とても仲良くなり、とても楽しんだ。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_14 -- 発展問題 (1問)
    # ----------------------------------------------------------
    {
        "id": "hij-14-a1-01",
        "section_id": "Hij_14",
        "drill": 3,
        "number": 1,
        "role": "advanced",
        "english": "Being interested gives the people you are talking to the feeling that they are important and that you care about them.",
        "japanese": "興味をもつことは、あなたが話している人に自分たちが重要で、あなたが気にかけているという感覚を与える。",
        "notes": "山形大",
    },
    # ==========================================================
    # Hij_15_1 -- Theme 15 倒置で英文が読める①
    # ==========================================================
    # ----------------------------------------------------------
    # Hij_15_1 -- 例題 (5問)
    # ----------------------------------------------------------
    {
        "id": "hij-15_1-e1-01",
        "section_id": "Hij_15_1",
        "drill": 1,
        "number": 1,
        "role": "example",
        "english": "There was a low wall between our garden and the field.",
        "japanese": "私たちの庭と野原の間に低い壁があった。",
        "notes": None,
    },
    {
        "id": "hij-15_1-e1-02",
        "section_id": "Hij_15_1",
        "drill": 1,
        "number": 2,
        "role": "example",
        "english": "At the station were two women on their way to Sapporo.",
        "japanese": "駅に、札幌に行く途中の2人の女性がいた。",
        "notes": None,
    },
    {
        "id": "hij-15_1-e1-03",
        "section_id": "Hij_15_1",
        "drill": 1,
        "number": 3,
        "role": "example",
        "english": "More important is the experience of reading Greek.",
        "japanese": "より重要なのは、ギリシャ語を読む経験だ。",
        "notes": None,
    },
    {
        "id": "hij-15_1-e1-04",
        "section_id": "Hij_15_1",
        "drill": 1,
        "number": 4,
        "role": "example",
        "english": "Little did I dream that I met you in such a place.",
        "japanese": "私はそんな場所であなたに会うとは、夢にも思わなかった。",
        "notes": None,
    },
    {
        "id": "hij-15_1-e1-05",
        "section_id": "Hij_15_1",
        "drill": 1,
        "number": 5,
        "role": "example",
        "english": "Never in my life have I seen such a beautiful castle.",
        "japanese": "私は人生でそんな美しい城を、一度も見たことがない。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_15_1 -- 確認問題 (5問)
    # ----------------------------------------------------------
    {
        "id": "hij-15_1-c1-01",
        "section_id": "Hij_15_1",
        "drill": 2,
        "number": 1,
        "role": "practice",
        "english": "Surprised at the news was the girl.",
        "japanese": "そのニュースに驚いたのは、その女の子だった。",
        "notes": None,
    },
    {
        "id": "hij-15_1-c1-02",
        "section_id": "Hij_15_1",
        "drill": 2,
        "number": 2,
        "role": "practice",
        "english": "Little did I dream that such a thing would happen.",
        "japanese": "そのようなことが起きるとは夢にも思わなかった。",
        "notes": None,
    },
    {
        "id": "hij-15_1-c1-03",
        "section_id": "Hij_15_1",
        "drill": 2,
        "number": 3,
        "role": "practice",
        "english": "Never had he heard such a beautiful voice.",
        "japanese": "彼はそのような美しい声を一度も聞いたことがなかった。",
        "notes": None,
    },
    {
        "id": "hij-15_1-c1-04",
        "section_id": "Hij_15_1",
        "drill": 2,
        "number": 4,
        "role": "practice",
        "english": "There is something strange about her.",
        "japanese": "彼女に関して不思議なことがある。",
        "notes": None,
    },
    {
        "id": "hij-15_1-c1-05",
        "section_id": "Hij_15_1",
        "drill": 2,
        "number": 5,
        "role": "practice",
        "english": "Only after entering the bank did he realize that he was in danger.",
        "japanese": "銀行に入ってようやく、彼は危険な状態にいるとわかった。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_15_1 -- 発展問題 (1問)
    # ----------------------------------------------------------
    {
        "id": "hij-15_1-a1-01",
        "section_id": "Hij_15_1",
        "drill": 3,
        "number": 1,
        "role": "advanced",
        "english": "From separate signs emerged a more comprehensible and personal perception.",
        "japanese": "別々の兆候から、より理解しやすく個人的な認識が現れた。",
        "notes": "滋賀医科大",
    },
    # ==========================================================
    # Hij_15_2 -- Theme 15 倒置で英文が読める②
    # ==========================================================
    # ----------------------------------------------------------
    # Hij_15_2 -- 例題 (5問)
    # ----------------------------------------------------------
    {
        "id": "hij-15_2-e1-01",
        "section_id": "Hij_15_2",
        "drill": 1,
        "number": 1,
        "role": "example",
        "english": "I didn't understand her, nor did she understand me.",
        "japanese": "私は彼女を理解できなかったし、彼女も私を理解できなかった。",
        "notes": None,
    },
    {
        "id": "hij-15_2-e1-02",
        "section_id": "Hij_15_2",
        "drill": 1,
        "number": 2,
        "role": "example",
        "english": "I was very happy, and so were the others.",
        "japanese": "私はとても幸せだったし、ほかの人もそうだった。",
        "notes": None,
    },
    {
        "id": "hij-15_2-e1-03",
        "section_id": "Hij_15_2",
        "drill": 1,
        "number": 3,
        "role": "example",
        "english": "Were I in your position, I would not do that.",
        "japanese": "私があなたの立場なら、それはやらないだろう。",
        "notes": None,
    },
    {
        "id": "hij-15_2-e1-04",
        "section_id": "Hij_15_2",
        "drill": 1,
        "number": 4,
        "role": "example",
        "english": "Had it not been for water, we could not have lived.",
        "japanese": "水がなかったら、私たちは生きていけなかっただろう。",
        "notes": None,
    },
    {
        "id": "hij-15_2-e1-05",
        "section_id": "Hij_15_2",
        "drill": 1,
        "number": 5,
        "role": "example",
        "english": "Should you need any help, please let me know.",
        "japanese": "万が一あなたが助けを必要としているなら、どうか私に知らせてください。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_15_2 -- 確認問題 (3問)
    # ----------------------------------------------------------
    {
        "id": "hij-15_2-c1-01",
        "section_id": "Hij_15_2",
        "drill": 2,
        "number": 1,
        "role": "practice",
        "english": "Were I not so fond of her, I would leave her soon.",
        "japanese": "私が彼女をそんなに好きではないなら、すぐに彼女のもとを離れるだろう。",
        "notes": None,
    },
    {
        "id": "hij-15_2-c1-02",
        "section_id": "Hij_15_2",
        "drill": 2,
        "number": 2,
        "role": "practice",
        "english": "He knew little about the party, nor did he care.",
        "japanese": "彼はそのパーティーについてほとんど知らなかったし、気にもしていなかった。",
        "notes": None,
    },
    {
        "id": "hij-15_2-c1-03",
        "section_id": "Hij_15_2",
        "drill": 2,
        "number": 3,
        "role": "practice",
        "english": "Had I known more about her character, I would not have trusted.",
        "japanese": "もし私が彼女の性格をもっと知っていたら、私は信頼しなかっただろう。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_15_2 -- 発展問題 (1問)
    # ----------------------------------------------------------
    {
        "id": "hij-15_2-a1-01",
        "section_id": "Hij_15_2",
        "drill": 3,
        "number": 1,
        "role": "advanced",
        "english": "As English-speaking people became more important, so did their language.",
        "japanese": "英語を話す人びとがより重要になるにつれて、その言語もより重要になった。",
        "notes": "愛知学院大",
    },
    # ==========================================================
    # Hij_16 -- Theme 16 省略で英文が読める
    # ==========================================================
    # ----------------------------------------------------------
    # Hij_16 -- 例題 (4問)
    # ----------------------------------------------------------
    {
        "id": "hij-16-e1-01",
        "section_id": "Hij_16",
        "drill": 1,
        "number": 1,
        "role": "example",
        "english": "When young, I was very interested in Japanese movies.",
        "japanese": "若いころ、私は日本映画にとても興味があった。",
        "notes": None,
    },
    {
        "id": "hij-16-e1-02",
        "section_id": "Hij_16",
        "drill": 1,
        "number": 2,
        "role": "example",
        "english": "My father is as fond of books as my uncle is of movies.",
        "japanese": "私の父は、おじが映画を好きなのと同じくらい本が好きだ。",
        "notes": None,
    },
    {
        "id": "hij-16-e1-03",
        "section_id": "Hij_16",
        "drill": 1,
        "number": 3,
        "role": "example",
        "english": "She said she had met him three hours before.",
        "japanese": "彼女は、3時間前に彼に会ったと言った。",
        "notes": None,
    },
    {
        "id": "hij-16-e1-04",
        "section_id": "Hij_16",
        "drill": 1,
        "number": 4,
        "role": "example",
        "english": "The boy opened the window, although his mother told him not to.",
        "japanese": "彼の母はやらないように言ったが、その少年は窓を開けた。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_16 -- 確認問題 (4問)
    # ----------------------------------------------------------
    {
        "id": "hij-16-c1-01",
        "section_id": "Hij_16",
        "drill": 2,
        "number": 1,
        "role": "practice",
        "english": "I don't think there'll be time to visit the place.",
        "japanese": "私はその場所を訪ねる時間がないと思う。",
        "notes": None,
    },
    {
        "id": "hij-16-c1-02",
        "section_id": "Hij_16",
        "drill": 2,
        "number": 2,
        "role": "practice",
        "english": "He isn't as energetic as he used to be.",
        "japanese": "彼は以前ほど精力的ではない。",
        "notes": None,
    },
    {
        "id": "hij-16-c1-03",
        "section_id": "Hij_16",
        "drill": 2,
        "number": 3,
        "role": "practice",
        "english": "Cold chicken is delicious when eaten with salad.",
        "japanese": "冷製チキンはサラダと食べるとおいしい。",
        "notes": None,
    },
    {
        "id": "hij-16-c1-04",
        "section_id": "Hij_16",
        "drill": 2,
        "number": 4,
        "role": "practice",
        "english": "He rarely does his best until he is forced to.",
        "japanese": "彼はやらざるをえないときまで、めったに最善をつくさない。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_16 -- 発展問題 (1問)
    # ----------------------------------------------------------
    {
        "id": "hij-16-a1-01",
        "section_id": "Hij_16",
        "drill": 3,
        "number": 1,
        "role": "advanced",
        "english": "When creating a video game, game designers feel it is important to keep within the limits of the computer's own power.",
        "japanese": "テレビゲームをつくるとき、ゲームデザイナーはコンピュータ自体の力の範囲内に保つことが重要だと感じている。",
        "notes": "青山学院大",
    },
    # ==========================================================
    # Hij_17 -- Theme 17 強調構文で英文が読める
    # ==========================================================
    # ----------------------------------------------------------
    # Hij_17 -- 例題 (5問)
    # ----------------------------------------------------------
    {
        "id": "hij-17-e1-01",
        "section_id": "Hij_17",
        "drill": 1,
        "number": 1,
        "role": "example",
        "english": "It was only yesterday that we last met.",
        "japanese": "私たちが最後に会ったのは、つい昨日のことだった。",
        "notes": None,
    },
    {
        "id": "hij-17-e1-02",
        "section_id": "Hij_17",
        "drill": 1,
        "number": 2,
        "role": "example",
        "english": "It was because Tom was rich that Mary married him.",
        "japanese": "メアリーがトムと結婚したのは、彼がお金持ちだったからだ。",
        "notes": None,
    },
    {
        "id": "hij-17-e1-03",
        "section_id": "Hij_17",
        "drill": 1,
        "number": 3,
        "role": "example",
        "english": "It was because of the train accident that the bus was very crowded.",
        "japanese": "バスがとても混雑していたのは、列車事故が原因だった。",
        "notes": None,
    },
    {
        "id": "hij-17-e1-04",
        "section_id": "Hij_17",
        "drill": 1,
        "number": 4,
        "role": "example",
        "english": "It was not until yesterday that I knew the news.",
        "japanese": "昨日になってはじめて、私はそのニュースを知った。",
        "notes": None,
    },
    {
        "id": "hij-17-e1-05",
        "section_id": "Hij_17",
        "drill": 1,
        "number": 5,
        "role": "example",
        "english": "It was my mother that told me to do housework.",
        "japanese": "私に家事をやるように言ったのは、私の母だった。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_17 -- 確認問題 (5問)
    # ----------------------------------------------------------
    {
        "id": "hij-17-c1-01",
        "section_id": "Hij_17",
        "drill": 2,
        "number": 1,
        "role": "practice",
        "english": "It was because I caught a cold that I was absent from school.",
        "japanese": "私が学校を休んだのは、風邪をひいたからだ。",
        "notes": None,
    },
    {
        "id": "hij-17-c1-02",
        "section_id": "Hij_17",
        "drill": 2,
        "number": 2,
        "role": "practice",
        "english": "It was not until yesterday that I started the project.",
        "japanese": "昨日になってはじめて、私はその計画を始めた。",
        "notes": None,
    },
    {
        "id": "hij-17-c1-03",
        "section_id": "Hij_17",
        "drill": 2,
        "number": 3,
        "role": "practice",
        "english": "It was due to the heavy rain that the game was cancelled.",
        "japanese": "その試合が中止されたのは、ひどい雨が原因だった。",
        "notes": None,
    },
    {
        "id": "hij-17-c1-04",
        "section_id": "Hij_17",
        "drill": 2,
        "number": 4,
        "role": "practice",
        "english": "It is only recently that we have got so much information.",
        "japanese": "私たちがそんなに多くの情報を手に入れるようになったのは、つい最近のことだ。",
        "notes": None,
    },
    {
        "id": "hij-17-c1-05",
        "section_id": "Hij_17",
        "drill": 2,
        "number": 5,
        "role": "practice",
        "english": "It is the type of brain that determines the differences in the psychology of the sexes.",
        "japanese": "性別の心理の違いを決定するのは、脳の種類だ。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_17 -- 発展問題 (1問)
    # ----------------------------------------------------------
    {
        "id": "hij-17-a1-01",
        "section_id": "Hij_17",
        "drill": 3,
        "number": 1,
        "role": "advanced",
        "english": "It is only when they are about eighteen months old that they understand that they are being reflected in the mirror.",
        "japanese": "生後18か月ころになって、ようやく自分が鏡に映っていると理解する。",
        "notes": "関西大",
    },
]

# ============================================================
# 10. SENTENCE_STRUCTURES
# ============================================================

SENTENCE_STRUCTURES = [
    # === Hij_14 例題 ===
    # --- hij-14-e1-01 ---
    {"sentence_id": "hij-14-e1-01", "label": "overall", "value": "S V O and O"},
    {"sentence_id": "hij-14-e1-01", "label": "details", "value": "She(S) said(V) <that it was my mistake>(O:that節) and <that I must not do it again>(O:that節)"},
    # --- hij-14-e1-02 ---
    {"sentence_id": "hij-14-e1-02", "label": "overall", "value": "S V O M and M"},
    {"sentence_id": "hij-14-e1-02", "label": "details", "value": "This(S) poses(V) a threat(O) [to agriculture and the food chain](M), and [to human health](M)"},
    # --- hij-14-e1-03 ---
    {"sentence_id": "hij-14-e1-03", "label": "overall", "value": "S V O"},
    {"sentence_id": "hij-14-e1-03", "label": "details", "value": "I(S) like(V) <watching TV, playing video games, and wasting time>(O:動名詞3つの並列)"},
    # --- hij-14-e1-04 ---
    {"sentence_id": "hij-14-e1-04", "label": "overall", "value": "M V S (M)"},
    {"sentence_id": "hij-14-e1-04", "label": "details", "value": "[In Africa](M) there(M) are(V) many people(S) (who do not have enough food, clothing or shelter)(M:関係代名詞節)"},
    # === Hij_14 確認問題 ===
    # --- hij-14-c1-01 ---
    {"sentence_id": "hij-14-c1-01", "label": "overall", "value": "S (M and M) V C"},
    {"sentence_id": "hij-14-c1-01", "label": "details", "value": "Kids(S) (who learn that books are wonderful)(M:関係代名詞節), and (who think of reading books as special)(M:関係代名詞節) are(V) wonderful(C)"},
    # --- hij-14-c1-02 ---
    {"sentence_id": "hij-14-c1-02", "label": "overall", "value": "S V O and V C"},
    {"sentence_id": "hij-14-c1-02", "label": "details", "value": "Some people(S) are giving up(V1) (highly paid but stressful)(M) jobs(O) and becoming(V2) self-employed(C)"},
    # --- hij-14-c1-03 ---
    {"sentence_id": "hij-14-c1-03", "label": "overall", "value": "S V1 O1, V2 O2, and V3 O3 M"},
    {"sentence_id": "hij-14-c1-03", "label": "details", "value": "They(S) played(V1) games(O1), made(V2) good friends(O2), and enjoyed(V3) themselves(O3) very much(M)"},
    # === Hij_14 発展問題 ===
    # --- hij-14-a1-01 ---
    {"sentence_id": "hij-14-a1-01", "label": "overall", "value": "S V O1 O2"},
    {"sentence_id": "hij-14-a1-01", "label": "details", "value": "<Being interested>(S:動名詞) gives(V) the people (you are talking to)(O1:関係代名詞省略) the feeling(O2) <that they are important>(同格) and <that you care about them>(同格)"},
    # === Hij_15_1 例題 ===
    # --- hij-15_1-e1-01 ---
    {"sentence_id": "hij-15_1-e1-01", "label": "overall", "value": "M V S M"},
    {"sentence_id": "hij-15_1-e1-01", "label": "details", "value": "There(M) was(V) a low wall(S) [between our garden and the field](M)"},
    # --- hij-15_1-e1-02 ---
    {"sentence_id": "hij-15_1-e1-02", "label": "overall", "value": "M V S M"},
    {"sentence_id": "hij-15_1-e1-02", "label": "details", "value": "[At the station](M) were(V) two women(S) (on their way to Sapporo)(M)"},
    # --- hij-15_1-e1-03 ---
    {"sentence_id": "hij-15_1-e1-03", "label": "overall", "value": "C V S M"},
    {"sentence_id": "hij-15_1-e1-03", "label": "details", "value": "More important(C) is(V) the experience(S) (of reading Greek)(M)"},
    # --- hij-15_1-e1-04 ---
    {"sentence_id": "hij-15_1-e1-04", "label": "overall", "value": "M V S O"},
    {"sentence_id": "hij-15_1-e1-04", "label": "details", "value": "Little(M:否定副詞) did(助動詞) I(S) dream(V) <that I met you in such a place>(O)"},
    # --- hij-15_1-e1-05 ---
    {"sentence_id": "hij-15_1-e1-05", "label": "overall", "value": "M M V S O"},
    {"sentence_id": "hij-15_1-e1-05", "label": "details", "value": "Never(M:否定副詞) [in my life](M) have(助動詞) I(S) seen(V) such a beautiful castle(O)"},
    # === Hij_15_1 確認問題 ===
    # --- hij-15_1-c1-01 ---
    {"sentence_id": "hij-15_1-c1-01", "label": "overall", "value": "C M V S"},
    {"sentence_id": "hij-15_1-c1-01", "label": "details", "value": "Surprised(C:過去分詞) [at the news](M) was(V) the girl(S)"},
    # --- hij-15_1-c1-02 ---
    {"sentence_id": "hij-15_1-c1-02", "label": "overall", "value": "M V S O"},
    {"sentence_id": "hij-15_1-c1-02", "label": "details", "value": "Little(M:否定副詞) did(助動詞) I(S) dream(V) <that such a thing would happen>(O)"},
    # --- hij-15_1-c1-03 ---
    {"sentence_id": "hij-15_1-c1-03", "label": "overall", "value": "M V S O"},
    {"sentence_id": "hij-15_1-c1-03", "label": "details", "value": "Never(M:否定副詞) had(助動詞) he(S) heard(V) such a beautiful voice(O)"},
    # --- hij-15_1-c1-04 ---
    {"sentence_id": "hij-15_1-c1-04", "label": "overall", "value": "M V S (M) M"},
    {"sentence_id": "hij-15_1-c1-04", "label": "details", "value": "There(M) is(V) something(S) (strange)(M:形容詞) [about her](M)"},
    # --- hij-15_1-c1-05 ---
    {"sentence_id": "hij-15_1-c1-05", "label": "overall", "value": "M M V S O"},
    {"sentence_id": "hij-15_1-c1-05", "label": "details", "value": "Only(M:否定副詞) [after entering the bank](M) did(助動詞) he(S) realize(V) <that he was in danger>(O)"},
    # === Hij_15_1 発展問題 ===
    # --- hij-15_1-a1-01 ---
    {"sentence_id": "hij-15_1-a1-01", "label": "overall", "value": "M V S"},
    {"sentence_id": "hij-15_1-a1-01", "label": "details", "value": "[From separate signs](M) emerged(V) a more comprehensible and personal perception(S)"},
    # === Hij_15_2 例題 ===
    # --- hij-15_2-e1-01 ---
    {"sentence_id": "hij-15_2-e1-01", "label": "overall", "value": "S V O, nor V S O"},
    {"sentence_id": "hij-15_2-e1-01", "label": "details", "value": "I(S) didn't understand(V) her(O), nor did(助動詞) she(S) understand(V) me(O)"},
    # --- hij-15_2-e1-02 ---
    {"sentence_id": "hij-15_2-e1-02", "label": "overall", "value": "S V C, and so V S"},
    {"sentence_id": "hij-15_2-e1-02", "label": "details", "value": "I(S) was(V) very happy(C), and so were(V) the others(S)"},
    # --- hij-15_2-e1-03 ---
    {"sentence_id": "hij-15_2-e1-03", "label": "overall", "value": "[M] S V O"},
    {"sentence_id": "hij-15_2-e1-03", "label": "details", "value": "[Were I in your position](M:仮定法倒置) I(S) would not do(V) that(O)"},
    # --- hij-15_2-e1-04 ---
    {"sentence_id": "hij-15_2-e1-04", "label": "overall", "value": "[M] S V"},
    {"sentence_id": "hij-15_2-e1-04", "label": "details", "value": "[Had it not been for water](M:仮定法倒置) we(S) could not have lived(V)"},
    # --- hij-15_2-e1-05 ---
    {"sentence_id": "hij-15_2-e1-05", "label": "overall", "value": "[M] V O C"},
    {"sentence_id": "hij-15_2-e1-05", "label": "details", "value": "[Should you need any help](M:仮定法倒置) please(M) let(V) me(O) know(C)"},
    # === Hij_15_2 確認問題 ===
    # --- hij-15_2-c1-01 ---
    {"sentence_id": "hij-15_2-c1-01", "label": "overall", "value": "[M] S V O M"},
    {"sentence_id": "hij-15_2-c1-01", "label": "details", "value": "[Were I not so fond of her](M:仮定法倒置) I(S) would leave(V) her(O) soon(M)"},
    # --- hij-15_2-c1-02 ---
    {"sentence_id": "hij-15_2-c1-02", "label": "overall", "value": "S V O M, nor V S"},
    {"sentence_id": "hij-15_2-c1-02", "label": "details", "value": "He(S) knew(V) little(O) [about the party](M), nor did(助動詞) he(S) care(V)"},
    # --- hij-15_2-c1-03 ---
    {"sentence_id": "hij-15_2-c1-03", "label": "overall", "value": "[M] S V"},
    {"sentence_id": "hij-15_2-c1-03", "label": "details", "value": "[Had I known more about her character](M:仮定法倒置) I(S) would not have trusted(V)"},
    # === Hij_15_2 発展問題 ===
    # --- hij-15_2-a1-01 ---
    {"sentence_id": "hij-15_2-a1-01", "label": "overall", "value": "M so V S"},
    {"sentence_id": "hij-15_2-a1-01", "label": "details", "value": "[As English-speaking people became more important](M:比例のas) so did(V:代動詞) their language(S)"},
    # === Hij_16 例題 ===
    # --- hij-16-e1-01 ---
    {"sentence_id": "hij-16-e1-01", "label": "overall", "value": "M S V C M"},
    {"sentence_id": "hij-16-e1-01", "label": "details", "value": "[When (I was) young](M:SVの省略) I(S) was(V) very interested(C) [in Japanese movies](M)"},
    # --- hij-16-e1-02 ---
    {"sentence_id": "hij-16-e1-02", "label": "overall", "value": "S V C M S V M"},
    {"sentence_id": "hij-16-e1-02", "label": "details", "value": "My father(S1) is(V1) as fond(C) [of books](M) as my uncle(S2) is(V2) (fond:省略) [of movies](M)"},
    # --- hij-16-e1-03 ---
    {"sentence_id": "hij-16-e1-03", "label": "overall", "value": "S V O"},
    {"sentence_id": "hij-16-e1-03", "label": "details", "value": "She(S) said(V) <(that) she had met him three hours before>(O:thatの省略)"},
    # --- hij-16-e1-04 ---
    {"sentence_id": "hij-16-e1-04", "label": "overall", "value": "S V O M"},
    {"sentence_id": "hij-16-e1-04", "label": "details", "value": "The boy(S) opened(V) the window(O), [although his mother told him not to (open the window)](M:代不定詞)"},
    # === Hij_16 確認問題 ===
    # --- hij-16-c1-01 ---
    {"sentence_id": "hij-16-c1-01", "label": "overall", "value": "S V O"},
    {"sentence_id": "hij-16-c1-01", "label": "details", "value": "I(S) don't think(V) <(that) there'll be time to visit the place>(O:thatの省略)"},
    # --- hij-16-c1-02 ---
    {"sentence_id": "hij-16-c1-02", "label": "overall", "value": "S V C M"},
    {"sentence_id": "hij-16-c1-02", "label": "details", "value": "He(S) isn't(V) as energetic(C) [as he used to be (energetic:省略)](M:比較の省略)"},
    # --- hij-16-c1-03 ---
    {"sentence_id": "hij-16-c1-03", "label": "overall", "value": "S V C M"},
    {"sentence_id": "hij-16-c1-03", "label": "details", "value": "Cold chicken(S) is(V) delicious(C) [when (it is) eaten with salad](M:SVの省略)"},
    # --- hij-16-c1-04 ---
    {"sentence_id": "hij-16-c1-04", "label": "overall", "value": "S M V O M"},
    {"sentence_id": "hij-16-c1-04", "label": "details", "value": "He(S) rarely(M) does(V) his best(O) [until he is forced to (do his best:省略)](M:代不定詞)"},
    # === Hij_16 発展問題 ===
    # --- hij-16-a1-01 ---
    {"sentence_id": "hij-16-a1-01", "label": "overall", "value": "M S V O"},
    {"sentence_id": "hij-16-a1-01", "label": "details", "value": "[When (they are) creating a video game](M:SVの省略) game designers(S) feel(V) <(that) it is important to keep within the limits of the computer's own power>(O:thatの省略+形式主語)"},
    # === Hij_17 例題 ===
    # --- hij-17-e1-01 ---
    {"sentence_id": "hij-17-e1-01", "label": "overall", "value": "強調構文（副詞）"},
    {"sentence_id": "hij-17-e1-01", "label": "details", "value": "It was [only yesterday](強調:副詞) that we last met"},
    # --- hij-17-e1-02 ---
    {"sentence_id": "hij-17-e1-02", "label": "overall", "value": "強調構文（副詞節）"},
    {"sentence_id": "hij-17-e1-02", "label": "details", "value": "It was [because Tom was rich](強調:副詞節) that Mary married him"},
    # --- hij-17-e1-03 ---
    {"sentence_id": "hij-17-e1-03", "label": "overall", "value": "強調構文（前置詞句）"},
    {"sentence_id": "hij-17-e1-03", "label": "details", "value": "It was [because of the train accident](強調:前置詞句) that the bus was very crowded"},
    # --- hij-17-e1-04 ---
    {"sentence_id": "hij-17-e1-04", "label": "overall", "value": "強調構文（not until）"},
    {"sentence_id": "hij-17-e1-04", "label": "details", "value": "It was [not until yesterday](強調:前置詞句) that I knew the news"},
    # --- hij-17-e1-05 ---
    {"sentence_id": "hij-17-e1-05", "label": "overall", "value": "強調構文（名詞＋不完全文）"},
    {"sentence_id": "hij-17-e1-05", "label": "details", "value": "It was [my mother](強調:名詞) that told(Sが欠けた不完全文) me to do housework"},
    # === Hij_17 確認問題 ===
    # --- hij-17-c1-01 ---
    {"sentence_id": "hij-17-c1-01", "label": "overall", "value": "強調構文（副詞節）"},
    {"sentence_id": "hij-17-c1-01", "label": "details", "value": "It was [because I caught a cold](強調:副詞節) that I was absent from school"},
    # --- hij-17-c1-02 ---
    {"sentence_id": "hij-17-c1-02", "label": "overall", "value": "強調構文（not until）"},
    {"sentence_id": "hij-17-c1-02", "label": "details", "value": "It was [not until yesterday](強調:副詞) that I started the project"},
    # --- hij-17-c1-03 ---
    {"sentence_id": "hij-17-c1-03", "label": "overall", "value": "強調構文（前置詞句）"},
    {"sentence_id": "hij-17-c1-03", "label": "details", "value": "It was [due to the heavy rain](強調:前置詞句) that the game was cancelled"},
    # --- hij-17-c1-04 ---
    {"sentence_id": "hij-17-c1-04", "label": "overall", "value": "強調構文（副詞）"},
    {"sentence_id": "hij-17-c1-04", "label": "details", "value": "It is [only recently](強調:副詞) that we have got so much information"},
    # --- hij-17-c1-05 ---
    {"sentence_id": "hij-17-c1-05", "label": "overall", "value": "強調構文（名詞＋不完全文）"},
    {"sentence_id": "hij-17-c1-05", "label": "details", "value": "It is [the type of brain](強調:名詞) that determines(Sが欠けた不完全文) the differences in the psychology of the sexes"},
    # === Hij_17 発展問題 ===
    # --- hij-17-a1-01 ---
    {"sentence_id": "hij-17-a1-01", "label": "overall", "value": "強調構文（副詞節）"},
    {"sentence_id": "hij-17-a1-01", "label": "details", "value": "It is [only when they are about eighteen months old](強調:副詞節) that they understand <that they are being reflected in the mirror>(O:名詞節)"},
]

# ============================================================
# 11. SENTENCE_KNOWLEDGE_TAGS
# ============================================================

SENTENCE_KNOWLEDGE_TAGS = [
    # --- Hij_14 例題 ---
    {"sentence_id": "hij-14-e1-01", "node_id": "hco-001"},
    {"sentence_id": "hij-14-e1-02", "node_id": "hco-001"},
    {"sentence_id": "hij-14-e1-03", "node_id": "hco-001"},
    {"sentence_id": "hij-14-e1-04", "node_id": "hco-001"},
    # --- Hij_14 確認問題 ---
    {"sentence_id": "hij-14-c1-01", "node_id": "hco-001"},
    {"sentence_id": "hij-14-c1-02", "node_id": "hco-001"},
    {"sentence_id": "hij-14-c1-03", "node_id": "hco-001"},
    # --- Hij_14 発展問題 ---
    {"sentence_id": "hij-14-a1-01", "node_id": "hco-001"},
    # --- Hij_15_1 例題 ---
    {"sentence_id": "hij-15_1-e1-01", "node_id": "hco-002"},
    {"sentence_id": "hij-15_1-e1-02", "node_id": "hco-002"},
    {"sentence_id": "hij-15_1-e1-03", "node_id": "hco-002"},
    {"sentence_id": "hij-15_1-e1-04", "node_id": "hco-002"},
    {"sentence_id": "hij-15_1-e1-05", "node_id": "hco-002"},
    # --- Hij_15_1 確認問題 ---
    {"sentence_id": "hij-15_1-c1-01", "node_id": "hco-002"},
    {"sentence_id": "hij-15_1-c1-02", "node_id": "hco-002"},
    {"sentence_id": "hij-15_1-c1-03", "node_id": "hco-002"},
    {"sentence_id": "hij-15_1-c1-04", "node_id": "hco-002"},
    {"sentence_id": "hij-15_1-c1-05", "node_id": "hco-002"},
    # --- Hij_15_1 発展問題 ---
    {"sentence_id": "hij-15_1-a1-01", "node_id": "hco-002"},
    # --- Hij_15_2 例題 ---
    {"sentence_id": "hij-15_2-e1-01", "node_id": "hco-011"},
    {"sentence_id": "hij-15_2-e1-02", "node_id": "hco-011"},
    {"sentence_id": "hij-15_2-e1-03", "node_id": "hco-011"},
    {"sentence_id": "hij-15_2-e1-04", "node_id": "hco-011"},
    {"sentence_id": "hij-15_2-e1-05", "node_id": "hco-011"},
    # --- Hij_15_2 確認問題 ---
    {"sentence_id": "hij-15_2-c1-01", "node_id": "hco-011"},
    {"sentence_id": "hij-15_2-c1-02", "node_id": "hco-011"},
    {"sentence_id": "hij-15_2-c1-03", "node_id": "hco-011"},
    # --- Hij_15_2 発展問題 ---
    {"sentence_id": "hij-15_2-a1-01", "node_id": "hco-011"},
    # --- Hij_16 例題 ---
    {"sentence_id": "hij-16-e1-01", "node_id": "hco-003"},
    {"sentence_id": "hij-16-e1-02", "node_id": "hco-003"},
    {"sentence_id": "hij-16-e1-03", "node_id": "hco-003"},
    {"sentence_id": "hij-16-e1-04", "node_id": "hco-003"},
    # --- Hij_16 確認問題 ---
    {"sentence_id": "hij-16-c1-01", "node_id": "hco-003"},
    {"sentence_id": "hij-16-c1-02", "node_id": "hco-003"},
    {"sentence_id": "hij-16-c1-03", "node_id": "hco-003"},
    {"sentence_id": "hij-16-c1-04", "node_id": "hco-003"},
    # --- Hij_16 発展問題 ---
    {"sentence_id": "hij-16-a1-01", "node_id": "hco-003"},
    # --- Hij_17 例題 ---
    {"sentence_id": "hij-17-e1-01", "node_id": "hco-004"},
    {"sentence_id": "hij-17-e1-02", "node_id": "hco-004"},
    {"sentence_id": "hij-17-e1-03", "node_id": "hco-004"},
    {"sentence_id": "hij-17-e1-04", "node_id": "hco-004"},
    {"sentence_id": "hij-17-e1-05", "node_id": "hco-004"},
    # --- Hij_17 確認問題 ---
    {"sentence_id": "hij-17-c1-01", "node_id": "hco-004"},
    {"sentence_id": "hij-17-c1-02", "node_id": "hco-004"},
    {"sentence_id": "hij-17-c1-03", "node_id": "hco-004"},
    {"sentence_id": "hij-17-c1-04", "node_id": "hco-004"},
    {"sentence_id": "hij-17-c1-05", "node_id": "hco-004"},
    # --- Hij_17 発展問題 ---
    {"sentence_id": "hij-17-a1-01", "node_id": "hco-004"},
]
