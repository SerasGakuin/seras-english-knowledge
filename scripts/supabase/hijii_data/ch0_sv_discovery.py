"""序章: SVの発見（Theme 01 ①②、Intro）— 5ノード、18英文"""

# ============================================================
# 1. KNOWLEDGE_NODES
# ============================================================

KNOWLEDGE_NODES = [
    {
        "id": "hsv-000",
        "name": "文の要素と意味のカタマリ",
        "category": "SVの発見",
        "priority": "P1",
        "notes": "SVOCM（主語・動詞・目的語・補語・修飾語）の5つの文の要素と、句（SVなし）・節（SVあり）の区別、名詞/形容詞/副詞/前置詞の品詞の役割を理解する。英文読解の基盤となる用語・概念。",
    },
    {
        "id": "hsv-001",
        "name": "名詞節による長い主語の発見",
        "category": "SVの発見",
        "priority": "P1",
        "notes": "That/What/Howなどが文頭で名詞節（名詞のカタマリ）をつくり、長い主語になるパターン。「1つの節にSVは1つ」を根拠に、2個目の動詞の手前で主語の範囲を確定する。",
    },
    {
        "id": "hsv-002",
        "name": "動詞の過去形と過去分詞の識別",
        "category": "SVの発見",
        "priority": "P1",
        "notes": "見た目が同じ過去形とp.p.を区別するパターン。(1)過去形とすると目的語がない、(2)うしろに本当の動詞がある、の2点を根拠に過去分詞と判断し、形容詞のカタマリとして前の名詞を修飾すると解釈する。",
    },
    {
        "id": "hsv-003",
        "name": "関係代名詞の省略によるSV発見",
        "category": "SVの発見",
        "priority": "P1",
        "notes": "「名詞+SV」の語順で関係代名詞の省略を見抜くパターン。(1)名詞SVの語順、(2)Oがない、の2条件を根拠に関係代名詞の省略と判断し、形容詞のカタマリの範囲を確定して文のSVを特定する。",
    },
    {
        "id": "hsv-004",
        "name": "修飾語(M)によるSVO把握の難化パターン",
        "category": "SVの発見",
        "priority": "P1",
        "notes": "Mが文頭(MSV)・SV間(SMV)・VO間(SVMO)に入ることでSVOの把握が難しくなるパターン。群前置詞・前置詞句・分詞句・不定詞句・関係詞節がMをつくる。「句のなかにSVは含まれない」を根拠にMの範囲を確定し、SVOを特定する。",
    },
]

# ============================================================
# 2. UNDERSTANDING_GOALS
# ============================================================

UNDERSTANDING_GOALS = [
    # hsv-000
    {"node_id": "hsv-000", "seq": 1, "goal": "S（主語）、V（動詞）、O（目的語）、C（補語）、M（修飾語）の5つの文の要素を説明できる"},
    {"node_id": "hsv-000", "seq": 2, "goal": "句（SVの文構造がない意味のカタマリ）と節（SVの文構造がある意味のカタマリ）の違いを説明できる"},
    {"node_id": "hsv-000", "seq": 3, "goal": "名詞・形容詞・副詞・前置詞の4品詞の役割を説明できる"},
    {"node_id": "hsv-000", "seq": 4, "goal": "名詞のカタマリ〈〉、形容詞のカタマリ（）、副詞のカタマリ[]の表記法を理解している"},
    # hsv-001
    {"node_id": "hsv-001", "seq": 1, "goal": "That/What/Howが文頭にきたとき、名詞節が長い主語をつくる可能性に気づける"},
    {"node_id": "hsv-001", "seq": 2, "goal": "「1つの節にSVは1つしか使えない」ことを根拠に、2個目の動詞の手前で名詞節の範囲を確定できる"},
    {"node_id": "hsv-001", "seq": 3, "goal": "名詞節による長い主語の範囲を正確に指摘し、文のSとVを特定できる"},
    # hsv-002
    {"node_id": "hsv-002", "seq": 1, "goal": "過去分詞を動詞の過去形とすると目的語がないことに気づける"},
    {"node_id": "hsv-002", "seq": 2, "goal": "過去分詞のうしろに本当の動詞があることを根拠に、過去分詞と判断できる"},
    {"node_id": "hsv-002", "seq": 3, "goal": "過去分詞が形容詞のカタマリをつくって前の名詞を修飾するパターンを認識できる"},
    # hsv-003
    {"node_id": "hsv-003", "seq": 1, "goal": "「名詞+SV」の語順から関係代名詞の省略を見抜ける"},
    {"node_id": "hsv-003", "seq": 2, "goal": "関係代名詞が省略された形容詞のカタマリの範囲を確定できる"},
    {"node_id": "hsv-003", "seq": 3, "goal": "Oの欠如を関係代名詞省略の根拠として利用できる"},
    # hsv-004
    {"node_id": "hsv-004", "seq": 1, "goal": "群前置詞（thanks to, due to, because of等）が文頭で副詞句をつくるMSVパターンを認識できる"},
    {"node_id": "hsv-004", "seq": 2, "goal": "前置詞句・分詞句・不定詞句・関係詞節がSV間に入るSMVパターンを認識できる"},
    {"node_id": "hsv-004", "seq": 3, "goal": "他動詞のあとに前置詞句のMが入り、目的語が後方に回るSVMOパターンを認識できる"},
    {"node_id": "hsv-004", "seq": 4, "goal": "「句のなかにSVは含まれない」ことを根拠にMの範囲を確定し、SVを特定できる"},
]

