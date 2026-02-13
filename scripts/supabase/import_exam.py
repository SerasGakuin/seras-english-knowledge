"""Import Exam_01 and Exam_02 data into Supabase.

Phase D: Exam sections contain university entrance exam sentences
that test knowledge from all chapters.

Usage:
    python scripts/supabase/import_exam.py [--dry-run]

Environment variables:
    SUPABASE_URL  - Supabase project URL
    SUPABASE_KEY  - Supabase service_role key
"""

import argparse
import os
import sys

from supabase import create_client


# ============================================================
# Data definitions
# ============================================================

SECTIONS = [
    {
        "id": "Exam_01",
        "book": "はじめの英文読解ドリル",
        "title": "入試実戦演習①",
        "pages": "p.150-154",
        "type": "exam",
    },
    {
        "id": "Exam_02",
        "book": "はじめの英文読解ドリル",
        "title": "入試実戦演習②",
        "pages": "p.155-160",
        "type": "exam",
    },
]

# Both Exam sections require the final drill section from each chapter
SECTION_PREREQUISITES = [
    {"section_id": "Exam_01", "prerequisite_id": prereq}
    for prereq in [
        "Ch01_06", "Ch02_08", "Ch03_05", "Ch04_06", "Ch05_02", "Ch06_06",
    ]
] + [
    {"section_id": "Exam_02", "prerequisite_id": prereq}
    for prereq in [
        "Ch01_06", "Ch02_08", "Ch03_05", "Ch04_06", "Ch05_02", "Ch06_06",
    ]
]

# Section knowledge nodes (union of all sentence tags, seq ordered by first appearance)
SECTION_KNOWLEDGE_NODES = [
    # Exam_01
    {"section_id": "Exam_01", "node_id": "strc-007", "seq": 1},
    {"section_id": "Exam_01", "node_id": "strc-008", "seq": 2},
    {"section_id": "Exam_01", "node_id": "clau-034", "seq": 3},
    {"section_id": "Exam_01", "node_id": "vtyp-007", "seq": 4},
    {"section_id": "Exam_01", "node_id": "read-011", "seq": 5},
    {"section_id": "Exam_01", "node_id": "clau-032", "seq": 6},
    {"section_id": "Exam_01", "node_id": "clau-039", "seq": 7},
    {"section_id": "Exam_01", "node_id": "read-010", "seq": 8},
    {"section_id": "Exam_01", "node_id": "clau-004", "seq": 9},
    {"section_id": "Exam_01", "node_id": "clau-006", "seq": 10},
    {"section_id": "Exam_01", "node_id": "read-008", "seq": 11},
    {"section_id": "Exam_01", "node_id": "clau-033", "seq": 12},
    {"section_id": "Exam_01", "node_id": "strc-015", "seq": 13},
    {"section_id": "Exam_01", "node_id": "read-013", "seq": 14},
    {"section_id": "Exam_01", "node_id": "clau-007", "seq": 15},
    {"section_id": "Exam_01", "node_id": "clau-028", "seq": 16},
    # Exam_02
    {"section_id": "Exam_02", "node_id": "clau-031", "seq": 1},
    {"section_id": "Exam_02", "node_id": "clau-033", "seq": 2},
    {"section_id": "Exam_02", "node_id": "clau-007", "seq": 3},
    {"section_id": "Exam_02", "node_id": "clau-004", "seq": 4},
    {"section_id": "Exam_02", "node_id": "clau-036", "seq": 5},
    {"section_id": "Exam_02", "node_id": "clau-032", "seq": 6},
    {"section_id": "Exam_02", "node_id": "clau-013", "seq": 7},
    {"section_id": "Exam_02", "node_id": "read-008", "seq": 8},
    {"section_id": "Exam_02", "node_id": "subj-003", "seq": 9},
    {"section_id": "Exam_02", "node_id": "read-007", "seq": 10},
    {"section_id": "Exam_02", "node_id": "strc-008", "seq": 11},
    {"section_id": "Exam_02", "node_id": "strc-007", "seq": 12},
    {"section_id": "Exam_02", "node_id": "clau-034", "seq": 13},
    {"section_id": "Exam_02", "node_id": "clau-028", "seq": 14},
    {"section_id": "Exam_02", "node_id": "clau-008", "seq": 15},
    {"section_id": "Exam_02", "node_id": "clau-029", "seq": 16},
    {"section_id": "Exam_02", "node_id": "vtyp-021", "seq": 17},
    {"section_id": "Exam_02", "node_id": "strc-015", "seq": 18},
    {"section_id": "Exam_02", "node_id": "vtyp-009", "seq": 19},
]

# ============================================================
# Sentences
# ============================================================

