"""Table constants: insertion order, deletion order, FK dependency map."""

# Insert order: parents before children (FK targets before FK sources).
INSERTION_ORDER: list[str] = [
    "knowledge_nodes",
    "knowledge_node_prerequisites",
    "understanding_goals",
    "check_points",
    "knowledge_references",
    "sections",
    "section_knowledge_nodes",
    "section_prerequisites",
    "sentences",
    "sentence_structures",
    "sentence_knowledge_tags",
]

# Delete order: children before parents (reverse of insertion).
DELETION_ORDER: list[str] = list(reversed(INSERTION_ORDER))

# BookData attribute name for each table.
BOOKDATA_ATTR: dict[str, str] = {
    "knowledge_nodes": "knowledge_nodes",
    "knowledge_node_prerequisites": "node_prerequisites",
    "understanding_goals": "understanding_goals",
    "check_points": "check_points",
    "knowledge_references": "knowledge_references",
    "sections": "sections",
    "section_knowledge_nodes": "section_knowledge_nodes",
    "section_prerequisites": "section_prerequisites",
    "sentences": "sentences",
    "sentence_structures": "sentence_structures",
    "sentence_knowledge_tags": "sentence_knowledge_tags",
}

# Deletion filters: table → (filter_column, id_source).
# id_source is one of "sections", "knowledge_nodes", "sentences" — the set
# of IDs fetched from DB during the discover phase.
DELETION_FILTERS: dict[str, tuple[str, str]] = {
    "sentence_knowledge_tags": ("sentence_id", "sentences"),
    "sentence_structures": ("sentence_id", "sentences"),
    "sentences": ("section_id", "sections"),
    "section_prerequisites": ("section_id", "sections"),
    "section_knowledge_nodes": ("section_id", "sections"),
    "sections": ("id", "sections"),
    "knowledge_references": ("node_id", "knowledge_nodes"),
    "check_points": ("node_id", "knowledge_nodes"),
    "understanding_goals": ("node_id", "knowledge_nodes"),
    "knowledge_node_prerequisites": ("node_id", "knowledge_nodes"),
    "knowledge_nodes": ("id", "knowledge_nodes"),
}
