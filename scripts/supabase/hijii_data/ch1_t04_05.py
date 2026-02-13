"""第1章: 意味のカタマリ編 Theme 04-05（形容詞句・形容詞節）"""

# ============================================================
# 1. KNOWLEDGE_NODES
# ============================================================

KNOWLEDGE_NODES = [
    {
        "id": "hch-003",
        "name": "形容詞句（前置詞・不定詞・分詞による後置修飾）",
        "category": "意味のカタマリ",
        "priority": "P1",
        "notes": "2語以上からなるSVのない形容詞のカタマリ（形容詞句）が前の名詞を修飾するパターン。(1)前置詞句の後置修飾、(2)不定詞の形容詞的用法（名詞とSV・VO・同格の3関係）、(3)分詞の形容詞用法（現在分詞「～している」/過去分詞「～された」）の3パターン。「句のなかにSVは入らない」を根拠にカタマリの範囲を確定する。",
    },
    {
        "id": "hch-004",
        "name": "形容詞節（関係代名詞・前置詞+関係代名詞・関係副詞）",
        "category": "意味のカタマリ",
        "priority": "P1",
        "notes": "2語以上からなるSVのある形容詞のカタマリ（形容詞節）が前の名詞を修飾するパターン。(1)関係代名詞（who/which/that/whose）、(2)前置詞+関係代名詞（in which/of whom/by which等）、(3)関係副詞（when/where/why/how）の3パターン。「1つの節にSVは1つ」を根拠に2個目の動詞の手前でカタマリの範囲を確定する。形容詞句との違いはSVがあること。",
    },
]

# ============================================================
# 2. UNDERSTANDING_GOALS
# ============================================================

UNDERSTANDING_GOALS = [
    # hch-003
    {"node_id": "hch-003", "seq": 1, "goal": "形容詞句の3パターン（前置詞句・不定詞の形容詞的用法・分詞の形容詞用法）を列挙できる"},
    {"node_id": "hch-003", "seq": 2, "goal": "「句のなかにSVは入らない」を根拠に形容詞句の範囲を確定できる"},
    {"node_id": "hch-003", "seq": 3, "goal": "不定詞の形容詞的用法で、修飾する名詞とto doの間にSV・VO・同格の3つの関係があることを説明できる"},
    {"node_id": "hch-003", "seq": 4, "goal": "現在分詞（～している/能動）と過去分詞（～された/受動）が形容詞句をつくって前の名詞を修飾するパターンを識別できる"},
    {"node_id": "hch-003", "seq": 5, "goal": "形容詞句の範囲を（ ）で括り、修飾先の名詞を特定できる"},
    # hch-004
    {"node_id": "hch-004", "seq": 1, "goal": "形容詞節の3パターン（関係代名詞・前置詞+関係代名詞・関係副詞）を列挙できる"},
    {"node_id": "hch-004", "seq": 2, "goal": "「1つの節にSVは1つ」を根拠に、2個目の動詞の手前で形容詞節の範囲を確定できる"},
    {"node_id": "hch-004", "seq": 3, "goal": "前置詞+関係代名詞（in which, of whom, by which等）は前置詞から形容詞節が始まることを理解している"},
    {"node_id": "hch-004", "seq": 4, "goal": "関係代名詞・関係副詞自体は訳さず、形容詞節の範囲を（ ）で括り修飾先の名詞を特定できる"},
    {"node_id": "hch-004", "seq": 5, "goal": "形容詞句（SVなし）と形容詞節（SVあり）の違いを説明できる"},
]

# ============================================================
# 3. CHECK_POINTS
# ============================================================