SENTENCES = [
    # ----------------------------------------------------------
    # Exam_01 — Problem (1): 青山学院大学
    # ----------------------------------------------------------
    {
        "id": "haj-exam-01-q1-s1",
        "section_id": "Exam_01",
        "drill": 1,
        "number": 1,
        "role": "practice",
        "english": "The Internet is no longer concerned with information exchange alone.",
        "japanese": "インターネットは，もはや情報交換だけに関わっているわけではない。",
        "notes": "青山学院大学",
    },
    {
        "id": "haj-exam-01-q1-s2",
        "section_id": "Exam_01",
        "drill": 1,
        "number": 2,
        "role": "practice",
        "english": "It is a sophisticated tool enabling individuals to create content, communicate with one another, and even escape reality.",
        "japanese": "それ［インターネット］は，個々人がコンテンツを作成したり，お互いに意思を伝え合ったり，さらには現実から逃げたりすることさえも可能にする洗練された道具である。",
        "notes": "青山学院大学",
    },
    # ----------------------------------------------------------
    # Exam_01 — Problem (2): 中央大学
    # ----------------------------------------------------------
    {
        "id": "haj-exam-01-q2-s1",
        "section_id": "Exam_01",
        "drill": 2,
        "number": 1,
        "role": "practice",
        "english": "Having tasted the pleasure in mathematics he will not forget it easily and then there is a good chance that mathematics will become something for him: a hobby, or a tool of his profession, or his profession, or a great ambition.",
        "japanese": "数学で楽しさを味わえば，（その）人はその楽しさを容易には忘れないだろう。そして，数学がその人にとって重要なもの，すなわち，趣味，職業上の技能，職業，大きな野望の的になる可能性が十分にある。",
        "notes": "中央大学",
    },
    # ----------------------------------------------------------
    # Exam_01 — Problem (3): 同志社大学
    # ----------------------------------------------------------
    {
        "id": "haj-exam-01-q3-s1",
        "section_id": "Exam_01",
        "drill": 3,
        "number": 1,
        "role": "practice",
        "english": "Understanding how reading on paper differs from reading on screens requires some explanation of how the human brain interprets written language.",
        "japanese": "紙上で読むことと画面上で読むことがどのように異なるかを理解するためには，人間の脳が文字言語をどのように解釈しているかについて少し説明が必要である。",
        "notes": "同志社大学",
    },
    {
        "id": "haj-exam-01-q3-s2",
        "section_id": "Exam_01",
        "drill": 3,
        "number": 2,
        "role": "practice",
        "english": "Although letters and words are symbols representing sounds and ideas, the brain also regards them as physical objects.",
        "japanese": "文字や単語は，音や考えを表す記号であるが，脳は，それらを物理的な物であると見なしてもいる。",
        "notes": "同志社大学",
    },
    # ----------------------------------------------------------
    # Exam_01 — Problem (4): 神戸大学
    # ----------------------------------------------------------
    {
        "id": "haj-exam-01-q4-s1",
        "section_id": "Exam_01",
        "drill": 4,
        "number": 1,
        "role": "practice",
        "english": "As researchers, we aim to unravel how light pollution is affecting coastal and marine ecosystems.",
        "japanese": "研究者として，私たちは，光害が海岸沿いと海の生態系にどのように影響を与えているのかを解明しようと努力している。",
        "notes": "神戸大学",
    },
    {
        "id": "haj-exam-01-q4-s2",
        "section_id": "Exam_01",
        "drill": 4,
        "number": 2,
        "role": "practice",
        "english": "Only by understanding if, when and how light pollution affects nocturnal life can we find ways to mitigate the impact.",
        "japanese": "光害は，夜行性の生物に影響するのかどうか，いつ，どのように影響するのかを理解することによってのみ［理解することによってようやく］，私たちはその影響を緩和する方法を見つけることができる。",
        "notes": "神戸大学",
    },
    # ----------------------------------------------------------
    # Exam_02 — 共通テスト (oral health)
    # ----------------------------------------------------------
    {
        "id": "haj-exam-02-s01",
        "section_id": "Exam_02",
        "drill": 0,
        "number": 1,
        "role": "practice",
        "english": "In recent years, governments around the world have been working to raise awareness about oral health.",
        "japanese": "近年，世界中の政府は，口内の健康についての意識を高めるために努力している。",
        "notes": None,
    },
    {
        "id": "haj-exam-02-s02",
        "section_id": "Exam_02",
        "drill": 0,
        "number": 2,
        "role": "practice",
        "english": "While many people have heard that brushing their teeth multiple times per day is a good habit, they most likely have not considered all the reasons why this is crucial.",
        "japanese": "多くの人が，1日に複数回歯を磨くことは良い習慣であると聞いたことがあるが，彼らは，これが重要であるあらゆる理由について考えたことがない可能性が極めて高い。",
        "notes": None,
    },
    {
        "id": "haj-exam-02-s03",
        "section_id": "Exam_02",
        "drill": 0,
        "number": 3,
        "role": "practice",
        "english": "Simply stated, teeth are important.",
        "japanese": "簡単に言うと，歯は大切である。",
        "notes": None,
    },
    {
        "id": "haj-exam-02-s04",
        "section_id": "Exam_02",
        "drill": 0,
        "number": 4,
        "role": "practice",
        "english": "Teeth are required to pronounce words accurately.",
        "japanese": "単語を正確に発音するために，歯は必要である。",
        "notes": None,
    },
    {
        "id": "haj-exam-02-s05",
        "section_id": "Exam_02",
        "drill": 0,
        "number": 5,
        "role": "practice",
        "english": "In fact, poor oral health can actually make it difficult to speak.",
        "japanese": "実際，口内の健康状態が悪いと，話すことが難しくなる。",
        "notes": None,
    },
    {
        "id": "haj-exam-02-s06",
        "section_id": "Exam_02",
        "drill": 0,
        "number": 6,
        "role": "practice",
        "english": "An even more basic necessity is being able to chew well.",
        "japanese": "さらに基本的に必要なことは，うまく噛めることである。",
        "notes": None,
    },
    {
        "id": "haj-exam-02-s07",
        "section_id": "Exam_02",
        "drill": 0,
        "number": 7,
        "role": "practice",
        "english": "Chewing breaks food down and makes it easier for the body to digest it.",
        "japanese": "噛むことによって，食べ物が砕かれ，体がそれをより容易に消化できるようになる。",
        "notes": None,
    },
    {
        "id": "haj-exam-02-s08",
        "section_id": "Exam_02",
        "drill": 0,
        "number": 8,
        "role": "practice",
        "english": "Proper chewing is also linked to the enjoyment of food.",
        "japanese": "正しく噛むことは，食べ物を楽しむことにも関連している。",
        "notes": None,
    },
    {
        "id": "haj-exam-02-s09",
        "section_id": "Exam_02",
        "drill": 0,
        "number": 9,
        "role": "practice",
        "english": "The average person has experienced the frustration of not being able to chew on one side after a dental procedure.",
        "japanese": "普通の人は，歯の治療の後，一方の側で噛むことができないイライラを経験したことがある。",
        "notes": None,
    },
    {
        "id": "haj-exam-02-s10",
        "section_id": "Exam_02",
        "drill": 0,
        "number": 10,
        "role": "practice",
        "english": "A person with weak teeth may experience this disappointment all the time.",
        "japanese": "弱い歯を持っている人は，この落胆を常に経験するかもしれない。",
        "notes": None,
    },
    {
        "id": "haj-exam-02-s11",
        "section_id": "Exam_02",
        "drill": 0,
        "number": 11,
        "role": "practice",
        "english": "In other words, oral health impacts people's quality of life.",
        "japanese": "言い換えると，口内の健康は，人々の生活の質に影響するのである。",
        "notes": None,
    },
    {
        "id": "haj-exam-02-s12",
        "section_id": "Exam_02",
        "drill": 0,
        "number": 12,
        "role": "practice",
        "english": "Dentists have long recommended brushing after meals.",
        "japanese": "歯科医たちは，長らく，食事の後に歯を磨くことを推奨してきた。",
        "notes": None,
    },
    {
        "id": "haj-exam-02-s13",
        "section_id": "Exam_02",
        "drill": 0,
        "number": 13,
        "role": "practice",
        "english": "People actively seeking excellent oral health may brush several times per day.",
        "japanese": "積極的に素晴らしい口内の健康を得ようとしている人々は，1日に複数回歯を磨くかもしれない。",
        "notes": None,
    },
    {
        "id": "haj-exam-02-s14",
        "section_id": "Exam_02",
        "drill": 0,
        "number": 14,
        "role": "practice",
        "english": "Most brush their teeth before they go to sleep and then again at some time the following morning.",
        "japanese": "ほとんどの人々は，寝る前に歯を磨き，そして次の朝のある時に，再び歯を磨く。",
        "notes": None,
    },
    {
        "id": "haj-exam-02-s15",
        "section_id": "Exam_02",
        "drill": 0,
        "number": 15,
        "role": "practice",
        "english": "Dentists also believe it is important to floss daily, using a special type of string to remove substances from between teeth.",
        "japanese": "歯科医は，歯の間から物質を取り除くための特別なタイプの糸を使って，毎日フロスすることが重要であると信じてもいる。",
        "notes": None,
    },
    {
        "id": "haj-exam-02-s16",
        "section_id": "Exam_02",
        "drill": 0,
        "number": 16,
        "role": "practice",
        "english": "Another prevention method is for a dentist to seal the teeth using a plastic gel (sealant) that hardens around the tooth surface and prevents damage.",
        "japanese": "別の予防方法は，歯の表面の周りで固まり，損傷を防ぐ合成樹脂製のジェル（シーラント）を使って，歯科医が歯をコーティングすることである。",
        "notes": None,
    },
    {
        "id": "haj-exam-02-s17",
        "section_id": "Exam_02",
        "drill": 0,
        "number": 17,
        "role": "practice",
        "english": "Visiting the dentist annually or more frequently is key.",
        "japanese": "1年に1度，またはそれ以上の頻度で歯科医を訪れることが，重要である。",
        "notes": None,
    },
    {
        "id": "haj-exam-02-s18",
        "section_id": "Exam_02",
        "drill": 0,
        "number": 18,
        "role": "practice",
        "english": "As dental treatment sometimes causes pain, there are those who actively avoid seeing a dentist.",
        "japanese": "歯の治療は時々，痛みを引き起こすため，歯科医に診てもらうのを意図的に避ける人がいる。",
        "notes": None,
    },
    {
        "id": "haj-exam-02-s19",
        "section_id": "Exam_02",
        "drill": 0,
        "number": 19,
        "role": "practice",
        "english": "However, it is important that people start viewing their dentist as an important ally who can, literally, make them smile throughout their lives.",
        "japanese": "しかし，人々が，歯科医は，人生を通じて自分たちを文字通り笑顔にさせてくれる大切な味方であると見なし始めることが，重要である。",
        "notes": None,
    },
]