# ============================================================
# 3. CHECK_POINTS
# ============================================================

CHECK_POINTS = [
    # hsv-000
    {"node_id": "hsv-000", "seq": 1, "question": "文の要素SVOCMのうち、Mとは何か？", "answer": "修飾語。前置詞のカタマリ、名詞をうしろから修飾する形容詞のカタマリ、副詞がMにあたる。"},
    {"node_id": "hsv-000", "seq": 2, "question": "句と節の違いは何か？", "answer": "句はSVの文構造がない意味のカタマリ、節はSVの文構造がある意味のカタマリ。"},
    {"node_id": "hsv-000", "seq": 3, "question": "名詞は文のどの要素になれるか？", "answer": "S（主語）、O（目的語）、C（補語）のいずれか。"},
    {"node_id": "hsv-000", "seq": 4, "question": "前置詞はどのようなカタマリをつくるか？", "answer": "形容詞のカタマリ（前の名詞を修飾）と副詞のカタマリ（動詞を修飾）をつくる。"},
    # hsv-001
    {"node_id": "hsv-001", "seq": 1, "question": "長いSをつくれる代表的な単語は？", "answer": "That / What / How（名詞節をつくる単語）。"},
    {"node_id": "hsv-001", "seq": 2, "question": "名詞節による長いSの範囲を確定する根拠は？", "answer": "「1つの節にSVは1つしか使えない」ので、2個目の動詞の手前でSの範囲が終わる。"},
    {"node_id": "hsv-001", "seq": 3, "question": "That he ate ten hamburgers surprised me. のSとVは？", "answer": "S = That he ate ten hamburgers、V = surprised。"},
    # hsv-002
    {"node_id": "hsv-002", "seq": 1, "question": "動詞の過去形と過去分詞の識別で使う2つの根拠は？", "answer": "(1)過去分詞を動詞の過去形とすると目的語がない、(2)うしろに本当の動詞がある。"},
    {"node_id": "hsv-002", "seq": 2, "question": "A rainbow observed by the woman was round. のVは何か？また、observedは何か？", "answer": "Vはwas。observedは過去分詞で、observed by the womanが形容詞のカタマリとしてA rainbowを修飾する。"},
    {"node_id": "hsv-002", "seq": 3, "question": "過去分詞がつくる形容詞のカタマリの位置は？", "answer": "うしろから前の名詞を修飾する（後置修飾）。"},
    # hsv-003
    {"node_id": "hsv-003", "seq": 1, "question": "関係代名詞省略を見抜く2つの条件は？", "answer": "(1)名詞SVの語順、(2)Oがない。"},
    {"node_id": "hsv-003", "seq": 2, "question": "The world we live in has changed in recent years. のSとVは？", "answer": "S = The world、V = has changed。weとlive inの間に関係代名詞が省略されている。"},
    {"node_id": "hsv-003", "seq": 3, "question": "関係代名詞が省略されたカタマリは何のはたらきをするか？", "answer": "形容詞のカタマリとして前の名詞を修飾する。"},
    # hsv-004
    {"node_id": "hsv-004", "seq": 1, "question": "群前置詞の例を3つ挙げよ。", "answer": "thanks to（～のおかげで）、because of（～が原因で）、due to（～が原因で）、in addition to（～に加えて）、in spite of（～にもかかわらず）など。"},
    {"node_id": "hsv-004", "seq": 2, "question": "SMVパターンでMに入りうる語句は？", "answer": "前置詞句、分詞句、不定詞句、関係詞節。"},
    {"node_id": "hsv-004", "seq": 3, "question": "SVMOパターンを見抜くポイントは？", "answer": "他動詞のあとに前置詞句が入り、目的語(O)がうしろに回っている。「目的語は名詞しかなれない」ので、前置詞句はOにならない。"},
    {"node_id": "hsv-004", "seq": 4, "question": "Mの範囲を確定する根拠は？", "answer": "「句のなかにSVは含まれない」こと。句の終わりを見極めてSVを確定する。"},
]

