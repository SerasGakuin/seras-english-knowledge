"""Import 英文法の核心 data into Supabase.

Phase F: Third textbook structuring with independent knowledge network.
Data source: YAML files in kakushin_data/ directory.

Usage:
    python scripts/supabase/import_kakushin.py [--dry-run]

Environment variables:
    SUPABASE_URL  - Supabase project URL
    SUPABASE_KEY  - Supabase service_role key
"""

import argparse
import os
import sys
from pathlib import Path

import yaml
from supabase import create_client

# ============================================================
# YAML data loading
# ============================================================

DATA_DIR = Path(__file__).parent / "kakushin_data"


def load_yaml(path: Path) -> dict:
    """Load a YAML file and return its contents."""
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def _load_knowledge_nodes():
    """Load and merge knowledge_nodes from part1~part4.yaml."""
    nodes_dir = DATA_DIR / "knowledge_nodes"
    all_nodes = []
    all_goals = []
    all_checks = []
    all_node_prereqs = []
    all_refs = []

    for part_file in sorted(nodes_dir.glob("part*.yaml")):
        data = load_yaml(part_file)
        all_nodes.extend(data.get("knowledge_nodes", []))
        all_goals.extend(data.get("understanding_goals", []))
        all_checks.extend(data.get("check_points", []))
        all_node_prereqs.extend(data.get("node_prerequisites", []))
        all_refs.extend(data.get("knowledge_references", []))

    return all_nodes, all_goals, all_checks, all_node_prereqs, all_refs


def _load_sentences():
    """Load and merge sentences from kaku_*.yaml files."""
    sentences_dir = DATA_DIR / "sentences"
    all_sentences = []
    all_structures = []
    all_tags = []

    for sent_file in sorted(sentences_dir.glob("kaku_*.yaml")):
        data = load_yaml(sent_file)
        all_sentences.extend(data.get("sentences", []))
        all_structures.extend(data.get("sentence_structures", []))
        all_tags.extend(data.get("sentence_knowledge_tags", []))

    return all_sentences, all_structures, all_tags


def _load_sections():
    """Load sections, section_knowledge_nodes, section_prerequisites."""
    data = load_yaml(DATA_DIR / "sections.yaml")
    sections = data.get("sections", [])
    sec_nodes = data.get("section_knowledge_nodes", [])
    sec_prereqs = data.get("section_prerequisites", [])
    return sections, sec_nodes, sec_prereqs


def _load_cross_book_links():
    """Load cross_book_links if the file exists."""
    links_path = DATA_DIR / "cross_book_links.yaml"
    if not links_path.exists():
        return []
    data = load_yaml(links_path)
    return data.get("cross_book_links", [])


# ============================================================
# Merge all data
# ============================================================

ALL_NODES, ALL_GOALS, ALL_CHECKS, ALL_NODE_PREREQS, ALL_REFS = _load_knowledge_nodes()
ALL_SENTENCES, ALL_STRUCTURES, ALL_TAGS = _load_sentences()
ALL_SECTIONS, ALL_SEC_NODES, ALL_SEC_PREREQS = _load_sections()
CROSS_BOOK_LINKS = _load_cross_book_links()

# Normalize sentences: number defaults to 0, notes defaults to None, strip extra fields
_SENTENCE_FIELDS = {"id", "section_id", "drill", "number", "role", "english", "japanese", "notes"}
for s in ALL_SENTENCES:
    if s.get("number") is None:
        s["number"] = 0
    if s.get("drill") is None:
        s["drill"] = 0
    if not s.get("notes"):
        s["notes"] = None
    # Remove fields not in DB schema (e.g. 'book' added in some YAML files)
    extra_keys = set(s.keys()) - _SENTENCE_FIELDS
    for k in extra_keys:
        del s[k]