# ============================================================
# Sentence structures (label/value pairs)
# ============================================================

SENTENCE_STRUCTURES = [
    # --- Exam_01 q1-s1 ---
    {"sentence_id": "haj-exam-01-q1-s1", "label": "overall", "value": "S V M C M"},
    {"sentence_id": "haj-exam-01-q1-s1", "label": "details", "value": "The Internet(S) is(V) <no longer>(M) concerned(C) <with information exchange alone>(M)"},
    # --- Exam_01 q1-s2 ---
    {"sentence_id": "haj-exam-01-q1-s2", "label": "overall", "value": "S V C (M:形容詞句)"},
    {"sentence_id": "haj-exam-01-q1-s2", "label": "details", "value": "It(S) is(V) a sophisticated tool(C) (enabling individuals to create content, communicate with one another, and even escape reality)(M:形容詞句)"},
    {"sentence_id": "haj-exam-01-q1-s2", "label": "enabling_clause", "value": "enabling(V) individuals(O) to create content, communicate with one another, and even escape reality(C:並列)"},
    # --- Exam_01 q2-s1 ---
    {"sentence_id": "haj-exam-01-q2-s1", "label": "overall", "value": "M(分詞構文) S V O M + V S (that同格)"},
    {"sentence_id": "haj-exam-01-q2-s1", "label": "details", "value": "<Having tasted the pleasure in mathematics>(M:分詞構文) he(S) will not forget(V) it(O) <easily>(M) and <then>(M) there(形式) is(V) a good chance(S) [that mathematics will become something for him: a hobby, or a tool of his profession, or his profession, or a great ambition](同格)"},
    # --- Exam_01 q3-s1 ---
    {"sentence_id": "haj-exam-01-q3-s1", "label": "overall", "value": "[S:動名詞句 [名詞節how]] V O (M [名詞節how])"},
    {"sentence_id": "haj-exam-01-q3-s1", "label": "details", "value": "[Understanding [<how> reading <on paper> differs <from reading on screens>]](S:動名詞句) requires(V) some explanation(O) (of [<how> the human brain interprets written language])(M)"},
    # --- Exam_01 q3-s2 ---
    {"sentence_id": "haj-exam-01-q3-s2", "label": "overall", "value": "M(副詞節Although) S M V O C"},
    {"sentence_id": "haj-exam-01-q3-s2", "label": "details", "value": "<Although letters and words are symbols (representing sounds and ideas)>(M:副詞節) the brain(S) <also>(M) regards(V) them(O) as physical objects(C)"},
    # --- Exam_01 q4-s1 ---
    {"sentence_id": "haj-exam-01-q4-s1", "label": "overall", "value": "M S V [O:名詞節how]"},
    {"sentence_id": "haj-exam-01-q4-s1", "label": "details", "value": "<As researchers>(M) we(S) aim to unravel(V) [<how> light pollution is affecting coastal and marine ecosystems](O:名詞節)"},
    # --- Exam_01 q4-s2 ---
    {"sentence_id": "haj-exam-01-q4-s2", "label": "overall", "value": "M(Only+否定副詞→倒置) 疑問文語順: V S V O(M:形容詞句)"},
    {"sentence_id": "haj-exam-01-q4-s2", "label": "details", "value": "<Only by understanding [if, when and how light pollution affects nocturnal life]>(M:否定副詞) can(V) we(S) find(V) ways(O) (to mitigate the impact)(M:形容詞句)"},
    # --- Exam_02 s01 ---
    {"sentence_id": "haj-exam-02-s01", "label": "overall", "value": "M S M V M(不定詞:副詞句)"},
    {"sentence_id": "haj-exam-02-s01", "label": "details", "value": "<In recent years>(M) governments(S) <around the world>(M) have been working(V) <to raise awareness about oral health>(M:副詞句)"},
    # --- Exam_02 s02 ---
    {"sentence_id": "haj-exam-02-s02", "label": "overall", "value": "M(While副詞節[O:that名詞節[S:動名詞句]]) S M V O (M:why形容詞節)"},
    {"sentence_id": "haj-exam-02-s02", "label": "details", "value": "<While many people have heard [that [brushing their teeth multiple times per day](S:動名詞) is a good habit]>(M:副詞節) they(S) <most likely>(M) have not considered(V) all the reasons(O) (<why> this is crucial)(M:形容詞節)"},
    # --- Exam_02 s03 ---
    {"sentence_id": "haj-exam-02-s03", "label": "overall", "value": "M(分詞構文) S V C"},
    {"sentence_id": "haj-exam-02-s03", "label": "details", "value": "<Simply stated>(M:分詞構文) teeth(S) are(V) important(C)"},
    # --- Exam_02 s04 ---
    {"sentence_id": "haj-exam-02-s04", "label": "overall", "value": "S V M(不定詞:副詞句)"},
    {"sentence_id": "haj-exam-02-s04", "label": "details", "value": "Teeth(S) are required(V) <to pronounce words accurately>(M:副詞句)"},
    # --- Exam_02 s05 ---
    {"sentence_id": "haj-exam-02-s05", "label": "overall", "value": "M S V O C [真S:to不定詞]"},
    {"sentence_id": "haj-exam-02-s05", "label": "details", "value": "<In fact>(M) poor oral health(S) can <actually> make(V) it(O:形式) difficult(C) [to speak](真S)"},
    # --- Exam_02 s06 ---
    {"sentence_id": "haj-exam-02-s06", "label": "overall", "value": "S V C(動名詞句)"},
    {"sentence_id": "haj-exam-02-s06", "label": "details", "value": "An even more basic necessity(S) is(V) [being able to chew well](C:動名詞句)"},
    # --- Exam_02 s07 ---
    {"sentence_id": "haj-exam-02-s07", "label": "overall", "value": "S V O M + V O C [真S:for+不定詞]"},
    {"sentence_id": "haj-exam-02-s07", "label": "details", "value": "Chewing(S:動名詞) breaks(V) food(O) <down>(M) and makes(V) it(O:形式) easier(C) [for the body to digest it](真S)"},
    # --- Exam_02 s08 ---
    {"sentence_id": "haj-exam-02-s08", "label": "overall", "value": "S V M M"},
    {"sentence_id": "haj-exam-02-s08", "label": "details", "value": "Proper chewing(S) is(V) <also>(M) linked(V) <to the enjoyment of food>(M)"},
    # --- Exam_02 s09 ---
    {"sentence_id": "haj-exam-02-s09", "label": "overall", "value": "S V O (M:of動名詞) M M"},
    {"sentence_id": "haj-exam-02-s09", "label": "details", "value": "The average person(S) has experienced(V) the frustration(O) (of not being able to chew)(M前:動名詞) <on one side>(M) <after a dental procedure>(M)"},
    # --- Exam_02 s10 ---
    {"sentence_id": "haj-exam-02-s10", "label": "overall", "value": "S (M) V O M"},
    {"sentence_id": "haj-exam-02-s10", "label": "details", "value": "A person(S) (with weak teeth)(M) may experience(V) this disappointment(O) <all the time>(M)"},
    # --- Exam_02 s11 ---
    {"sentence_id": "haj-exam-02-s11", "label": "overall", "value": "M S V O"},
    {"sentence_id": "haj-exam-02-s11", "label": "details", "value": "<In other words>(M) oral health(S) impacts(V) people's quality of life(O)"},
    # --- Exam_02 s12 ---
    {"sentence_id": "haj-exam-02-s12", "label": "overall", "value": "S V M O(動名詞)"},
    {"sentence_id": "haj-exam-02-s12", "label": "details", "value": "Dentists(S) have(V) <long>(M) recommended(V) [brushing <after meals>](O:動名詞)"},
    # --- Exam_02 s13 ---
    {"sentence_id": "haj-exam-02-s13", "label": "overall", "value": "S (M:分詞形容詞句) V M"},
    {"sentence_id": "haj-exam-02-s13", "label": "details", "value": "People(S) (<actively> seeking excellent oral health)(M:形容詞句) may brush(V) <several times per day>(M)"},
    # --- Exam_02 s14 ---
    {"sentence_id": "haj-exam-02-s14", "label": "overall", "value": "S V O M(before副詞節) + M M M M"},
    {"sentence_id": "haj-exam-02-s14", "label": "details", "value": "Most(S) brush(V) their teeth(O) <before they go to sleep>(M:副詞節) and <then>(M) <again>(M) <at some time>(M) <the following morning>(M)"},
    # --- Exam_02 s15 ---
    {"sentence_id": "haj-exam-02-s15", "label": "overall", "value": "S M V O(形式it) [真S:to不定詞] M(分詞構文)"},
    {"sentence_id": "haj-exam-02-s15", "label": "details", "value": "Dentists(S) <also>(M) believe(V) it(O:形式) is important(C) [to floss <daily>](真S) <using a special type of string (to remove substances from between teeth)>(M:分詞構文)"},
    # --- Exam_02 s16 ---
    {"sentence_id": "haj-exam-02-s16", "label": "overall", "value": "S V C(for+不定詞句 [M:分詞構文 (M:that形容詞節)])"},
    {"sentence_id": "haj-exam-02-s16", "label": "details", "value": "Another prevention method(S) is(V) [for a dentist to seal the teeth <using a plastic gel (sealant) (that hardens around the tooth surface and prevents damage)>](C)"},
    # --- Exam_02 s17 ---
    {"sentence_id": "haj-exam-02-s17", "label": "overall", "value": "S(動名詞句) V C"},
    {"sentence_id": "haj-exam-02-s17", "label": "details", "value": "[Visiting the dentist <annually> or <more frequently>](S:動名詞句) is(V) key(C)"},
    # --- Exam_02 s18 ---
    {"sentence_id": "haj-exam-02-s18", "label": "overall", "value": "M(As副詞節) V S (M:who形容詞節[O:動名詞])"},
    {"sentence_id": "haj-exam-02-s18", "label": "details", "value": "<As dental treatment sometimes causes pain>(M:副詞節) there(形式) are(V) those(S) (who <actively> avoid [seeing a dentist])(M:形容詞節)"},
    # --- Exam_02 s19 ---
    {"sentence_id": "haj-exam-02-s19", "label": "overall", "value": "M S(形式it) V C [真S:that名詞節[O:動名詞[C:as+名詞(M:who形容詞節)]]]"},
    {"sentence_id": "haj-exam-02-s19", "label": "details", "value": "<However>(M) it(S:形式) is(V) important(C) [that people start [viewing their dentist as an important ally (who can, <literally>, make them smile <throughout their lives>)]](真S:that名詞節)"},
]

