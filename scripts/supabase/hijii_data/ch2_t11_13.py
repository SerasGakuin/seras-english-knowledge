"""第2章: 識別編 Theme 11-13（that / it / asの識別）"""

# ============================================================
# 1. KNOWLEDGE_NODES
# ============================================================

KNOWLEDGE_NODES = [
    {
        "id": "hid-004",
        "name": "thatの識別（関係代名詞・同格・名詞節）",
        "category": "識別",
        "priority": "P1",
        "notes": "that単体の識別。thatのうしろが不完全文（名詞が欠けている）なら関係代名詞で形容詞節、完全文なら接続詞。接続詞のthatは、名詞の中身を説明する同格のthat（the fact/news/idea/belief that～）と、文のS・O・Cをつくる名詞節のthat「～ということ」に分かれる。同格のthatと関係代名詞のthatはうしろの完全文・不完全文で識別する。",
    },
    {
        "id": "hid-009",
        "name": "thatの識別（副詞節用法 that+α）",
        "category": "識別",
        "priority": "P1",
        "notes": "that＋αの識別。so～that ...「とても～なので…」/ such～that ...「とても～なので…」/ so that S 助動詞「～するように」（目的）/ ～, so that ...「その結果～」（結果）/ now that「いまや～なので」/ in that「～という点で」。soとthatの距離・カンマの有無で3パターンを識別する。soとthatが離れれば因果（so～that）、くっついてカンマなしなら目的（so that S 助動詞）、くっついてカンマありなら結果（～, so that ...）。",
    },
    {
        "id": "hid-005",
        "name": "itの識別（形式主語・形式目的語・訳さないit）",
        "category": "識別",
        "priority": "P1",
        "notes": "itの3パターンを識別する。(1)形式主語: 英語は「長いものはうしろに」の原則から、長い主語をItで形式的に置き、うしろのthat節・不定詞の名詞的用法・動名詞の名詞句・疑問詞の名詞節で受ける。(2)形式目的語: 第5文型(SVOC)の目的語に不定詞やthat節を直接おけないので、itを目的語に置いてうしろで説明する。make it a rule to～「～することにしている」、take it for granted that～「～を当然だと思う」等。(3)訳さないit: It seems/appears that～.「～のように思える」（断定を避ける表現）、時のit、天候のit、距離のit。",
    },
    {
        "id": "hid-006",
        "name": "asの識別（前置詞・接続詞・譲歩）",
        "category": "識別",
        "priority": "P1",
        "notes": "asはうしろに名詞1語なら前置詞「～として」（イコールの性質）、うしろにSVなら接続詞。接続詞のasは4つの意味: (1)時「～するとき」（前後同時）、(2)比例「～するにつれて」（比較級とセット）、(3)理由「～ので」（becauseより弱い理由、軽くつけ加える程度）、(4)様態「～ように」（省略や代動詞とセット）。すべてのasに共通するのはイコールの性質。譲歩のas「形容詞〔名詞〕as S（may）be」は倒置形で「Sは～だけれども」。as a childは「子どものころ」と訳す例外。",
    },
]

# ============================================================
# 2. UNDERSTANDING_GOALS
# ============================================================

UNDERSTANDING_GOALS = [
    # hid-004: thatの識別（関係代名詞・同格・名詞節）
    {"node_id": "hid-004", "seq": 1, "goal": "thatのうしろが不完全文（名詞が欠けている）なら関係代名詞、完全文なら接続詞と識別できる"},
    {"node_id": "hid-004", "seq": 2, "goal": "同格のthatと相性のよい名詞（fact, news, idea, belief）を知り、同格のthatを見抜ける"},
    {"node_id": "hid-004", "seq": 3, "goal": "名詞節のthat「～ということ」が文のS・O・Cになるパターンを識別できる"},
    # hid-009: thatの識別（副詞節用法 that+α）
    {"node_id": "hid-009", "seq": 1, "goal": "so～that / such～that を見抜き「とても～なので…」と訳せる"},
    {"node_id": "hid-009", "seq": 2, "goal": "soとthatの距離・カンマの有無で so thatの3パターン（因果・目的・結果）を正確に識別できる"},
    {"node_id": "hid-009", "seq": 3, "goal": "now that「いまや～なので」、in that「～という点で」を識別できる"},
    # hid-005: itの識別
    {"node_id": "hid-005", "seq": 1, "goal": "形式主語のitを見抜き、うしろのthat節・不定詞・動名詞・疑問詞節が真の主語であると特定できる"},
    {"node_id": "hid-005", "seq": 2, "goal": "形式目的語のitが第5文型(SVOC)の目的語に使われるパターンを識別できる"},
    {"node_id": "hid-005", "seq": 3, "goal": "It seems/appears that～.や時・天候・距離のitを「訳さないit」として識別できる"},
    # hid-006: asの識別
    {"node_id": "hid-006", "seq": 1, "goal": "asのうしろに名詞1語なら前置詞「～として」、うしろにSVなら接続詞と判断できる"},
    {"node_id": "hid-006", "seq": 2, "goal": "接続詞のasを、時（同時）・比例（比較級とセット）・理由（弱い理由）・様態（省略とセット）の4つに識別できる"},
    {"node_id": "hid-006", "seq": 3, "goal": "譲歩のas（形容詞 as S be「Sは～だけれども」）を倒置の形から見抜ける"},
]

# ============================================================
# 3. CHECK_POINTS
# ============================================================