# Kakushin node ID prefixes for deletion
KAKUSHIN_NODE_PREFIXES = ("khs-", "kvt-", "kjd-", "kta-")
KAKUSHIN_SECTION_PREFIX = "Kaku_"
KAKUSHIN_SENTENCE_PREFIX = "kaku-"


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
    """Delete existing Kakushin data in reverse dependency order (idempotent)."""
    print("  Deleting cross_book_links for Kakushin nodes...")
    for prefix in KAKUSHIN_NODE_PREFIXES:
        client.table("cross_book_links").delete().like(
            "source_node", f"{prefix}%"
        ).execute()
        client.table("cross_book_links").delete().like(
            "target_node", f"{prefix}%"
        ).execute()

    print("  Deleting sentence_knowledge_tags for Kakushin sentences...")
    client.table("sentence_knowledge_tags").delete().like(
        "sentence_id", f"{KAKUSHIN_SENTENCE_PREFIX}%"
    ).execute()

    print("  Deleting sentence_structures for Kakushin sentences...")
    client.table("sentence_structures").delete().like(
        "sentence_id", f"{KAKUSHIN_SENTENCE_PREFIX}%"
    ).execute()

    print("  Deleting sentences for Kakushin sections...")
    kakushin_section_ids = [s["id"] for s in ALL_SECTIONS]
    if kakushin_section_ids:
        client.table("sentences").delete().in_(
            "section_id", kakushin_section_ids
        ).execute()

    print("  Deleting section_knowledge_nodes for Kakushin sections...")
    if kakushin_section_ids:
        client.table("section_knowledge_nodes").delete().in_(
            "section_id", kakushin_section_ids
        ).execute()

    print("  Deleting section_prerequisites for Kakushin sections...")
    if kakushin_section_ids:
        client.table("section_prerequisites").delete().in_(
            "section_id", kakushin_section_ids
        ).execute()

    print("  Deleting sections for Kakushin...")
    if kakushin_section_ids:
        client.table("sections").delete().in_(
            "id", kakushin_section_ids
        ).execute()

    print("  Deleting knowledge_references for Kakushin nodes...")
    kakushin_node_ids = [n["id"] for n in ALL_NODES]
    if kakushin_node_ids:
        client.table("knowledge_references").delete().in_(
            "node_id", kakushin_node_ids
        ).execute()

    print("  Deleting check_points for Kakushin nodes...")
    if kakushin_node_ids:
        client.table("check_points").delete().in_(
            "node_id", kakushin_node_ids
        ).execute()

    print("  Deleting understanding_goals for Kakushin nodes...")
    if kakushin_node_ids:
        client.table("understanding_goals").delete().in_(
            "node_id", kakushin_node_ids
        ).execute()

    print("  Deleting knowledge_node_prerequisites for Kakushin nodes...")
    if kakushin_node_ids:
        client.table("knowledge_node_prerequisites").delete().in_(
            "node_id", kakushin_node_ids
        ).execute()

    print("  Deleting knowledge_nodes for Kakushin...")
    if kakushin_node_ids:
        client.table("knowledge_nodes").delete().in_(
            "id", kakushin_node_ids
        ).execute()

    print("  Deletion complete.")


def batch_insert(client, table, data, batch_size=100):
    """Insert data in batches to avoid request size limits."""
    for i in range(0, len(data), batch_size):
        batch = data[i:i + batch_size]
        client.table(table).insert(batch).execute()