# ============================================================
# 4. NODE_PREREQUISITES
# ============================================================

NODE_PREREQUISITES = [
    {"node_id": "hsv-001", "prerequisite_id": "hsv-000"},
    {"node_id": "hsv-002", "prerequisite_id": "hsv-000"},
    {"node_id": "hsv-003", "prerequisite_id": "hsv-000"},
    {"node_id": "hsv-004", "prerequisite_id": "hsv-000"},
]

# ============================================================
# 5. KNOWLEDGE_REFERENCES
# ============================================================

KNOWLEDGE_REFERENCES = [
    {"node_id": "hsv-000", "book": "肘井の読解のための英文法", "section_id": "Hij_00", "pages": "p.8-9"},
    {"node_id": "hsv-001", "book": "肘井の読解のための英文法", "section_id": "Hij_01_1", "pages": "p.12-14"},
    {"node_id": "hsv-002", "book": "肘井の読解のための英文法", "section_id": "Hij_01_1", "pages": "p.15"},
    {"node_id": "hsv-003", "book": "肘井の読解のための英文法", "section_id": "Hij_01_1", "pages": "p.16"},
    {"node_id": "hsv-004", "book": "肘井の読解のための英文法", "section_id": "Hij_01_2", "pages": "p.18-22"},
]

# ============================================================
# 6. SECTIONS
# ============================================================

SECTIONS = [
    {
        "id": "Hij_00",
        "book": "肘井の読解のための英文法",
        "title": "本編に入る前に",
        "pages": "p.8-9",
        "type": "introduction",
    },
    {
        "id": "Hij_01_1",
        "book": "肘井の読解のための英文法",
        "title": "Theme 01 SVの発見で英文が読める①",
        "pages": "p.12-17",
        "type": "drill",
    },
    {
        "id": "Hij_01_2",
        "book": "肘井の読解のための英文法",
        "title": "Theme 01 SVの発見で英文が読める②",
        "pages": "p.18-23",
        "type": "drill",
    },
]

# ============================================================
# 7. SECTION_PREREQUISITES
# ============================================================

SECTION_PREREQUISITES = [
    {"section_id": "Hij_01_1", "prerequisite_id": "Hij_00"},
    {"section_id": "Hij_01_2", "prerequisite_id": "Hij_01_1"},
]

# ============================================================
# 8. SECTION_KNOWLEDGE_NODES
# ============================================================

SECTION_KNOWLEDGE_NODES = [
    {"section_id": "Hij_00", "node_id": "hsv-000", "seq": 1},
    {"section_id": "Hij_01_1", "node_id": "hsv-001", "seq": 1},
    {"section_id": "Hij_01_1", "node_id": "hsv-002", "seq": 2},
    {"section_id": "Hij_01_1", "node_id": "hsv-003", "seq": 3},
    {"section_id": "Hij_01_2", "node_id": "hsv-004", "seq": 1},
]

# ============================================================
# 9. SENTENCES
# ============================================================