CHECK_POINTS = [
    # hid-004: thatの識別（関係代名詞・同格・名詞節）
    {"node_id": "hid-004", "seq": 1, "question": "thatが関係代名詞か接続詞かを見分ける方法は？", "answer": "thatのうしろが不完全文（名詞が欠けている）なら関係代名詞、完全文なら接続詞。"},
    {"node_id": "hid-004", "seq": 2, "question": "同格のthatと相性のよい名詞を4つ挙げよ。", "answer": "fact（事実）、news（知らせ）、idea（考え）、belief（信念）。"},
    {"node_id": "hid-004", "seq": 3, "question": "The probability is that the experiment will fail. のthatはどの用法か？", "answer": "名詞節のthat。that以下が文のC（補語）の位置で「～ということ」の意味。"},
    # hid-009: thatの識別（副詞節用法 that+α）
    {"node_id": "hid-009", "seq": 1, "question": "so thatの3パターンを挙げよ。", "answer": "(1) so～that ...「とても～なので…」（soとthatが離れる）、(2) so that S 助動詞「Sが～するように」（くっつく＋カンマなし）、(3) ～, so that ...「その結果～」（くっつく＋カンマあり）。"},
    {"node_id": "hid-009", "seq": 2, "question": "now thatとin thatの意味は？", "answer": "now that「いまや～なので」（因果関係）、in that「～という点で」（因果関係を表すこともある）。"},
    {"node_id": "hid-009", "seq": 3, "question": "such～thatとso～thatの違いは？", "answer": "suchは名詞を伴う（such a hard test that～）、soは形容詞・副詞を伴う（so small that～）。どちらも「とても～なので…」。"},
    # hid-005: itの識別
    {"node_id": "hid-005", "seq": 1, "question": "形式主語のitで代用するものを4つ挙げよ。", "answer": "that節、不定詞の名詞的用法、動名詞の名詞句、疑問詞の名詞節。"},
    {"node_id": "hid-005", "seq": 2, "question": "形式目的語のitはどの文型で使われるか？", "answer": "第5文型（SVOC）の目的語に使われる。不定詞やthat節を直接おけないので、itを目的語にしてうしろで説明する。"},
    {"node_id": "hid-005", "seq": 3, "question": "It seems that～. はどのようなitか？", "answer": "訳さないit。断定を避けて表現をやわらかくする表現。It appears that～.も同じ型。"},
    # hid-006: asの識別
    {"node_id": "hid-006", "seq": 1, "question": "asが前置詞か接続詞かを見分ける方法は？", "answer": "うしろに名詞1語なら前置詞「～として」、うしろにSVなら接続詞。"},
    {"node_id": "hid-006", "seq": 2, "question": "接続詞のasの4つの意味は？", "answer": "時「～するとき」（前後同時）、比例「～するにつれて」（比較級とセット）、理由「～ので」（弱い理由）、様態「～ように」（省略や代動詞とセット）。"},
    {"node_id": "hid-006", "seq": 3, "question": "譲歩のasの形は？", "answer": "形容詞〔名詞〕as S（may）be「Sは形容詞〔名詞〕だけれども」。S be 形容詞〔名詞〕の第2文型をイメージして訳す。"},
]

# ============================================================
# 4. NODE_PREREQUISITES
# ============================================================

NODE_PREREQUISITES = [
    {"node_id": "hid-004", "prerequisite_id": "hch-002"},
    {"node_id": "hid-009", "prerequisite_id": "hid-004"},
    {"node_id": "hid-005", "prerequisite_id": "hid-004"},
    {"node_id": "hid-006", "prerequisite_id": "hid-005"},
]

# ============================================================
# 5. KNOWLEDGE_REFERENCES
# ============================================================

KNOWLEDGE_REFERENCES = [
    {"node_id": "hid-004", "book": "肘井の読解のための英文法", "section_id": "Hij_11_1", "pages": "p.80-85"},
    {"node_id": "hid-009", "book": "肘井の読解のための英文法", "section_id": "Hij_11_2", "pages": "p.86-91"},
    {"node_id": "hid-005", "book": "肘井の読解のための英文法", "section_id": "Hij_12", "pages": "p.92-97"},
    {"node_id": "hid-006", "book": "肘井の読解のための英文法", "section_id": "Hij_13", "pages": "p.98-103"},
]

# ============================================================
# 6. SECTIONS
# ============================================================

SECTIONS = [
    {
        "id": "Hij_11_1",
        "book": "肘井の読解のための英文法",
        "title": "Theme 11 thatの識別で英文が読める①",
        "pages": "p.80-85",
        "type": "drill",
    },
    {
        "id": "Hij_11_2",
        "book": "肘井の読解のための英文法",
        "title": "Theme 11 thatの識別で英文が読める②",
        "pages": "p.86-91",
        "type": "drill",
    },
    {
        "id": "Hij_12",
        "book": "肘井の読解のための英文法",
        "title": "Theme 12 itの識別で英文が読める",
        "pages": "p.92-97",
        "type": "drill",
    },
    {
        "id": "Hij_13",
        "book": "肘井の読解のための英文法",
        "title": "Theme 13 asの識別で英文が読める",
        "pages": "p.98-103",
        "type": "drill",
    },
]

# ============================================================
# 7. SECTION_PREREQUISITES
# ============================================================

SECTION_PREREQUISITES = [
    {"section_id": "Hij_11_1", "prerequisite_id": "Hij_10"},
    {"section_id": "Hij_11_2", "prerequisite_id": "Hij_11_1"},
    {"section_id": "Hij_12", "prerequisite_id": "Hij_11_2"},
    {"section_id": "Hij_13", "prerequisite_id": "Hij_12"},
]

# ============================================================
# 8. SECTION_KNOWLEDGE_NODES
# ============================================================

SECTION_KNOWLEDGE_NODES = [
    {"section_id": "Hij_11_1", "node_id": "hid-004", "seq": 1},
    {"section_id": "Hij_11_2", "node_id": "hid-009", "seq": 1},
    {"section_id": "Hij_12", "node_id": "hid-005", "seq": 1},
    {"section_id": "Hij_13", "node_id": "hid-006", "seq": 1},
]

# ============================================================
# 9. SENTENCES
# ============================================================

