"""参考書間リンク: 肘井 ↔ はじめの英文読解ドリル"""

# ============================================================
# CROSS_BOOK_LINKS
# ============================================================
# link_type: same_concept / extends / prerequisite
#
# same_concept: ほぼ同じ知識を扱っている
# extends: 一方が他方を詳細化・発展させている
# prerequisite: 一方が他方の前提知識になっている

CROSS_BOOK_LINKS = [
    # ----------------------------------------------------------
    # same_concept: 句と節の認識
    # ----------------------------------------------------------
    # 肘井 hch (名詞句) ↔ はじめ clau (句と節)
    {"source_node": "hch-001", "target_node": "clau-001", "link_type": "same_concept",
     "notes": "動名詞の名詞句 — 両書とも動名詞がS/O/Cになることを扱う"},
    {"source_node": "hch-002", "target_node": "clau-002", "link_type": "same_concept",
     "notes": "不定詞の名詞的用法 — 両書ともto不定詞がS/O/Cになることを扱う"},
    {"source_node": "hch-003", "target_node": "clau-006", "link_type": "same_concept",
     "notes": "名詞節(that/what/how等) — 両書とも名詞節の認識を扱う"},

    # 肘井 hch (形容詞句/節) ↔ はじめ clau (形容詞関連)
    {"source_node": "hch-004", "target_node": "clau-009", "link_type": "same_concept",
     "notes": "形容詞句（前置詞句・分詞・不定詞の後置修飾）"},
    {"source_node": "hch-005", "target_node": "clau-013", "link_type": "same_concept",
     "notes": "形容詞節（関係代名詞・関係副詞）"},

    # 肘井 hch (副詞句/節) ↔ はじめ clau (副詞関連)
    {"source_node": "hch-006", "target_node": "clau-028", "link_type": "same_concept",
     "notes": "副詞句（前置詞句・不定詞の副詞的用法等）"},
    {"source_node": "hch-007", "target_node": "clau-033", "link_type": "same_concept",
     "notes": "副詞節（時・条件・譲歩等の接続詞）"},

    # ----------------------------------------------------------
    # same_concept: 動詞の型
    # ----------------------------------------------------------
    {"source_node": "hvp-001", "target_node": "strc-013", "link_type": "same_concept",
     "notes": "第4文型 SVOO"},
    {"source_node": "hvp-002", "target_node": "strc-015", "link_type": "same_concept",
     "notes": "第5文型 SVOC"},
    {"source_node": "hvp-003", "target_node": "vtyp-001", "link_type": "same_concept",
     "notes": "SVO to do型の動詞パターン"},

    # ----------------------------------------------------------
    # same_concept: 構文
    # ----------------------------------------------------------
    {"source_node": "hco-002", "target_node": "read-013", "link_type": "same_concept",
     "notes": "倒置構文（否定副詞の倒置等）"},
    {"source_node": "hco-004", "target_node": "read-011", "link_type": "same_concept",
     "notes": "強調構文 It is ... that ~"},

    # ----------------------------------------------------------
    # extends: 肘井が詳細化
    # ----------------------------------------------------------
    # 識別テクニック（肘井独自の体系化）
    {"source_node": "hid-001", "target_node": "clau-001", "link_type": "extends",
     "notes": "肘井はto doの3用法識別テクニックを体系化。はじめは用法ごとの解説"},
    {"source_node": "hid-002", "target_node": "clau-004", "link_type": "extends",
     "notes": "肘井は-ingの識別テクニックを体系化（動名詞/現在分詞/分詞構文）"},
    {"source_node": "hid-004", "target_node": "clau-006", "link_type": "extends",
     "notes": "肘井はthatの多義性識別に特化（名詞節/形容詞節/副詞節/強調構文/同格）"},

    # ----------------------------------------------------------
    # extends: はじめが詳細化
    # ----------------------------------------------------------
    {"source_node": "hsv-002", "target_node": "clau-034", "link_type": "extends",
     "notes": "はじめは過去分詞の形容詞用法をより詳細に扱う（分詞の形容詞用法）"},

    # ----------------------------------------------------------
    # prerequisite: 肘井の基礎 → はじめの応用
    # ----------------------------------------------------------
    {"source_node": "hsv-000", "target_node": "strc-001", "link_type": "same_concept",
     "notes": "文の要素(SVOCM)の基礎概念 — 両書の出発点"},
]