# ============================================================
# Sentence knowledge tags
# ============================================================

SENTENCE_KNOWLEDGE_TAGS = [
    # --- Exam_01 q1-s1 ---
    {"sentence_id": "haj-exam-01-q1-s1", "node_id": "strc-007"},
    {"sentence_id": "haj-exam-01-q1-s1", "node_id": "strc-008"},
    # --- Exam_01 q1-s2 ---
    {"sentence_id": "haj-exam-01-q1-s2", "node_id": "clau-034"},
    {"sentence_id": "haj-exam-01-q1-s2", "node_id": "vtyp-007"},
    {"sentence_id": "haj-exam-01-q1-s2", "node_id": "read-011"},
    # --- Exam_01 q2-s1 ---
    {"sentence_id": "haj-exam-01-q2-s1", "node_id": "clau-032"},
    {"sentence_id": "haj-exam-01-q2-s1", "node_id": "clau-039"},
    {"sentence_id": "haj-exam-01-q2-s1", "node_id": "read-010"},
    # --- Exam_01 q3-s1 ---
    {"sentence_id": "haj-exam-01-q3-s1", "node_id": "clau-004"},
    {"sentence_id": "haj-exam-01-q3-s1", "node_id": "clau-006"},
    {"sentence_id": "haj-exam-01-q3-s1", "node_id": "read-008"},
    # --- Exam_01 q3-s2 ---
    {"sentence_id": "haj-exam-01-q3-s2", "node_id": "clau-033"},
    {"sentence_id": "haj-exam-01-q3-s2", "node_id": "clau-034"},
    {"sentence_id": "haj-exam-01-q3-s2", "node_id": "strc-015"},
    # --- Exam_01 q4-s1 ---
    {"sentence_id": "haj-exam-01-q4-s1", "node_id": "strc-008"},
    {"sentence_id": "haj-exam-01-q4-s1", "node_id": "clau-006"},
    # --- Exam_01 q4-s2 ---
    {"sentence_id": "haj-exam-01-q4-s2", "node_id": "read-013"},
    {"sentence_id": "haj-exam-01-q4-s2", "node_id": "clau-007"},
    {"sentence_id": "haj-exam-01-q4-s2", "node_id": "clau-006"},
    {"sentence_id": "haj-exam-01-q4-s2", "node_id": "read-011"},
    {"sentence_id": "haj-exam-01-q4-s2", "node_id": "clau-028"},
    # --- Exam_02 s01 ---
    {"sentence_id": "haj-exam-02-s01", "node_id": "clau-031"},
    # --- Exam_02 s02 ---
    {"sentence_id": "haj-exam-02-s02", "node_id": "clau-033"},
    {"sentence_id": "haj-exam-02-s02", "node_id": "clau-007"},
    {"sentence_id": "haj-exam-02-s02", "node_id": "clau-004"},
    {"sentence_id": "haj-exam-02-s02", "node_id": "clau-036"},
    # --- Exam_02 s03 ---
    {"sentence_id": "haj-exam-02-s03", "node_id": "clau-032"},
    # --- Exam_02 s04 ---
    {"sentence_id": "haj-exam-02-s04", "node_id": "clau-031"},
    # --- Exam_02 s05 ---
    {"sentence_id": "haj-exam-02-s05", "node_id": "clau-013"},
    {"sentence_id": "haj-exam-02-s05", "node_id": "read-008"},
    # --- Exam_02 s06 ---
    {"sentence_id": "haj-exam-02-s06", "node_id": "clau-004"},
    # --- Exam_02 s07 ---
    {"sentence_id": "haj-exam-02-s07", "node_id": "clau-013"},
    {"sentence_id": "haj-exam-02-s07", "node_id": "subj-003"},
    {"sentence_id": "haj-exam-02-s07", "node_id": "read-008"},
    # --- Exam_02 s08 ---
    {"sentence_id": "haj-exam-02-s08", "node_id": "read-007"},
    # --- Exam_02 s09 ---
    {"sentence_id": "haj-exam-02-s09", "node_id": "clau-004"},
    # --- Exam_02 s10 ---
    {"sentence_id": "haj-exam-02-s10", "node_id": "strc-008"},
    # --- Exam_02 s11 ---
    {"sentence_id": "haj-exam-02-s11", "node_id": "strc-007"},
    # --- Exam_02 s12 ---
    {"sentence_id": "haj-exam-02-s12", "node_id": "clau-004"},
    # --- Exam_02 s13 ---
    {"sentence_id": "haj-exam-02-s13", "node_id": "clau-034"},
    # --- Exam_02 s14 ---
    {"sentence_id": "haj-exam-02-s14", "node_id": "clau-033"},
    # --- Exam_02 s15 ---
    {"sentence_id": "haj-exam-02-s15", "node_id": "clau-008"},
    {"sentence_id": "haj-exam-02-s15", "node_id": "clau-032"},
    {"sentence_id": "haj-exam-02-s15", "node_id": "clau-028"},
    # --- Exam_02 s16 ---
    {"sentence_id": "haj-exam-02-s16", "node_id": "subj-003"},
    {"sentence_id": "haj-exam-02-s16", "node_id": "clau-029"},
    # --- Exam_02 s17 ---
    {"sentence_id": "haj-exam-02-s17", "node_id": "clau-004"},
    # --- Exam_02 s18 ---
    {"sentence_id": "haj-exam-02-s18", "node_id": "clau-033"},
    {"sentence_id": "haj-exam-02-s18", "node_id": "vtyp-021"},
    {"sentence_id": "haj-exam-02-s18", "node_id": "clau-029"},
    # --- Exam_02 s19 ---
    {"sentence_id": "haj-exam-02-s19", "node_id": "clau-008"},
    {"sentence_id": "haj-exam-02-s19", "node_id": "strc-015"},
    {"sentence_id": "haj-exam-02-s19", "node_id": "vtyp-009"},
    {"sentence_id": "haj-exam-02-s19", "node_id": "clau-029"},
]