def insert_data(client):
    """Insert all Kakushin data."""
    print("\n--- Inserting knowledge_nodes ---")
    batch_insert(client, "knowledge_nodes", ALL_NODES)
    print(f"  knowledge_nodes: {len(ALL_NODES)}")

    print("\n--- Inserting knowledge_node_prerequisites ---")
    batch_insert(client, "knowledge_node_prerequisites", ALL_NODE_PREREQS)
    print(f"  knowledge_node_prerequisites: {len(ALL_NODE_PREREQS)}")

    print("\n--- Inserting understanding_goals ---")
    batch_insert(client, "understanding_goals", ALL_GOALS)
    print(f"  understanding_goals: {len(ALL_GOALS)}")

    print("\n--- Inserting check_points ---")
    batch_insert(client, "check_points", ALL_CHECKS)
    print(f"  check_points: {len(ALL_CHECKS)}")

    print("\n--- Inserting knowledge_references ---")
    batch_insert(client, "knowledge_references", ALL_REFS)
    print(f"  knowledge_references: {len(ALL_REFS)}")

    print("\n--- Inserting sections ---")
    batch_insert(client, "sections", ALL_SECTIONS)
    print(f"  sections: {len(ALL_SECTIONS)}")

    print("\n--- Inserting section_prerequisites ---")
    batch_insert(client, "section_prerequisites", ALL_SEC_PREREQS)
    print(f"  section_prerequisites: {len(ALL_SEC_PREREQS)}")

    print("\n--- Inserting section_knowledge_nodes ---")
    batch_insert(client, "section_knowledge_nodes", ALL_SEC_NODES)
    print(f"  section_knowledge_nodes: {len(ALL_SEC_NODES)}")

    print("\n--- Inserting sentences ---")
    batch_insert(client, "sentences", ALL_SENTENCES)
    print(f"  sentences: {len(ALL_SENTENCES)}")

    print("\n--- Inserting sentence_structures ---")
    batch_insert(client, "sentence_structures", ALL_STRUCTURES)
    print(f"  sentence_structures: {len(ALL_STRUCTURES)}")

    print("\n--- Inserting sentence_knowledge_tags ---")
    batch_insert(client, "sentence_knowledge_tags", ALL_TAGS)
    print(f"  sentence_knowledge_tags: {len(ALL_TAGS)}")

    if CROSS_BOOK_LINKS:
        print("\n--- Inserting cross_book_links ---")
        batch_insert(client, "cross_book_links", CROSS_BOOK_LINKS)
        print(f"  cross_book_links: {len(CROSS_BOOK_LINKS)}")
    else:
        print("\n--- No cross_book_links to insert ---")


def validate_data():
    """Run basic validation checks on the data before inserting."""
    errors = []

    # Check for duplicate IDs
    node_ids = [n["id"] for n in ALL_NODES]
    if len(node_ids) != len(set(node_ids)):
        dupes = [x for x in node_ids if node_ids.count(x) > 1]
        errors.append(f"Duplicate node IDs: {set(dupes)}")

    section_ids = [s["id"] for s in ALL_SECTIONS]
    if len(section_ids) != len(set(section_ids)):
        dupes = [x for x in section_ids if section_ids.count(x) > 1]
        errors.append(f"Duplicate section IDs: {set(dupes)}")

    sentence_ids = [s["id"] for s in ALL_SENTENCES]
    if len(sentence_ids) != len(set(sentence_ids)):
        dupes = [x for x in sentence_ids if sentence_ids.count(x) > 1]
        errors.append(f"Duplicate sentence IDs: {set(dupes)}")

    # Check FK references
    node_id_set = set(node_ids)
    section_id_set = set(section_ids)
    sentence_id_set = set(sentence_ids)

    for g in ALL_GOALS:
        if g["node_id"] not in node_id_set:
            errors.append(f"Goal references missing node: {g['node_id']}")

    for c in ALL_CHECKS:
        if c["node_id"] not in node_id_set:
            errors.append(f"Check references missing node: {c['node_id']}")

    for p in ALL_NODE_PREREQS:
        if p["node_id"] not in node_id_set:
            errors.append(f"Node prereq references missing node: {p['node_id']}")
        if p["prerequisite_id"] not in node_id_set:
            errors.append(f"Node prereq references missing prerequisite: {p['prerequisite_id']}")

    for s in ALL_SENTENCES:
        if s["section_id"] not in section_id_set:
            errors.append(f"Sentence {s['id']} references missing section: {s['section_id']}")

    for st in ALL_STRUCTURES:
        if st["sentence_id"] not in sentence_id_set:
            errors.append(f"Structure references missing sentence: {st['sentence_id']}")

    for t in ALL_TAGS:
        if t["sentence_id"] not in sentence_id_set:
            errors.append(f"Tag references missing sentence: {t['sentence_id']}")
        if t["node_id"] not in node_id_set:
            errors.append(f"Tag references missing node: {t['node_id']}")

    for sn in ALL_SEC_NODES:
        if sn["section_id"] not in section_id_set:
            errors.append(f"Section node references missing section: {sn['section_id']}")
        if sn["node_id"] not in node_id_set:
            errors.append(f"Section node references missing node: {sn['node_id']}")

    for sp in ALL_SEC_PREREQS:
        if sp["section_id"] not in section_id_set:
            errors.append(f"Section prereq references missing section: {sp['section_id']}")
        if sp["prerequisite_id"] not in section_id_set:
            errors.append(f"Section prereq references missing prerequisite: {sp['prerequisite_id']}")

    return errors