SENTENCES = [
    # ==========================================================
    # Hij_11_1 -- Theme 11 thatの識別で英文が読める①
    # ==========================================================
    # ----------------------------------------------------------
    # Hij_11_1 -- 例題 (4問)
    # ----------------------------------------------------------
    {
        "id": "hij-11_1-e1-01",
        "section_id": "Hij_11_1",
        "drill": 1,
        "number": 1,
        "role": "example",
        "english": "Who that knows her can believe the story?",
        "japanese": "彼女を知る人のうちのだれが、その話を信じられるだろうか。",
        "notes": None,
    },
    {
        "id": "hij-11_1-e1-02",
        "section_id": "Hij_11_1",
        "drill": 1,
        "number": 2,
        "role": "example",
        "english": "The fact that he wrote his essay is obvious.",
        "japanese": "彼が自分の論文を書いたという事実は、明らかだ。",
        "notes": None,
    },
    {
        "id": "hij-11_1-e1-03",
        "section_id": "Hij_11_1",
        "drill": 1,
        "number": 3,
        "role": "example",
        "english": "The trouble is that she doesn't understand you at all.",
        "japanese": "困ったことに、彼女はあなたをまったく理解していない。",
        "notes": None,
    },
    {
        "id": "hij-11_1-e1-04",
        "section_id": "Hij_11_1",
        "drill": 1,
        "number": 4,
        "role": "example",
        "english": "He told me that the road was closed.",
        "japanese": "彼は、私にその道路は閉鎖されていると伝えた。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_11_1 -- ポイント例文 (3問: ポイント18, 19, 20)
    # ----------------------------------------------------------
    {
        "id": "hij-11_1-e1-05",
        "section_id": "Hij_11_1",
        "drill": 1,
        "number": 5,
        "role": "example",
        "english": "The news that he survived the accident delighted me.",
        "japanese": "彼がその事故で生き残ったという知らせが、私を喜ばせた。",
        "notes": "ポイント18 例文",
    },
    {
        "id": "hij-11_1-e1-06",
        "section_id": "Hij_11_1",
        "drill": 1,
        "number": 6,
        "role": "example",
        "english": "The country imports 50% of the oil that it consumes.",
        "japanese": "その国は、消費する石油の50％を輸入している。",
        "notes": "ポイント19 例文",
    },
    {
        "id": "hij-11_1-e1-07",
        "section_id": "Hij_11_1",
        "drill": 1,
        "number": 7,
        "role": "example",
        "english": "The probability is that the experiment will fail.",
        "japanese": "おそらく、その実験は失敗するだろう。",
        "notes": "ポイント20 例文",
    },
    # ----------------------------------------------------------
    # Hij_11_1 -- 確認問題 (3問)
    # ----------------------------------------------------------
    {
        "id": "hij-11_1-c1-01",
        "section_id": "Hij_11_1",
        "drill": 2,
        "number": 1,
        "role": "practice",
        "english": "She knew that he was married.",
        "japanese": "彼女は彼が結婚しているということを知っていた。",
        "notes": None,
    },
    {
        "id": "hij-11_1-c1-02",
        "section_id": "Hij_11_1",
        "drill": 2,
        "number": 2,
        "role": "practice",
        "english": "Who that has common sense can believe such a thing?",
        "japanese": "常識のあるだれが、そのようなものを信じられるだろうか。",
        "notes": None,
    },
    {
        "id": "hij-11_1-c1-03",
        "section_id": "Hij_11_1",
        "drill": 2,
        "number": 3,
        "role": "practice",
        "english": "The fact that you are my friend is important.",
        "japanese": "あなたが私の友人であるという事実は重要だ。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_11_1 -- 発展問題 (1問)
    # ----------------------------------------------------------
    {
        "id": "hij-11_1-a1-01",
        "section_id": "Hij_11_1",
        "drill": 3,
        "number": 1,
        "role": "advanced",
        "english": "Our belief that these ideas about birth and death are real creates a powerful illusion that causes us a great deal of suffering.",
        "japanese": "生死に関するこれらの考えが本当だというわれわれの信念は、われわれに非常に多くの苦しみをもたらす強力な幻想をつくり出す。",
        "notes": "お茶の水女子大",
    },
    # ==========================================================
    # Hij_11_2 -- Theme 11 thatの識別で英文が読める②
    # ==========================================================
    # ----------------------------------------------------------
    # Hij_11_2 -- 例題 (5問)
    # ----------------------------------------------------------
    {
        "id": "hij-11_2-e1-01",
        "section_id": "Hij_11_2",
        "drill": 1,
        "number": 1,
        "role": "example",
        "english": "The rooms are so small that it is hard to wave my arm.",
        "japanese": "それらの部屋はとても狭いので、自分の腕を振り回すのは難しい。",
        "notes": None,
    },
    {
        "id": "hij-11_2-e1-02",
        "section_id": "Hij_11_2",
        "drill": 1,
        "number": 2,
        "role": "example",
        "english": "This was such a hard test that we did not finish it.",
        "japanese": "これはとても難しいテストだったので、私たちは終えられなかった。",
        "notes": None,
    },
    {
        "id": "hij-11_2-e1-03",
        "section_id": "Hij_11_2",
        "drill": 1,
        "number": 3,
        "role": "example",
        "english": "He left home early so that he might catch the first train.",
        "japanese": "彼は始発列車に間に合うように、家を早く出た。",
        "notes": None,
    },
    {
        "id": "hij-11_2-e1-04",
        "section_id": "Hij_11_2",
        "drill": 1,
        "number": 4,
        "role": "example",
        "english": "Now that he has a child, he has to work harder.",
        "japanese": "いまや彼には子どもがいるので、もっと一生懸命働かなければならない。",
        "notes": None,
    },
    {
        "id": "hij-11_2-e1-05",
        "section_id": "Hij_11_2",
        "drill": 1,
        "number": 5,
        "role": "example",
        "english": "Men differ from animals in that they can think and speak.",
        "japanese": "人間は考えたり話したりできる点で、動物と違う。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_11_2 -- ポイント例文 (3問: ポイント21 例文1-3)
    # ----------------------------------------------------------
    {
        "id": "hij-11_2-e1-06",
        "section_id": "Hij_11_2",
        "drill": 1,
        "number": 6,
        "role": "example",
        "english": "This is so beautiful that I can't express it by words.",
        "japanese": "これはとても美しいので、言葉では表せない。",
        "notes": "ポイント21 例文1",
    },
    {
        "id": "hij-11_2-e1-07",
        "section_id": "Hij_11_2",
        "drill": 1,
        "number": 7,
        "role": "example",
        "english": "Let's take an express train so that we can get there on time.",
        "japanese": "時間通りにそこに到着できるように、急行列車に乗ろう。",
        "notes": "ポイント21 例文2",
    },
    {
        "id": "hij-11_2-e1-08",
        "section_id": "Hij_11_2",
        "drill": 1,
        "number": 8,
        "role": "example",
        "english": "He was late for the time, so that he missed the train.",
        "japanese": "彼はその時間に遅れた。その結果、電車を逃した。",
        "notes": "ポイント21 例文3",
    },
    # ----------------------------------------------------------
    # Hij_11_2 -- 確認問題 (3問)
    # ----------------------------------------------------------
    {
        "id": "hij-11_2-c1-01",
        "section_id": "Hij_11_2",
        "drill": 2,
        "number": 1,
        "role": "practice",
        "english": "This is so beautiful a picture that I can't express it by words.",
        "japanese": "これはとても美しい絵なので、言葉では表せない。",
        "notes": None,
    },
    {
        "id": "hij-11_2-c1-02",
        "section_id": "Hij_11_2",
        "drill": 2,
        "number": 2,
        "role": "practice",
        "english": "You should be more mature now that you are a high school student.",
        "japanese": "いまやあなたは高校生なので、もっと分別があるべきだ。",
        "notes": None,
    },
    {
        "id": "hij-11_2-c1-03",
        "section_id": "Hij_11_2",
        "drill": 2,
        "number": 3,
        "role": "practice",
        "english": "She has been lucky in that she has never had to worry about money.",
        "japanese": "彼女は一度もお金の心配をしなくてもよかった点で、幸運だ。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_11_2 -- 発展問題 (1問)
    # ----------------------------------------------------------
    {
        "id": "hij-11_2-a1-01",
        "section_id": "Hij_11_2",
        "drill": 3,
        "number": 1,
        "role": "advanced",
        "english": "The gate was locked so that no one could come into the factory without permission.",
        "japanese": "その門は、だれも許可なしで工場に入ってこられないように、鍵がかけられていた。",
        "notes": "センター試験・本試／改",
    },
    # ==========================================================
    # Hij_12 -- Theme 12 itの識別で英文が読める
    # ==========================================================
    # ----------------------------------------------------------
    # Hij_12 -- 例題 (5問)
    # ----------------------------------------------------------
    {
        "id": "hij-12-e1-01",
        "section_id": "Hij_12",
        "drill": 1,
        "number": 1,
        "role": "example",
        "english": "It is important that you understand her feelings.",
        "japanese": "あなたが彼女の感情を理解することが、重要だ。",
        "notes": None,
    },
    {
        "id": "hij-12-e1-02",
        "section_id": "Hij_12",
        "drill": 1,
        "number": 2,
        "role": "example",
        "english": "It is not wise to pay little attention to your own health.",
        "japanese": "自分自身の健康にほとんど注意を払わないのは、賢明ではない。",
        "notes": None,
    },
    {
        "id": "hij-12-e1-03",
        "section_id": "Hij_12",
        "drill": 1,
        "number": 3,
        "role": "example",
        "english": "I make it a rule to take a walk in the morning.",
        "japanese": "私は朝、散歩することにしている。",
        "notes": None,
    },
    {
        "id": "hij-12-e1-04",
        "section_id": "Hij_12",
        "drill": 1,
        "number": 4,
        "role": "example",
        "english": "You should not take it for granted that I will help you.",
        "japanese": "あなたは、私があなたを助けることを当然だと思うべきではない。",
        "notes": None,
    },
    {
        "id": "hij-12-e1-05",
        "section_id": "Hij_12",
        "drill": 1,
        "number": 5,
        "role": "example",
        "english": "It seems that he is not suitable for the task.",
        "japanese": "彼はその仕事に適していないように思える。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_12 -- ポイント例文 (5問: ポイント22 例文1-4, ポイント23 例文)
    # ----------------------------------------------------------
    {
        "id": "hij-12-e1-06",
        "section_id": "Hij_12",
        "drill": 1,
        "number": 6,
        "role": "example",
        "english": "It's a shame that she can't come.",
        "japanese": "彼女が来られないのは残念だ。",
        "notes": "ポイント22 例文1",
    },
    {
        "id": "hij-12-e1-07",
        "section_id": "Hij_12",
        "drill": 1,
        "number": 7,
        "role": "example",
        "english": "It is difficult to remember the rule.",
        "japanese": "そのルールを覚えることは難しい。",
        "notes": "ポイント22 例文2",
    },
    {
        "id": "hij-12-e1-08",
        "section_id": "Hij_12",
        "drill": 1,
        "number": 8,
        "role": "example",
        "english": "It is no use crying over spilt milk.",
        "japanese": "こぼれたミルクを嘆いても意味がない（覆水盆に返らず）。",
        "notes": "ポイント22 例文3",
    },
    {
        "id": "hij-12-e1-09",
        "section_id": "Hij_12",
        "drill": 1,
        "number": 9,
        "role": "example",
        "english": "It does not matter who you are.",
        "japanese": "あなたがだれかは重要ではない。",
        "notes": "ポイント22 例文4",
    },
    {
        "id": "hij-12-e1-10",
        "section_id": "Hij_12",
        "drill": 1,
        "number": 10,
        "role": "example",
        "english": "It appears that she knows everything about it.",
        "japanese": "彼女はそれについてすべてを知っているように思える。",
        "notes": "ポイント23 例文",
    },
    # ----------------------------------------------------------
    # Hij_12 -- 確認問題 (3問)
    # ----------------------------------------------------------
    {
        "id": "hij-12-c1-01",
        "section_id": "Hij_12",
        "drill": 2,
        "number": 1,
        "role": "practice",
        "english": "It's a great pleasure to be with you.",
        "japanese": "あなたと一緒にいることは、とてもうれしい。",
        "notes": None,
    },
    {
        "id": "hij-12-c1-02",
        "section_id": "Hij_12",
        "drill": 2,
        "number": 2,
        "role": "practice",
        "english": "It appears that you don't understand her feelings.",
        "japanese": "あなたは彼女の感情を理解していないように思える。",
        "notes": None,
    },
    {
        "id": "hij-12-c1-03",
        "section_id": "Hij_12",
        "drill": 2,
        "number": 3,
        "role": "practice",
        "english": "She gave up her job as she found it impossible to work.",
        "japanese": "彼女は働くのがむりだと思ったので、仕事を辞めた。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_12 -- 発展問題 (1問)
    # ----------------------------------------------------------
    {
        "id": "hij-12-a1-01",
        "section_id": "Hij_12",
        "drill": 3,
        "number": 1,
        "role": "advanced",
        "english": "Most social scientists take it for granted that a person's clothing expresses meaning.",
        "japanese": "ほとんどの社会科学者が、人の衣服が意味を表すということを当然だと思っている。",
        "notes": "九州大",
    },
    # ==========================================================
    # Hij_13 -- Theme 13 asの識別で英文が読める
    # ==========================================================
    # ----------------------------------------------------------
    # Hij_13 -- 例題 (5問)
    # ----------------------------------------------------------
    {
        "id": "hij-13-e1-01",
        "section_id": "Hij_13",
        "drill": 1,
        "number": 1,
        "role": "example",
        "english": "He worked as president of the company.",
        "japanese": "彼はその会社の社長として働いた。",
        "notes": None,
    },
    {
        "id": "hij-13-e1-02",
        "section_id": "Hij_13",
        "drill": 1,
        "number": 2,
        "role": "example",
        "english": "As I got there, he left there.",
        "japanese": "私がそこに着くと、彼はそこを出発した。",
        "notes": None,
    },
    {
        "id": "hij-13-e1-03",
        "section_id": "Hij_13",
        "drill": 1,
        "number": 3,
        "role": "example",
        "english": "As it grew darker, it became colder.",
        "japanese": "暗くなるにつれて、寒くなってきた。",
        "notes": None,
    },
    {
        "id": "hij-13-e1-04",
        "section_id": "Hij_13",
        "drill": 1,
        "number": 4,
        "role": "example",
        "english": "Tom gave up his job as he couldn't work.",
        "japanese": "トムは働けなくなったので、仕事を辞めた。",
        "notes": None,
    },
    {
        "id": "hij-13-e1-05",
        "section_id": "Hij_13",
        "drill": 1,
        "number": 5,
        "role": "example",
        "english": "He doesn't behave as I tell him to.",
        "japanese": "彼は、私が言うようにはふるまわない。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_13 -- ポイント例文 (2問: ポイント24, 25)
    # ----------------------------------------------------------
    {
        "id": "hij-13-e1-06",
        "section_id": "Hij_13",
        "drill": 1,
        "number": 6,
        "role": "example",
        "english": "As a child I was afraid of dogs.",
        "japanese": "子どものころ、私は犬がこわかった。",
        "notes": "ポイント24 例文",
    },
    {
        "id": "hij-13-e1-07",
        "section_id": "Hij_13",
        "drill": 1,
        "number": 7,
        "role": "example",
        "english": "Young as he is, he is a good manager.",
        "japanese": "彼は若いけれども、立派な経営者だ。",
        "notes": "ポイント25 例文",
    },
    # ----------------------------------------------------------
    # Hij_13 -- 確認問題 (4問)
    # ----------------------------------------------------------
    {
        "id": "hij-13-c1-01",
        "section_id": "Hij_13",
        "drill": 2,
        "number": 1,
        "role": "practice",
        "english": "As he is a married man, he has to think of his wife.",
        "japanese": "彼は既婚者なので、妻のことを考えなければならない。",
        "notes": None,
    },
    {
        "id": "hij-13-c1-02",
        "section_id": "Hij_13",
        "drill": 2,
        "number": 2,
        "role": "practice",
        "english": "When you are in Rome, do as the Romans do.",
        "japanese": "ローマにいるときは、ローマ人がやるようにしなさい（郷に入りては郷に従え）。",
        "notes": None,
    },
    {
        "id": "hij-13-c1-03",
        "section_id": "Hij_13",
        "drill": 2,
        "number": 3,
        "role": "practice",
        "english": "We do not necessarily grow wiser as we grow older.",
        "japanese": "私たちは年をとるにつれて、必ずしも賢くなるわけではない。",
        "notes": None,
    },
    {
        "id": "hij-13-c1-04",
        "section_id": "Hij_13",
        "drill": 2,
        "number": 4,
        "role": "practice",
        "english": "As autumn comes, we feel lonely.",
        "japanese": "秋がくると、私たちはさびしく感じる。",
        "notes": None,
    },
    # ----------------------------------------------------------
    # Hij_13 -- 発展問題 (1問)
    # ----------------------------------------------------------
    {
        "id": "hij-13-a1-01",
        "section_id": "Hij_13",
        "drill": 3,
        "number": 1,
        "role": "advanced",
        "english": "As these languages become more powerful, their use as tools of business and culture increases.",
        "japanese": "これらの言語はより強力になるにつれて、ビジネスや文化の道具として使われることが増えている。",
        "notes": "佐賀大",
    },
]

# ============================================================
# 10. SENTENCE_STRUCTURES
# ============================================================

SENTENCE_STRUCTURES = [
    # --- hij-11_1-e1-01 ---
    {"sentence_id": "hij-11_1-e1-01", "label": "overall", "value": "S (M) V O"},
    {"sentence_id": "hij-11_1-e1-01", "label": "details", "value": "Who(S) (that knows her)(M:関係代名詞) can believe(V) the story(O)?"},
    # --- hij-11_1-e1-02 ---
    {"sentence_id": "hij-11_1-e1-02", "label": "overall", "value": "S <同格> V C"},
    {"sentence_id": "hij-11_1-e1-02", "label": "details", "value": "The fact(S) <that he wrote his essay>(同格のthat) is(V) obvious(C)"},
    # --- hij-11_1-e1-03 ---
    {"sentence_id": "hij-11_1-e1-03", "label": "overall", "value": "S V C"},
    {"sentence_id": "hij-11_1-e1-03", "label": "details", "value": "The trouble(S) is(V) <that she doesn't understand you at all>(C:名詞節)"},
    # --- hij-11_1-e1-04 ---
    {"sentence_id": "hij-11_1-e1-04", "label": "overall", "value": "S V O1 O2"},
    {"sentence_id": "hij-11_1-e1-04", "label": "details", "value": "He(S) told(V) me(O1) <that the road was closed>(O2:名詞節)"},
    # --- hij-11_1-e1-05 (ポイント18) ---
    {"sentence_id": "hij-11_1-e1-05", "label": "overall", "value": "S <同格> V O"},
    {"sentence_id": "hij-11_1-e1-05", "label": "details", "value": "The news(S) <that he survived the accident>(同格のthat) delighted(V) me(O)"},
    # --- hij-11_1-e1-06 (ポイント19) ---
    {"sentence_id": "hij-11_1-e1-06", "label": "overall", "value": "S V O (M)"},
    {"sentence_id": "hij-11_1-e1-06", "label": "details", "value": "The country(S) imports(V) 50% of the oil(O) (that it consumes)(M:関係代名詞)"},
    # --- hij-11_1-e1-07 (ポイント20) ---
    {"sentence_id": "hij-11_1-e1-07", "label": "overall", "value": "S V C"},
    {"sentence_id": "hij-11_1-e1-07", "label": "details", "value": "The probability(S) is(V) <that the experiment will fail>(C:名詞節)"},
    # --- hij-11_1-c1-01 ---
    {"sentence_id": "hij-11_1-c1-01", "label": "overall", "value": "S V O"},
    {"sentence_id": "hij-11_1-c1-01", "label": "details", "value": "She(S) knew(V) <that he was married>(O:名詞節)"},
    # --- hij-11_1-c1-02 ---
    {"sentence_id": "hij-11_1-c1-02", "label": "overall", "value": "S (M) V O"},
    {"sentence_id": "hij-11_1-c1-02", "label": "details", "value": "Who(S) (that has common sense)(M:関係代名詞) can believe(V) such a thing(O)?"},
    # --- hij-11_1-c1-03 ---
    {"sentence_id": "hij-11_1-c1-03", "label": "overall", "value": "S <同格> V C"},
    {"sentence_id": "hij-11_1-c1-03", "label": "details", "value": "The fact(S) <that you are my friend>(同格のthat) is(V) important(C)"},
    # --- hij-11_1-a1-01 ---
    {"sentence_id": "hij-11_1-a1-01", "label": "overall", "value": "S <同格> V O (M)"},
    {"sentence_id": "hij-11_1-a1-01", "label": "details", "value": "Our belief(S) <that these ideas about birth and death are real>(同格のthat) creates(V) a powerful illusion(O) (that causes us a great deal of suffering)(M:関係代名詞)"},
    # --- hij-11_2-e1-01 ---
    {"sentence_id": "hij-11_2-e1-01", "label": "overall", "value": "S V C [M]"},
    {"sentence_id": "hij-11_2-e1-01", "label": "details", "value": "The rooms(S) are(V) so small(C) [that it is hard to wave my arm](M:so~that)"},
    # --- hij-11_2-e1-02 ---
    {"sentence_id": "hij-11_2-e1-02", "label": "overall", "value": "S V C [M]"},
    {"sentence_id": "hij-11_2-e1-02", "label": "details", "value": "This(S) was(V) such a hard test(C) [that we did not finish it](M:such~that)"},
    # --- hij-11_2-e1-03 ---
    {"sentence_id": "hij-11_2-e1-03", "label": "overall", "value": "S V O M [M]"},
    {"sentence_id": "hij-11_2-e1-03", "label": "details", "value": "He(S) left(V) home(O) early(M) [so that he might catch the first train](M:so that目的)"},
    # --- hij-11_2-e1-04 ---
    {"sentence_id": "hij-11_2-e1-04", "label": "overall", "value": "[M] S V M"},
    {"sentence_id": "hij-11_2-e1-04", "label": "details", "value": "[Now that he has a child](M:now that) he(S) has to work(V) harder(M)"},
    # --- hij-11_2-e1-05 ---
    {"sentence_id": "hij-11_2-e1-05", "label": "overall", "value": "S V [M] [M]"},
    {"sentence_id": "hij-11_2-e1-05", "label": "details", "value": "Men(S) differ(V) [from animals](M) [in that they can think and speak](M:in that)"},
    # --- hij-11_2-e1-06 (ポイント21 例文1) ---
    {"sentence_id": "hij-11_2-e1-06", "label": "overall", "value": "S V C [M]"},
    {"sentence_id": "hij-11_2-e1-06", "label": "details", "value": "This(S) is(V) so beautiful(C) [that I can't express it by words](M:so~that)"},
    # --- hij-11_2-e1-07 (ポイント21 例文2) ---
    {"sentence_id": "hij-11_2-e1-07", "label": "overall", "value": "V O [M]"},
    {"sentence_id": "hij-11_2-e1-07", "label": "details", "value": "Let's take(V) an express train(O) [so that we can get there on time](M:so that目的)"},
    # --- hij-11_2-e1-08 (ポイント21 例文3) ---
    {"sentence_id": "hij-11_2-e1-08", "label": "overall", "value": "S V C [M] [M]"},
    {"sentence_id": "hij-11_2-e1-08", "label": "details", "value": "He(S) was(V) late(C) [for the time](M) [so that he missed the train](M:so that結果)"},
    # --- hij-11_2-c1-01 ---
    {"sentence_id": "hij-11_2-c1-01", "label": "overall", "value": "S V C [M]"},
    {"sentence_id": "hij-11_2-c1-01", "label": "details", "value": "This(S) is(V) so beautiful a picture(C) [that I can't express it by words](M:so~that)"},
    # --- hij-11_2-c1-02 ---
    {"sentence_id": "hij-11_2-c1-02", "label": "overall", "value": "S V C [M]"},
    {"sentence_id": "hij-11_2-c1-02", "label": "details", "value": "You(S) should be(V) more mature(C) [now that you are a high school student](M:now that)"},
    # --- hij-11_2-c1-03 ---
    {"sentence_id": "hij-11_2-c1-03", "label": "overall", "value": "S V C [M]"},
    {"sentence_id": "hij-11_2-c1-03", "label": "details", "value": "She(S) has been(V) lucky(C) [in that she has never had to worry about money](M:in that)"},
    # --- hij-11_2-a1-01 ---
    {"sentence_id": "hij-11_2-a1-01", "label": "overall", "value": "S V [M]"},
    {"sentence_id": "hij-11_2-a1-01", "label": "details", "value": "The gate(S) was locked(V) [so that no one could come into the factory without permission](M:so that目的)"},
    # --- hij-12-e1-01 ---
    {"sentence_id": "hij-12-e1-01", "label": "overall", "value": "S V C S'"},
    {"sentence_id": "hij-12-e1-01", "label": "details", "value": "It(S:形式主語) is(V) important(C) <that you understand her feelings>(S':名詞節)"},
    # --- hij-12-e1-02 ---
    {"sentence_id": "hij-12-e1-02", "label": "overall", "value": "S V C S'"},
    {"sentence_id": "hij-12-e1-02", "label": "details", "value": "It(S:形式主語) is not(V) wise(C) <to pay little attention to your own health>(S':不定詞)"},
    # --- hij-12-e1-03 ---
    {"sentence_id": "hij-12-e1-03", "label": "overall", "value": "S V O C O'"},
    {"sentence_id": "hij-12-e1-03", "label": "details", "value": "I(S) make(V) it(O:形式目的語) a rule(C) <to take a walk in the morning>(O':不定詞)"},
    # --- hij-12-e1-04 ---
    {"sentence_id": "hij-12-e1-04", "label": "overall", "value": "S V A for B A'"},
    {"sentence_id": "hij-12-e1-04", "label": "details", "value": "You(S) should not take(V) it(A:形式目的語) for granted(B) <that I will help you>(A':名詞節)"},
    # --- hij-12-e1-05 ---
    {"sentence_id": "hij-12-e1-05", "label": "overall", "value": "S V C M"},
    {"sentence_id": "hij-12-e1-05", "label": "details", "value": "It(S:訳さないit) seems(V) <that he is not suitable for the task>(C)"},
    # --- hij-12-e1-06 (ポイント22 例文1) ---
    {"sentence_id": "hij-12-e1-06", "label": "overall", "value": "S V C S'"},
    {"sentence_id": "hij-12-e1-06", "label": "details", "value": "It(S:形式主語) 's(V) a shame(C) <that she can't come>(S':名詞節)"},
    # --- hij-12-e1-07 (ポイント22 例文2) ---
    {"sentence_id": "hij-12-e1-07", "label": "overall", "value": "S V C S'"},
    {"sentence_id": "hij-12-e1-07", "label": "details", "value": "It(S:形式主語) is(V) difficult(C) <to remember the rule>(S':不定詞)"},
    # --- hij-12-e1-08 (ポイント22 例文3) ---
    {"sentence_id": "hij-12-e1-08", "label": "overall", "value": "S V C S'"},
    {"sentence_id": "hij-12-e1-08", "label": "details", "value": "It(S:形式主語) is(V) no use(C) <crying over spilt milk>(S':動名詞)"},
    # --- hij-12-e1-09 (ポイント22 例文4) ---
    {"sentence_id": "hij-12-e1-09", "label": "overall", "value": "S V S'"},
    {"sentence_id": "hij-12-e1-09", "label": "details", "value": "It(S:形式主語) does not matter(V) <who you are>(S':疑問詞節)"},
    # --- hij-12-e1-10 (ポイント23) ---
    {"sentence_id": "hij-12-e1-10", "label": "overall", "value": "S V O [M]"},
    {"sentence_id": "hij-12-e1-10", "label": "details", "value": "It(S:訳さないit) appears(V) <that she knows everything>(O) [about it](M)"},
    # --- hij-12-c1-01 ---
    {"sentence_id": "hij-12-c1-01", "label": "overall", "value": "S V C S'"},
    {"sentence_id": "hij-12-c1-01", "label": "details", "value": "It(S:形式主語) 's(V) a great pleasure(C) <to be with you>(S':不定詞)"},
    # --- hij-12-c1-02 ---
    {"sentence_id": "hij-12-c1-02", "label": "overall", "value": "S V O"},
    {"sentence_id": "hij-12-c1-02", "label": "details", "value": "It(S:訳さないit) appears(V) <that you don't understand her feelings>(O)"},
    # --- hij-12-c1-03 ---
    {"sentence_id": "hij-12-c1-03", "label": "overall", "value": "S V O [M]"},
    {"sentence_id": "hij-12-c1-03", "label": "details", "value": "She(S) gave up(V) her job(O) [as she found it impossible to work](M:理由のas+形式目的語)"},
    # --- hij-12-a1-01 ---
    {"sentence_id": "hij-12-a1-01", "label": "overall", "value": "S V A for B A'"},
    {"sentence_id": "hij-12-a1-01", "label": "details", "value": "Most social scientists(S) take(V) it(A:形式目的語) for granted(B) <that a person's clothing expresses meaning>(A':名詞節)"},
    # --- hij-13-e1-01 ---
    {"sentence_id": "hij-13-e1-01", "label": "overall", "value": "S V [M]"},
    {"sentence_id": "hij-13-e1-01", "label": "details", "value": "He(S) worked(V) [as president of the company](M:前置詞as)"},
    # --- hij-13-e1-02 ---
    {"sentence_id": "hij-13-e1-02", "label": "overall", "value": "[M] S V M"},
    {"sentence_id": "hij-13-e1-02", "label": "details", "value": "[As I got there](M:時のas) he(S) left(V) there(M)"},
    # --- hij-13-e1-03 ---
    {"sentence_id": "hij-13-e1-03", "label": "overall", "value": "[M] S V C"},
    {"sentence_id": "hij-13-e1-03", "label": "details", "value": "[As it grew darker](M:比例のas) it(S) became(V) colder(C)"},
    # --- hij-13-e1-04 ---
    {"sentence_id": "hij-13-e1-04", "label": "overall", "value": "S V O [M]"},
    {"sentence_id": "hij-13-e1-04", "label": "details", "value": "Tom(S) gave up(V) his job(O) [as he couldn't work](M:理由のas)"},
    # --- hij-13-e1-05 ---
    {"sentence_id": "hij-13-e1-05", "label": "overall", "value": "S V [M]"},
    {"sentence_id": "hij-13-e1-05", "label": "details", "value": "He(S) doesn't behave(V) [as I tell him to](M:様態のas)"},
    # --- hij-13-e1-06 (ポイント24) ---
    {"sentence_id": "hij-13-e1-06", "label": "overall", "value": "[M] S V O"},
    {"sentence_id": "hij-13-e1-06", "label": "details", "value": "[As a child](M:前置詞as) I(S) was afraid(V) [of dogs](O)"},
    # --- hij-13-e1-07 (ポイント25) ---
    {"sentence_id": "hij-13-e1-07", "label": "overall", "value": "[M] S V C"},
    {"sentence_id": "hij-13-e1-07", "label": "details", "value": "[Young as he is](M:譲歩のas) he(S) is(V) a good manager(C)"},
    # --- hij-13-c1-01 ---
    {"sentence_id": "hij-13-c1-01", "label": "overall", "value": "[M] S V M"},
    {"sentence_id": "hij-13-c1-01", "label": "details", "value": "[As he is a married man](M:理由のas) he(S) has to think(V) [of his wife](M)"},
    # --- hij-13-c1-02 ---
    {"sentence_id": "hij-13-c1-02", "label": "overall", "value": "[M] V [M]"},
    {"sentence_id": "hij-13-c1-02", "label": "details", "value": "[When you are in Rome](M) do(V) [as the Romans do](M:様態のas)"},
    # --- hij-13-c1-03 ---
    {"sentence_id": "hij-13-c1-03", "label": "overall", "value": "S V C [M]"},
    {"sentence_id": "hij-13-c1-03", "label": "details", "value": "We(S) do not necessarily grow(V) wiser(C) [as we grow older](M:比例のas)"},
    # --- hij-13-c1-04 ---
    {"sentence_id": "hij-13-c1-04", "label": "overall", "value": "[M] S V C"},
    {"sentence_id": "hij-13-c1-04", "label": "details", "value": "[As autumn comes](M:時のas) we(S) feel(V) lonely(C)"},
    # --- hij-13-a1-01 ---
    {"sentence_id": "hij-13-a1-01", "label": "overall", "value": "[M] S (M) V"},
    {"sentence_id": "hij-13-a1-01", "label": "details", "value": "[As these languages become more powerful](M:比例のas) their use(S) (as tools of business and culture)(M:前置詞as) increases(V)"},
]

# ============================================================
# 11. SENTENCE_KNOWLEDGE_TAGS
# ============================================================

SENTENCE_KNOWLEDGE_TAGS = [
    # --- Hij_11_1 例題 + ポイント例文 ---
    {"sentence_id": "hij-11_1-e1-01", "node_id": "hid-004"},  # 関係代名詞
    {"sentence_id": "hij-11_1-e1-02", "node_id": "hid-004"},  # 同格のthat
    {"sentence_id": "hij-11_1-e1-03", "node_id": "hid-004"},  # 名詞節(C)
    {"sentence_id": "hij-11_1-e1-04", "node_id": "hid-004"},  # 名詞節(O2)
    {"sentence_id": "hij-11_1-e1-05", "node_id": "hid-004"},  # 同格のthat
    {"sentence_id": "hij-11_1-e1-06", "node_id": "hid-004"},  # 関係代名詞
    {"sentence_id": "hij-11_1-e1-07", "node_id": "hid-004"},  # 名詞節(C)
    # --- Hij_11_1 確認問題 ---
    {"sentence_id": "hij-11_1-c1-01", "node_id": "hid-004"},  # 名詞節(O)
    {"sentence_id": "hij-11_1-c1-02", "node_id": "hid-004"},  # 関係代名詞
    {"sentence_id": "hij-11_1-c1-03", "node_id": "hid-004"},  # 同格のthat
    # --- Hij_11_1 発展問題 ---
    {"sentence_id": "hij-11_1-a1-01", "node_id": "hid-004"},  # 同格+関係代名詞
    # --- Hij_11_2 例題 + ポイント例文 ---
    {"sentence_id": "hij-11_2-e1-01", "node_id": "hid-009"},  # so~that
    {"sentence_id": "hij-11_2-e1-02", "node_id": "hid-009"},  # such~that
    {"sentence_id": "hij-11_2-e1-03", "node_id": "hid-009"},  # so that目的
    {"sentence_id": "hij-11_2-e1-04", "node_id": "hid-009"},  # now that
    {"sentence_id": "hij-11_2-e1-05", "node_id": "hid-009"},  # in that
    {"sentence_id": "hij-11_2-e1-06", "node_id": "hid-009"},  # so~that
    {"sentence_id": "hij-11_2-e1-07", "node_id": "hid-009"},  # so that目的
    {"sentence_id": "hij-11_2-e1-08", "node_id": "hid-009"},  # so that結果
    # --- Hij_11_2 確認問題 ---
    {"sentence_id": "hij-11_2-c1-01", "node_id": "hid-009"},  # so~that
    {"sentence_id": "hij-11_2-c1-02", "node_id": "hid-009"},  # now that
    {"sentence_id": "hij-11_2-c1-03", "node_id": "hid-009"},  # in that
    # --- Hij_11_2 発展問題 ---
    {"sentence_id": "hij-11_2-a1-01", "node_id": "hid-009"},  # so that目的
    # --- Hij_12 例題 + ポイント例文 ---
    {"sentence_id": "hij-12-e1-01", "node_id": "hid-005"},  # 形式主語(that節)
    {"sentence_id": "hij-12-e1-02", "node_id": "hid-005"},  # 形式主語(不定詞)
    {"sentence_id": "hij-12-e1-03", "node_id": "hid-005"},  # 形式目的語
    {"sentence_id": "hij-12-e1-04", "node_id": "hid-005"},  # 形式目的語
    {"sentence_id": "hij-12-e1-05", "node_id": "hid-005"},  # 訳さないit
    {"sentence_id": "hij-12-e1-06", "node_id": "hid-005"},  # 形式主語(that節)
    {"sentence_id": "hij-12-e1-07", "node_id": "hid-005"},  # 形式主語(不定詞)
    {"sentence_id": "hij-12-e1-08", "node_id": "hid-005"},  # 形式主語(動名詞)
    {"sentence_id": "hij-12-e1-09", "node_id": "hid-005"},  # 形式主語(疑問詞節)
    {"sentence_id": "hij-12-e1-10", "node_id": "hid-005"},  # 訳さないit
    # --- Hij_12 確認問題 ---
    {"sentence_id": "hij-12-c1-01", "node_id": "hid-005"},  # 形式主語(不定詞)
    {"sentence_id": "hij-12-c1-02", "node_id": "hid-005"},  # 訳さないit
    {"sentence_id": "hij-12-c1-03", "node_id": "hid-005"},  # 形式目的語
    # --- Hij_12 発展問題 ---
    {"sentence_id": "hij-12-a1-01", "node_id": "hid-005"},  # 形式目的語
    # --- Hij_13 例題 + ポイント例文 ---
    {"sentence_id": "hij-13-e1-01", "node_id": "hid-006"},  # 前置詞as
    {"sentence_id": "hij-13-e1-02", "node_id": "hid-006"},  # 時のas
    {"sentence_id": "hij-13-e1-03", "node_id": "hid-006"},  # 比例のas
    {"sentence_id": "hij-13-e1-04", "node_id": "hid-006"},  # 理由のas
    {"sentence_id": "hij-13-e1-05", "node_id": "hid-006"},  # 様態のas
    {"sentence_id": "hij-13-e1-06", "node_id": "hid-006"},  # 前置詞as
    {"sentence_id": "hij-13-e1-07", "node_id": "hid-006"},  # 譲歩のas
    # --- Hij_13 確認問題 ---
    {"sentence_id": "hij-13-c1-01", "node_id": "hid-006"},  # 理由のas
    {"sentence_id": "hij-13-c1-02", "node_id": "hid-006"},  # 様態のas
    {"sentence_id": "hij-13-c1-03", "node_id": "hid-006"},  # 比例のas
    {"sentence_id": "hij-13-c1-04", "node_id": "hid-006"},  # 時のas
    # --- Hij_13 発展問題 ---
    {"sentence_id": "hij-13-a1-01", "node_id": "hid-006"},  # 比例のas+前置詞as
]