# ============================================================
# Helper functions
# ============================================================

def get_client():
    """Create a Supabase client from environment variables."""
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    if not url or not key:
        print("Error: SUPABASE_URL and SUPABASE_KEY must be set")
        sys.exit(1)
    return create_client(url, key)


def delete_existing(client):
    """Delete existing Exam data in reverse dependency order (idempotent)."""
    exam_sentence_prefix = "haj-exam-"
    exam_section_ids = ("Exam_01", "Exam_02")

    print("  Deleting sentence_knowledge_tags for Exam sentences...")
    client.table("sentence_knowledge_tags").delete().like(
        "sentence_id", f"{exam_sentence_prefix}%"
    ).execute()

    print("  Deleting sentence_structures for Exam sentences...")
    client.table("sentence_structures").delete().like(
        "sentence_id", f"{exam_sentence_prefix}%"
    ).execute()

    print("  Deleting sentences for Exam sections...")
    client.table("sentences").delete().in_(
        "section_id", list(exam_section_ids)
    ).execute()

    print("  Deleting section_knowledge_nodes for Exam sections...")
    client.table("section_knowledge_nodes").delete().in_(
        "section_id", list(exam_section_ids)
    ).execute()

    print("  Deleting section_prerequisites for Exam sections...")
    client.table("section_prerequisites").delete().in_(
        "section_id", list(exam_section_ids)
    ).execute()

    print("  Deleting sections for Exam...")
    client.table("sections").delete().in_(
        "id", list(exam_section_ids)
    ).execute()

    print("  Deletion complete.")