def preview_data():
    """Preview all data without inserting (dry-run mode)."""
    print("\n=== DRY RUN: Validation ===")
    errors = validate_data()
    if errors:
        print(f"\n  ERRORS ({len(errors)}):")
        for e in errors[:20]:
            print(f"    - {e}")
        if len(errors) > 20:
            print(f"    ... and {len(errors) - 20} more")
    else:
        print("  All validation checks passed!")

    print("\n=== DRY RUN: Data Summary ===")
    print(f"  Knowledge nodes:           {len(ALL_NODES)}")
    print(f"  Understanding goals:       {len(ALL_GOALS)}")
    print(f"  Check points:              {len(ALL_CHECKS)}")
    print(f"  Node prerequisites:        {len(ALL_NODE_PREREQS)}")
    print(f"  Knowledge references:      {len(ALL_REFS)}")
    print(f"  Sections:                  {len(ALL_SECTIONS)}")
    print(f"  Section prerequisites:     {len(ALL_SEC_PREREQS)}")
    print(f"  Section knowledge nodes:   {len(ALL_SEC_NODES)}")
    print(f"  Sentences:                 {len(ALL_SENTENCES)}")
    print(f"  Sentence structures:       {len(ALL_STRUCTURES)}")
    print(f"  Sentence knowledge tags:   {len(ALL_TAGS)}")
    print(f"  Cross-book links:          {len(CROSS_BOOK_LINKS)}")

    print("\n--- Nodes by category ---")
    categories = {}
    for n in ALL_NODES:
        categories[n["category"]] = categories.get(n["category"], 0) + 1
    for cat, cnt in sorted(categories.items()):
        print(f"  {cat}: {cnt}")

    print("\n--- Sections ---")
    for s in ALL_SECTIONS:
        print(f"  {s['id']}: {s['title']} ({s['pages']}) type={s['type']}")

    print(f"\n--- Sentences ({len(ALL_SENTENCES)}) ---")
    for s in ALL_SENTENCES[:5]:
        english_preview = s["english"][:60] + "..." if len(s["english"]) > 60 else s["english"]
        print(f"  {s['id']}: drill={s['drill']} \"{english_preview}\"")
    if len(ALL_SENTENCES) > 5:
        print(f"  ... and {len(ALL_SENTENCES) - 5} more")


# ============================================================
# Main
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description="Import 英文法の核心 data into Supabase."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview and validate data without inserting into Supabase.",
    )
    args = parser.parse_args()

    if args.dry_run:
        preview_data()
        return

    print("=== Kakushin Data Import ===")

    # Validate first
    print("\nStep 0: Validate data")
    errors = validate_data()
    if errors:
        print(f"\n  ERRORS ({len(errors)}):")
        for e in errors:
            print(f"    - {e}")
        print("\nAborting import due to validation errors.")
        sys.exit(1)
    print("  Validation passed!")

    client = get_client()

    print("\nStep 1: Delete existing Kakushin data")
    delete_existing(client)

    print("\nStep 2: Insert Kakushin data")
    insert_data(client)

    print("\n=== Import complete! ===")
    print(f"  Nodes: {len(ALL_NODES)}")
    print(f"  Sections: {len(ALL_SECTIONS)}")
    print(f"  Sentences: {len(ALL_SENTENCES)}")
    print(f"  Cross-book links: {len(CROSS_BOOK_LINKS)}")


if __name__ == "__main__":
    main()