SENTENCES = [
    # ----------------------------------------------------------
    # Hij_01_1 — 例題 (5問)
    # ----------------------------------------------------------
    {
        "id": "hij-01-e1-01",
        "section_id": "Hij_01_1",
        "drill": 1,
        "number": 1,
        "role": "example",
        "english": "That he ate ten hamburgers surprised me.",
        "japanese": "彼が10個のハンバーガーを食べたことが、私を驚かせた。",
        "notes": None,
    },
    {
        "id": "hij-01-e1-02",
        "section_id": "Hij_01_1",
        "drill": 1,
        "number": 2,
        "role": "example",
        "english": "How we view things is affected by our knowledge.",
        "japanese": "私たちがどのようにものごとを見るかは、知識に影響を受けている。",
        "notes": None,
    },
    {
        "id": "hij-01-e1-03",
        "section_id": "Hij_01_1",
        "drill": 1,
        "number": 3,
        "role": "example",
        "english": "What is important to you is also important to me.",
        "japanese": "あなたにとって重要なことは、私にとっても重要だ。",
        "notes": None,
    },
    {
        "id": "hij-01-e1-04",
        "section_id": "Hij_01_1",
        "drill": 1,
        "number": 4,
        "role": "example",
        "english": "A rainbow observed by the woman was round.",
        "japanese": "その女性が観察した虹は、丸かった。",
        "notes": None,
    },
    {
        "id": "hij-01-e1-05",
        "section_id": "Hij_01_1",
        "drill": 1,
        "number": 5,
        "role": "example",
        "english": "The world we live in has changed in recent years.",
        "japanese": "私たちが暮らす世の中は、近年変化してきた。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_01_1 — 確認問題 (3問)
    # ----------------------------------------------------------
    {
        "id": "hij-01-c1-01",
        "section_id": "Hij_01_1",
        "drill": 2,
        "number": 1,
        "role": "practice",
        "english": "The book I need is not in the library.",
        "japanese": "私が必要とする本は、その図書館にはない。",
        "notes": None,
    },
    {
        "id": "hij-01-c1-02",
        "section_id": "Hij_01_1",
        "drill": 2,
        "number": 2,
        "role": "practice",
        "english": "What you have achieved is wonderful.",
        "japanese": "あなたが成し遂げたことはすばらしい。",
        "notes": None,
    },
    {
        "id": "hij-01-c1-03",
        "section_id": "Hij_01_1",
        "drill": 2,
        "number": 3,
        "role": "practice",
        "english": "Money paid for the chocolate went to cocoa farmers.",
        "japanese": "そのチョコレートに支払われたお金は、カカオ農家のもとへと行っていた。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_01_1 — 発展問題 (1問)
    # ----------------------------------------------------------
    {
        "id": "hij-01-a1-01",
        "section_id": "Hij_01_1",
        "drill": 3,
        "number": 1,
        "role": "advanced",
        "english": "That the structure of society is key to health becomes clear.",
        "japanese": "社会構造が健康につながる重要な要素なのは、明らかになっている。",
        "notes": "学習院大／改",
    },
    # ----------------------------------------------------------
    # Hij_01_2 — 例題 (5問)
    # ----------------------------------------------------------
    {
        "id": "hij-01-e4-01",
        "section_id": "Hij_01_2",
        "drill": 1,
        "number": 1,
        "role": "example",
        "english": "Thanks to vacuum cleaners homes are cleaner.",
        "japanese": "掃除機のおかげで、家はよりきれいになる。",
        "notes": None,
    },
    {
        "id": "hij-01-e4-02",
        "section_id": "Hij_01_2",
        "drill": 1,
        "number": 2,
        "role": "example",
        "english": "Many students from all over the world came together.",
        "japanese": "世界中から多くの生徒が集まってきた。",
        "notes": None,
    },
    {
        "id": "hij-01-e4-03",
        "section_id": "Hij_01_2",
        "drill": 1,
        "number": 3,
        "role": "example",
        "english": "The man sitting in the corner is my father.",
        "japanese": "すみに座っている人は、私の父だ。",
        "notes": None,
    },
    {
        "id": "hij-01-e4-04",
        "section_id": "Hij_01_2",
        "drill": 1,
        "number": 4,
        "role": "example",
        "english": "The topic to be discussed at the meeting is difficult.",
        "japanese": "その会議で議論される話題は、難しい。",
        "notes": None,
    },
    {
        "id": "hij-01-e4-05",
        "section_id": "Hij_01_2",
        "drill": 1,
        "number": 5,
        "role": "example",
        "english": "He said in the interview that he loved his wife.",
        "japanese": "彼は会見で、妻を愛していると言った。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_01_2 — 確認問題 (3問)
    # ----------------------------------------------------------
    {
        "id": "hij-01-c2-01",
        "section_id": "Hij_01_2",
        "drill": 2,
        "number": 1,
        "role": "practice",
        "english": "In the Middle Ages the young had difficulty finding work.",
        "japanese": "中世では、若者は仕事を見つけるのに苦労していた。",
        "notes": None,
    },
    {
        "id": "hij-01-c2-02",
        "section_id": "Hij_01_2",
        "drill": 2,
        "number": 2,
        "role": "practice",
        "english": "The country with the largest population is China.",
        "japanese": "人口が最も多い国は中国だ。",
        "notes": None,
    },
    {
        "id": "hij-01-c2-03",
        "section_id": "Hij_01_2",
        "drill": 2,
        "number": 3,
        "role": "practice",
        "english": "They have to take into account the effects of education.",
        "japanese": "その人たちは、教育の影響を考慮に入れなければならない。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_01_2 — 発展問題 (1問)
    # ----------------------------------------------------------
    {
        "id": "hij-01-a2-01",
        "section_id": "Hij_01_2",
        "drill": 3,
        "number": 1,
        "role": "advanced",
        "english": "We learn from a young age what food communicates in our particular culture or family.",
        "japanese": "私たちは幼いころから、私たちの特定の文化や家族のなかで、食べ物が伝えるものを学ぶ。",
        "notes": "富山大",
    },
]

# ============================================================
# 10. SENTENCE_STRUCTURES
# ============================================================

SENTENCE_STRUCTURES = [
    # --- hij-01-e1-01 ---
    {"sentence_id": "hij-01-e1-01", "label": "overall", "value": "S V O"},
    {"sentence_id": "hij-01-e1-01", "label": "details", "value": "<That he ate ten hamburgers>(S:名詞節) surprised(V) me(O)"},
    # --- hij-01-e1-02 ---
    {"sentence_id": "hij-01-e1-02", "label": "overall", "value": "S V M"},
    {"sentence_id": "hij-01-e1-02", "label": "details", "value": "<How we view things>(S:名詞節) is affected(V) [by our knowledge](M)"},
    # --- hij-01-e1-03 ---
    {"sentence_id": "hij-01-e1-03", "label": "overall", "value": "S V M C M"},
    {"sentence_id": "hij-01-e1-03", "label": "details", "value": "<What is important to you>(S:名詞節) is(V) <also>(M) important(C) [to me](M)"},
    # --- hij-01-e1-04 ---
    {"sentence_id": "hij-01-e1-04", "label": "overall", "value": "S (M) V C"},
    {"sentence_id": "hij-01-e1-04", "label": "details", "value": "A rainbow(S) (observed by the woman)(M:形容詞句) was(V) round(C)"},
    # --- hij-01-e1-05 ---
    {"sentence_id": "hij-01-e1-05", "label": "overall", "value": "S (M) V M"},
    {"sentence_id": "hij-01-e1-05", "label": "details", "value": "The world(S) (we live in)(M:関係代名詞省略) has changed(V) [in recent years](M)"},
    # --- hij-01-c1-01 ---
    {"sentence_id": "hij-01-c1-01", "label": "overall", "value": "S (M) V M"},
    {"sentence_id": "hij-01-c1-01", "label": "details", "value": "The book(S) (I need)(M:関係代名詞省略) is not(V) [in the library](M)"},
    # --- hij-01-c1-02 ---
    {"sentence_id": "hij-01-c1-02", "label": "overall", "value": "S V C"},
    {"sentence_id": "hij-01-c1-02", "label": "details", "value": "<What you have achieved>(S:名詞節) is(V) wonderful(C)"},
    # --- hij-01-c1-03 ---
    {"sentence_id": "hij-01-c1-03", "label": "overall", "value": "S (M) V M"},
    {"sentence_id": "hij-01-c1-03", "label": "details", "value": "Money(S) (paid for the chocolate)(M:形容詞句) went(V) [to cocoa farmers](M)"},
    # --- hij-01-a1-01 ---
    {"sentence_id": "hij-01-a1-01", "label": "overall", "value": "S V C"},
    {"sentence_id": "hij-01-a1-01", "label": "details", "value": "<That the structure of society is key to health>(S:名詞節) becomes(V) clear(C)"},
    # --- hij-01-e4-01 ---
    {"sentence_id": "hij-01-e4-01", "label": "overall", "value": "M S V C"},
    {"sentence_id": "hij-01-e4-01", "label": "details", "value": "[Thanks to vacuum cleaners](M:群前置詞) homes(S) are(V) cleaner(C)"},
    # --- hij-01-e4-02 ---
    {"sentence_id": "hij-01-e4-02", "label": "overall", "value": "S (M) V"},
    {"sentence_id": "hij-01-e4-02", "label": "details", "value": "Many students(S) (from all over the world)(M:前置詞句) came together(V)"},
    # --- hij-01-e4-03 ---
    {"sentence_id": "hij-01-e4-03", "label": "overall", "value": "S (M) V C"},
    {"sentence_id": "hij-01-e4-03", "label": "details", "value": "The man(S) (sitting in the corner)(M:現在分詞句) is(V) my father(C)"},
    # --- hij-01-e4-04 ---
    {"sentence_id": "hij-01-e4-04", "label": "overall", "value": "S (M) V C"},
    {"sentence_id": "hij-01-e4-04", "label": "details", "value": "The topic(S) (to be discussed at the meeting)(M:不定詞句) is(V) difficult(C)"},
    # --- hij-01-e4-05 ---
    {"sentence_id": "hij-01-e4-05", "label": "overall", "value": "S V M O"},
    {"sentence_id": "hij-01-e4-05", "label": "details", "value": "He(S) said(V) [in the interview](M) <that he loved his wife>(O:名詞節)"},
    # --- hij-01-c2-01 ---
    {"sentence_id": "hij-01-c2-01", "label": "overall", "value": "M S V O M"},
    {"sentence_id": "hij-01-c2-01", "label": "details", "value": "[In the Middle Ages](M) the young(S) had(V) difficulty(O) [finding work](M)"},
    # --- hij-01-c2-02 ---
    {"sentence_id": "hij-01-c2-02", "label": "overall", "value": "S (M) V C"},
    {"sentence_id": "hij-01-c2-02", "label": "details", "value": "The country(S) (with the largest population)(M:前置詞句) is(V) China(C)"},
    # --- hij-01-c2-03 ---
    {"sentence_id": "hij-01-c2-03", "label": "overall", "value": "S V M O"},
    {"sentence_id": "hij-01-c2-03", "label": "details", "value": "They(S) have to take(V) [into account](M) the effects of education(O)"},
    # --- hij-01-a2-01 ---
    {"sentence_id": "hij-01-a2-01", "label": "overall", "value": "S V M O"},
    {"sentence_id": "hij-01-a2-01", "label": "details", "value": "We(S) learn(V) [from a young age](M) <what food communicates in our particular culture or family>(O:名詞節)"},
]

# ============================================================
# 11. SENTENCE_KNOWLEDGE_TAGS
# ============================================================

SENTENCE_KNOWLEDGE_TAGS = [
    # --- Hij_01_1 例題 ---
    {"sentence_id": "hij-01-e1-01", "node_id": "hsv-001"},
    {"sentence_id": "hij-01-e1-02", "node_id": "hsv-001"},
    {"sentence_id": "hij-01-e1-03", "node_id": "hsv-001"},
    {"sentence_id": "hij-01-e1-04", "node_id": "hsv-002"},
    {"sentence_id": "hij-01-e1-05", "node_id": "hsv-003"},
    # --- Hij_01_1 確認問題 ---
    {"sentence_id": "hij-01-c1-01", "node_id": "hsv-003"},
    {"sentence_id": "hij-01-c1-02", "node_id": "hsv-001"},
    {"sentence_id": "hij-01-c1-03", "node_id": "hsv-002"},
    # --- Hij_01_1 発展問題 ---
    {"sentence_id": "hij-01-a1-01", "node_id": "hsv-001"},
    # --- Hij_01_2 例題 ---
    {"sentence_id": "hij-01-e4-01", "node_id": "hsv-004"},
    {"sentence_id": "hij-01-e4-02", "node_id": "hsv-004"},
    {"sentence_id": "hij-01-e4-03", "node_id": "hsv-004"},
    {"sentence_id": "hij-01-e4-04", "node_id": "hsv-004"},
    {"sentence_id": "hij-01-e4-05", "node_id": "hsv-004"},
    # --- Hij_01_2 確認問題 ---
    {"sentence_id": "hij-01-c2-01", "node_id": "hsv-004"},
    {"sentence_id": "hij-01-c2-02", "node_id": "hsv-004"},
    {"sentence_id": "hij-01-c2-03", "node_id": "hsv-004"},
    # --- Hij_01_2 発展問題 ---
    {"sentence_id": "hij-01-a2-01", "node_id": "hsv-004"},
]