def insert_data(client):
    """Insert all Exam data."""
    print("\n--- Inserting sections ---")
    client.table("sections").insert(SECTIONS).execute()
    print(f"  sections: {len(SECTIONS)}")

    print("\n--- Inserting section_prerequisites ---")
    client.table("section_prerequisites").insert(SECTION_PREREQUISITES).execute()
    print(f"  section_prerequisites: {len(SECTION_PREREQUISITES)}")

    print("\n--- Inserting section_knowledge_nodes ---")
    client.table("section_knowledge_nodes").insert(SECTION_KNOWLEDGE_NODES).execute()
    print(f"  section_knowledge_nodes: {len(SECTION_KNOWLEDGE_NODES)}")

    print("\n--- Inserting sentences ---")
    client.table("sentences").insert(SENTENCES).execute()
    print(f"  sentences: {len(SENTENCES)}")

    print("\n--- Inserting sentence_structures ---")
    client.table("sentence_structures").insert(SENTENCE_STRUCTURES).execute()
    print(f"  sentence_structures: {len(SENTENCE_STRUCTURES)}")

    print("\n--- Inserting sentence_knowledge_tags ---")
    client.table("sentence_knowledge_tags").insert(SENTENCE_KNOWLEDGE_TAGS).execute()
    print(f"  sentence_knowledge_tags: {len(SENTENCE_KNOWLEDGE_TAGS)}")