CHECK_POINTS = [
    # hch-003
    {"node_id": "hch-003", "seq": 1, "question": "形容詞句の3パターンは何か？", "answer": "(1)前置詞句の後置修飾、(2)不定詞の形容詞的用法、(3)分詞の形容詞用法（現在分詞・過去分詞）。"},
    {"node_id": "hch-003", "seq": 2, "question": "形容詞句の範囲を確定する根拠は？", "answer": "「句のなかにSVは入らない」こと。動詞の手前で形容詞句が終わる。"},
    {"node_id": "hch-003", "seq": 3, "question": "不定詞の形容詞的用法で、修飾する名詞とto doの関係は何通りあるか？", "answer": "3通り。(1)SV関係、(2)VO関係、(3)同格関係。"},
    {"node_id": "hch-003", "seq": 4, "question": "現在分詞と過去分詞の形容詞用法の意味の違いは？", "answer": "現在分詞は「～している」（能動）、過去分詞は「～された」（受動）。"},
    # hch-004
    {"node_id": "hch-004", "seq": 1, "question": "形容詞節の3パターンは何か？", "answer": "(1)関係代名詞、(2)前置詞+関係代名詞、(3)関係副詞。"},
    {"node_id": "hch-004", "seq": 2, "question": "形容詞節の範囲を確定する根拠は？", "answer": "「1つの節にSVは1つ」なので、2個目の動詞の手前で形容詞節が終わる。"},
    {"node_id": "hch-004", "seq": 3, "question": "前置詞+関係代名詞では、形容詞節はどこから始まるか？", "answer": "前置詞から始まる。例: in whichならinから形容詞節が始まる。"},
    {"node_id": "hch-004", "seq": 4, "question": "形容詞句と形容詞節の違いは？", "answer": "形容詞句はSVの文構造がない形容詞のカタマリ、形容詞節はSVの文構造がある形容詞のカタマリ。"},
]

# ============================================================
# 4. NODE_PREREQUISITES
# ============================================================

NODE_PREREQUISITES = [
    {"node_id": "hch-004", "prerequisite_id": "hch-003"},
]

# ============================================================
# 5. KNOWLEDGE_REFERENCES
# ============================================================

KNOWLEDGE_REFERENCES = [
    {"node_id": "hch-003", "book": "肘井の読解のための英文法", "section_id": "Hij_04", "pages": "p.38-43"},
    {"node_id": "hch-004", "book": "肘井の読解のための英文法", "section_id": "Hij_05", "pages": "p.44-47"},
]

# ============================================================
# 6. SECTIONS
# ============================================================

SECTIONS = [
    {
        "id": "Hij_04",
        "book": "肘井の読解のための英文法",
        "title": "Theme 04 形容詞句で英文が読める",
        "pages": "p.38-43",
        "type": "drill",
    },
    {
        "id": "Hij_05",
        "book": "肘井の読解のための英文法",
        "title": "Theme 05 形容詞節で英文が読める",
        "pages": "p.44-47",
        "type": "drill",
    },
]

# ============================================================
# 7. SECTION_PREREQUISITES
# ============================================================

SECTION_PREREQUISITES = [
    {"section_id": "Hij_05", "prerequisite_id": "Hij_04"},
]

# ============================================================
# 8. SECTION_KNOWLEDGE_NODES
# ============================================================

SECTION_KNOWLEDGE_NODES = [
    {"section_id": "Hij_04", "node_id": "hch-003", "seq": 1},
    {"section_id": "Hij_05", "node_id": "hch-004", "seq": 1},
]

# ============================================================
# 9. SENTENCES
# ============================================================