def preview_data():
    """Preview all data without inserting (dry-run mode)."""
    print("\n=== DRY RUN: Preview of data to be inserted ===")

    print(f"\n--- Sections ({len(SECTIONS)}) ---")
    for s in SECTIONS:
        print(f"  {s['id']}: {s['title']} ({s['pages']}) type={s['type']}")

    print(f"\n--- Section prerequisites ({len(SECTION_PREREQUISITES)}) ---")
    for sp in SECTION_PREREQUISITES:
        print(f"  {sp['section_id']} requires {sp['prerequisite_id']}")

    print(f"\n--- Section knowledge nodes ({len(SECTION_KNOWLEDGE_NODES)}) ---")
    for sn in SECTION_KNOWLEDGE_NODES:
        print(f"  {sn['section_id']} -> {sn['node_id']} (seq={sn['seq']})")

    print(f"\n--- Sentences ({len(SENTENCES)}) ---")
    for s in SENTENCES:
        english_preview = s["english"][:60] + "..." if len(s["english"]) > 60 else s["english"]
        print(f"  {s['id']}: drill={s['drill']} num={s['number']} \"{english_preview}\"")

    print(f"\n--- Sentence structures ({len(SENTENCE_STRUCTURES)}) ---")
    for st in SENTENCE_STRUCTURES:
        value_preview = st["value"][:60] + "..." if len(st["value"]) > 60 else st["value"]
        print(f"  {st['sentence_id']}.{st['label']}: {value_preview}")

    print(f"\n--- Sentence knowledge tags ({len(SENTENCE_KNOWLEDGE_TAGS)}) ---")
    for t in SENTENCE_KNOWLEDGE_TAGS:
        print(f"  {t['sentence_id']} -> {t['node_id']}")

    print("\n=== Summary ===")
    print(f"  Sections:                {len(SECTIONS)}")
    print(f"  Section prerequisites:   {len(SECTION_PREREQUISITES)}")
    print(f"  Section knowledge nodes: {len(SECTION_KNOWLEDGE_NODES)}")
    print(f"  Sentences:               {len(SENTENCES)}")
    print(f"  Sentence structures:     {len(SENTENCE_STRUCTURES)}")
    print(f"  Sentence knowledge tags: {len(SENTENCE_KNOWLEDGE_TAGS)}")


# ============================================================
# Main
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description="Import Exam_01 and Exam_02 data into Supabase."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview data without inserting into Supabase.",
    )
    args = parser.parse_args()

    if args.dry_run:
        preview_data()
        return

    print("=== Exam Data Import ===")
    client = get_client()

    print("\nStep 1: Delete existing Exam data")
    delete_existing(client)

    print("\nStep 2: Insert Exam data")
    insert_data(client)

    print("\n=== Import complete! ===")


if __name__ == "__main__":
    main()