SENTENCES = [
    # ----------------------------------------------------------
    # Hij_04 -- 例題 (6問)
    # ----------------------------------------------------------
    {
        "id": "hij-04-e1-01",
        "section_id": "Hij_04",
        "drill": 1,
        "number": 1,
        "role": "example",
        "english": "The gap between ideal and reality has created pain.",
        "japanese": "理想と現実の間のギャップが、苦しみをつくり出してきた。",
        "notes": None,
    },
    {
        "id": "hij-04-e1-02",
        "section_id": "Hij_04",
        "drill": 1,
        "number": 2,
        "role": "example",
        "english": "He is the first person to study viruses.",
        "japanese": "彼がウイルスを研究した最初の人だ。",
        "notes": None,
    },
    {
        "id": "hij-04-e1-03",
        "section_id": "Hij_04",
        "drill": 1,
        "number": 3,
        "role": "example",
        "english": "I have no friends to talk to in English.",
        "japanese": "私には、英語で話す友人が一人もいない。",
        "notes": None,
    },
    {
        "id": "hij-04-e1-04",
        "section_id": "Hij_04",
        "drill": 1,
        "number": 4,
        "role": "example",
        "english": "The student has the ability to get better grades.",
        "japanese": "その生徒は、もっとよい成績をとる能力がある。",
        "notes": None,
    },
    {
        "id": "hij-04-e1-05",
        "section_id": "Hij_04",
        "drill": 1,
        "number": 5,
        "role": "example",
        "english": "The man standing by the wall is a famous actor.",
        "japanese": "壁のそばに立っている人は、有名な俳優だ。",
        "notes": None,
    },
    {
        "id": "hij-04-e1-06",
        "section_id": "Hij_04",
        "drill": 1,
        "number": 6,
        "role": "example",
        "english": "Fruits sold in the supermarket are often frozen.",
        "japanese": "スーパーマーケットで売られているフルーツは、凍っていることが多い。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_04 -- ポイント9 例文 (3問)
    # ----------------------------------------------------------
    {
        "id": "hij-04-e1-07",
        "section_id": "Hij_04",
        "drill": 1,
        "number": 7,
        "role": "example",
        "english": "I have a family to look after me.",
        "japanese": "私には、自分を世話してくれる家族がいる。",
        "notes": "ポイント9 例文1: 不定詞の形容詞的用法（SV関係）",
    },
    {
        "id": "hij-04-e1-08",
        "section_id": "Hij_04",
        "drill": 1,
        "number": 8,
        "role": "example",
        "english": "I have a family to look after.",
        "japanese": "私には、（自分が）世話をすべき家族がいる。",
        "notes": "ポイント9 例文2: 不定詞の形容詞的用法（VO関係）",
    },
    {
        "id": "hij-04-e1-09",
        "section_id": "Hij_04",
        "drill": 1,
        "number": 9,
        "role": "example",
        "english": "I have the ability to speak French fluently.",
        "japanese": "私は、フランス語を流ちょうに話す能力がある。",
        "notes": "ポイント9 例文3: 不定詞の形容詞的用法（同格関係）",
    },
    # ----------------------------------------------------------
    # Hij_04 -- 確認問題 (4問)
    # ----------------------------------------------------------
    {
        "id": "hij-04-c1-01",
        "section_id": "Hij_04",
        "drill": 2,
        "number": 1,
        "role": "practice",
        "english": "Five members of the crew were killed.",
        "japanese": "乗組員のうち5人が亡くなった。",
        "notes": None,
    },
    {
        "id": "hij-04-c1-02",
        "section_id": "Hij_04",
        "drill": 2,
        "number": 2,
        "role": "practice",
        "english": "The girl wearing the blue jeans is my sister.",
        "japanese": "青いジーンズをはいている少女は私の妹（姉）です。",
        "notes": None,
    },
    {
        "id": "hij-04-c1-03",
        "section_id": "Hij_04",
        "drill": 2,
        "number": 3,
        "role": "practice",
        "english": "His ambition to become a lawyer is wonderful.",
        "japanese": "彼の法律家になるという大志は、すばらしい。",
        "notes": None,
    },
    {
        "id": "hij-04-c1-04",
        "section_id": "Hij_04",
        "drill": 2,
        "number": 4,
        "role": "practice",
        "english": "The tests given to them were very easy.",
        "japanese": "その人たちに与えられたテストはとても簡単だった。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_04 -- 発展問題 (1問)
    # ----------------------------------------------------------
    {
        "id": "hij-04-a1-01",
        "section_id": "Hij_04",
        "drill": 3,
        "number": 1,
        "role": "advanced",
        "english": "The crop produced in one part of a field can be three times that of another.",
        "japanese": "畑のある場所で生み出された作物が、別の場所の作物の3倍になることがある。",
        "notes": "東京大",
    },
    # ----------------------------------------------------------
    # Hij_05 -- 例題 (5問)
    # ----------------------------------------------------------
    {
        "id": "hij-05-e1-01",
        "section_id": "Hij_05",
        "drill": 1,
        "number": 1,
        "role": "example",
        "english": "The woman who entered the room was my mother.",
        "japanese": "その部屋に入った女性は、私の母だった。",
        "notes": None,
    },
    {
        "id": "hij-05-e1-02",
        "section_id": "Hij_05",
        "drill": 1,
        "number": 2,
        "role": "example",
        "english": "I can't find the bag in which I put my wallet.",
        "japanese": "財布を入れたバッグが見つからない。",
        "notes": None,
    },
    {
        "id": "hij-05-e1-03",
        "section_id": "Hij_05",
        "drill": 1,
        "number": 3,
        "role": "example",
        "english": "She is married to an actor of whom you have heard.",
        "japanese": "彼女は、あなたが聞いたことがある俳優と結婚している。",
        "notes": None,
    },
    {
        "id": "hij-05-e1-04",
        "section_id": "Hij_05",
        "drill": 1,
        "number": 4,
        "role": "example",
        "english": "E-mail is a convenient way by which we communicate.",
        "japanese": "Eメールは、意思疎通する便利な方法だ。",
        "notes": None,
    },
    {
        "id": "hij-05-e1-05",
        "section_id": "Hij_05",
        "drill": 1,
        "number": 5,
        "role": "example",
        "english": "I can remember the time when phones were still rare.",
        "japanese": "私は電話がまだ珍しかった時代を、思い出すことができる。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_05 -- 確認問題 (3問)
    # ----------------------------------------------------------
    {
        "id": "hij-05-c1-01",
        "section_id": "Hij_05",
        "drill": 2,
        "number": 1,
        "role": "practice",
        "english": "Many people who make the trip to Japan are surprised at the friendliness of the people.",
        "japanese": "日本に旅行する多くの人が、日本人が友好的であると驚いている。",
        "notes": None,
    },
    {
        "id": "hij-05-c1-02",
        "section_id": "Hij_05",
        "drill": 2,
        "number": 2,
        "role": "practice",
        "english": "The police measured the speed at which the car was traveling.",
        "japanese": "警察は、その車が移動しているスピードを計測した。",
        "notes": None,
    },
    {
        "id": "hij-05-c1-03",
        "section_id": "Hij_05",
        "drill": 2,
        "number": 3,
        "role": "practice",
        "english": "A lawyer is a person whose business is to advise people about laws.",
        "japanese": "法律家は、人びとに法律について助言することを仕事とする人だ。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_05 -- 発展問題 (1問)
    # ----------------------------------------------------------
    {
        "id": "hij-05-a1-01",
        "section_id": "Hij_05",
        "drill": 3,
        "number": 1,
        "role": "advanced",
        "english": "There are times when I'll say something that I think is standard Japanese, only to have someone express their surprise at my use of Osaka-ben.",
        "japanese": "私が標準語だと思って言っているのに、私が大阪弁を使ったことに驚いたと人に言われるときがある。",
        "notes": "高知大",
    },
]

# ============================================================
# 10. SENTENCE_STRUCTURES
# ============================================================

SENTENCE_STRUCTURES = [
    # --- hij-04-e1-01 ---
    {"sentence_id": "hij-04-e1-01", "label": "overall", "value": "S (M) V O"},
    {"sentence_id": "hij-04-e1-01", "label": "details", "value": "The gap(S) (between ideal and reality)(M:前置詞句) has created(V) pain(O)"},
    # --- hij-04-e1-02 ---
    {"sentence_id": "hij-04-e1-02", "label": "overall", "value": "S V C (M)"},
    {"sentence_id": "hij-04-e1-02", "label": "details", "value": "He(S) is(V) the first person(C) (to study viruses)(M:不定詞の形容詞的用法/SV関係)"},
    # --- hij-04-e1-03 ---
    {"sentence_id": "hij-04-e1-03", "label": "overall", "value": "S V O (M)"},
    {"sentence_id": "hij-04-e1-03", "label": "details", "value": "I(S) have(V) no friends(O) (to talk to in English)(M:不定詞の形容詞的用法/VO関係)"},
    # --- hij-04-e1-04 ---
    {"sentence_id": "hij-04-e1-04", "label": "overall", "value": "S V O (M)"},
    {"sentence_id": "hij-04-e1-04", "label": "details", "value": "The student(S) has(V) the ability(O) (to get better grades)(M:不定詞の形容詞的用法/同格関係)"},
    # --- hij-04-e1-05 ---
    {"sentence_id": "hij-04-e1-05", "label": "overall", "value": "S (M) V C"},
    {"sentence_id": "hij-04-e1-05", "label": "details", "value": "The man(S) (standing by the wall)(M:現在分詞句) is(V) a famous actor(C)"},
    # --- hij-04-e1-06 ---
    {"sentence_id": "hij-04-e1-06", "label": "overall", "value": "S (M) V M C"},
    {"sentence_id": "hij-04-e1-06", "label": "details", "value": "Fruits(S) (sold in the supermarket)(M:過去分詞句) are(V) often(M) frozen(C)"},
    # --- hij-04-e1-07 ---
    {"sentence_id": "hij-04-e1-07", "label": "overall", "value": "S V O (M)"},
    {"sentence_id": "hij-04-e1-07", "label": "details", "value": "I(S) have(V) a family(O) (to look after me)(M:不定詞の形容詞的用法/SV関係)"},
    # --- hij-04-e1-08 ---
    {"sentence_id": "hij-04-e1-08", "label": "overall", "value": "S V O (M)"},
    {"sentence_id": "hij-04-e1-08", "label": "details", "value": "I(S) have(V) a family(O) (to look after)(M:不定詞の形容詞的用法/VO関係)"},
    # --- hij-04-e1-09 ---
    {"sentence_id": "hij-04-e1-09", "label": "overall", "value": "S V O (M)"},
    {"sentence_id": "hij-04-e1-09", "label": "details", "value": "I(S) have(V) the ability(O) (to speak French fluently)(M:不定詞の形容詞的用法/同格関係)"},
    # --- hij-04-c1-01 ---
    {"sentence_id": "hij-04-c1-01", "label": "overall", "value": "S (M) V"},
    {"sentence_id": "hij-04-c1-01", "label": "details", "value": "Five members(S) (of the crew)(M:前置詞句) were killed(V)"},
    # --- hij-04-c1-02 ---
    {"sentence_id": "hij-04-c1-02", "label": "overall", "value": "S (M) V C"},
    {"sentence_id": "hij-04-c1-02", "label": "details", "value": "The girl(S) (wearing the blue jeans)(M:現在分詞句) is(V) my sister(C)"},
    # --- hij-04-c1-03 ---
    {"sentence_id": "hij-04-c1-03", "label": "overall", "value": "S (M) V C"},
    {"sentence_id": "hij-04-c1-03", "label": "details", "value": "His ambition(S) (to become a lawyer)(M:不定詞の形容詞的用法/同格関係) is(V) wonderful(C)"},
    # --- hij-04-c1-04 ---
    {"sentence_id": "hij-04-c1-04", "label": "overall", "value": "S (M) V M C"},
    {"sentence_id": "hij-04-c1-04", "label": "details", "value": "The tests(S) (given to them)(M:過去分詞句) were(V) very(M) easy(C)"},
    # --- hij-04-a1-01 ---
    {"sentence_id": "hij-04-a1-01", "label": "overall", "value": "S (M) V C"},
    {"sentence_id": "hij-04-a1-01", "label": "details", "value": "The crop(S) (produced in one part of a field)(M:過去分詞句) can be(V) three times that of another(C)"},
    # --- hij-05-e1-01 ---
    {"sentence_id": "hij-05-e1-01", "label": "overall", "value": "S (M) V C"},
    {"sentence_id": "hij-05-e1-01", "label": "details", "value": "The woman(S) (who entered the room)(M:関係代名詞節) was(V) my mother(C)"},
    # --- hij-05-e1-02 ---
    {"sentence_id": "hij-05-e1-02", "label": "overall", "value": "S V O (M)"},
    {"sentence_id": "hij-05-e1-02", "label": "details", "value": "I(S) can't find(V) the bag(O) (in which I put my wallet)(M:前置詞+関係代名詞節)"},
    # --- hij-05-e1-03 ---
    {"sentence_id": "hij-05-e1-03", "label": "overall", "value": "S V M O (M)"},
    {"sentence_id": "hij-05-e1-03", "label": "details", "value": "She(S) is married(V) [to](M) an actor(O) (of whom you have heard)(M:前置詞+関係代名詞節)"},
    # --- hij-05-e1-04 ---
    {"sentence_id": "hij-05-e1-04", "label": "overall", "value": "S V C (M)"},
    {"sentence_id": "hij-05-e1-04", "label": "details", "value": "E-mail(S) is(V) a convenient way(C) (by which we communicate)(M:前置詞+関係代名詞節)"},
    # --- hij-05-e1-05 ---
    {"sentence_id": "hij-05-e1-05", "label": "overall", "value": "S V O (M)"},
    {"sentence_id": "hij-05-e1-05", "label": "details", "value": "I(S) can remember(V) the time(O) (when phones were still rare)(M:関係副詞節)"},
    # --- hij-05-c1-01 ---
    {"sentence_id": "hij-05-c1-01", "label": "overall", "value": "S (M) V M"},
    {"sentence_id": "hij-05-c1-01", "label": "details", "value": "Many people(S) (who make the trip to Japan)(M:関係代名詞節) are surprised(V) [at the friendliness of the people](M)"},
    # --- hij-05-c1-02 ---
    {"sentence_id": "hij-05-c1-02", "label": "overall", "value": "S V O (M)"},
    {"sentence_id": "hij-05-c1-02", "label": "details", "value": "The police(S) measured(V) the speed(O) (at which the car was traveling)(M:前置詞+関係代名詞節)"},
    # --- hij-05-c1-03 ---
    {"sentence_id": "hij-05-c1-03", "label": "overall", "value": "S V C (M)"},
    {"sentence_id": "hij-05-c1-03", "label": "details", "value": "A lawyer(S) is(V) a person(C) (whose business is to advise people about laws)(M:関係代名詞節)"},
    # --- hij-05-a1-01 ---
    {"sentence_id": "hij-05-a1-01", "label": "overall", "value": "M V S (M)"},
    {"sentence_id": "hij-05-a1-01", "label": "details", "value": "There(M) are(V) times(S) (when I'll say something (that I think is standard Japanese))(M:関係副詞節+関係代名詞節), [only to have someone express their surprise at my use of Osaka-ben](M:不定詞の副詞的用法/結果)"},
]

# ============================================================
# 11. SENTENCE_KNOWLEDGE_TAGS
# ============================================================

SENTENCE_KNOWLEDGE_TAGS = [
    # --- Hij_04 例題 ---
    {"sentence_id": "hij-04-e1-01", "node_id": "hch-003"},
    {"sentence_id": "hij-04-e1-02", "node_id": "hch-003"},
    {"sentence_id": "hij-04-e1-03", "node_id": "hch-003"},
    {"sentence_id": "hij-04-e1-04", "node_id": "hch-003"},
    {"sentence_id": "hij-04-e1-05", "node_id": "hch-003"},
    {"sentence_id": "hij-04-e1-06", "node_id": "hch-003"},
    # --- Hij_04 ポイント9 例文 ---
    {"sentence_id": "hij-04-e1-07", "node_id": "hch-003"},
    {"sentence_id": "hij-04-e1-08", "node_id": "hch-003"},
    {"sentence_id": "hij-04-e1-09", "node_id": "hch-003"},
    # --- Hij_04 確認問題 ---
    {"sentence_id": "hij-04-c1-01", "node_id": "hch-003"},
    {"sentence_id": "hij-04-c1-02", "node_id": "hch-003"},
    {"sentence_id": "hij-04-c1-03", "node_id": "hch-003"},
    {"sentence_id": "hij-04-c1-04", "node_id": "hch-003"},
    # --- Hij_04 発展問題 ---
    {"sentence_id": "hij-04-a1-01", "node_id": "hch-003"},
    # --- Hij_05 例題 ---
    {"sentence_id": "hij-05-e1-01", "node_id": "hch-004"},
    {"sentence_id": "hij-05-e1-02", "node_id": "hch-004"},
    {"sentence_id": "hij-05-e1-03", "node_id": "hch-004"},
    {"sentence_id": "hij-05-e1-04", "node_id": "hch-004"},
    {"sentence_id": "hij-05-e1-05", "node_id": "hch-004"},
    # --- Hij_05 確認問題 ---
    {"sentence_id": "hij-05-c1-01", "node_id": "hch-004"},
    {"sentence_id": "hij-05-c1-02", "node_id": "hch-004"},
    {"sentence_id": "hij-05-c1-03", "node_id": "hch-004"},
    # --- Hij_05 発展問題 ---
    {"sentence_id": "hij-05-a1-01", "node_id": "hch-004"},
]
