"""Import 肘井の読解のための英文法 data into Supabase.

Phase F: Second textbook structuring with independent knowledge network.

Usage:
    python scripts/supabase/import_hijii.py [--dry-run]

Environment variables:
    SUPABASE_URL  - Supabase project URL
    SUPABASE_KEY  - Supabase service_role key
"""

import argparse
import os
import sys

from supabase import create_client

# Import chapter data modules
from hijii_data import ch0_sv_discovery
from hijii_data import ch1_t02_03, ch1_t04_05, ch1_t06_07
from hijii_data import ch2_t08_10, ch2_t11_13
from hijii_data import ch3_t14_17, ch3_t18_22
from hijii_data import ch4_t23_28, ch4_t29_33
from hijii_data.cross_book_links import CROSS_BOOK_LINKS


# ============================================================
# Merge all chapter data
# ============================================================

_ALL_MODULES = [
    ch0_sv_discovery,
    ch1_t02_03, ch1_t04_05, ch1_t06_07,
    ch2_t08_10, ch2_t11_13,
    ch3_t14_17, ch3_t18_22,
    ch4_t23_28, ch4_t29_33,
]


def _merge(attr):
    """Merge a list attribute from all data modules."""
    result = []
    for mod in _ALL_MODULES:
        result.extend(getattr(mod, attr))
    return result


ALL_NODES = _merge("KNOWLEDGE_NODES")
ALL_GOALS = _merge("UNDERSTANDING_GOALS")
ALL_CHECKS = _merge("CHECK_POINTS")
ALL_NODE_PREREQS = _merge("NODE_PREREQUISITES")
ALL_REFS = _merge("KNOWLEDGE_REFERENCES")
ALL_SECTIONS = _merge("SECTIONS")
ALL_SEC_PREREQS = _merge("SECTION_PREREQUISITES")
ALL_SEC_NODES = _merge("SECTION_KNOWLEDGE_NODES")
ALL_SENTENCES = _merge("SENTENCES")
ALL_STRUCTURES = _merge("SENTENCE_STRUCTURES")
ALL_TAGS = _merge("SENTENCE_KNOWLEDGE_TAGS")

# Hijii node ID prefixes for deletion
HIJII_NODE_PREFIXES = ("hsv-", "hch-", "hid-", "hco-", "hvp-")
HIJII_SECTION_PREFIX = "Hij_"
HIJII_SENTENCE_PREFIX = "hij-"


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
    """Delete existing Hijii data in reverse dependency order (idempotent)."""
    print("  Deleting cross_book_links for Hijii nodes...")
    for prefix in HIJII_NODE_PREFIXES:
        client.table("cross_book_links").delete().like(
            "source_node", f"{prefix}%"
        ).execute()
        client.table("cross_book_links").delete().like(
            "target_node", f"{prefix}%"
        ).execute()

    print("  Deleting sentence_knowledge_tags for Hijii sentences...")
    client.table("sentence_knowledge_tags").delete().like(
        "sentence_id", f"{HIJII_SENTENCE_PREFIX}%"
    ).execute()

    print("  Deleting sentence_structures for Hijii sentences...")
    client.table("sentence_structures").delete().like(
        "sentence_id", f"{HIJII_SENTENCE_PREFIX}%"
    ).execute()

    print("  Deleting sentences for Hijii sections...")
    hijii_section_ids = [s["id"] for s in ALL_SECTIONS]
    if hijii_section_ids:
        client.table("sentences").delete().in_(
            "section_id", hijii_section_ids
        ).execute()

    print("  Deleting section_knowledge_nodes for Hijii sections...")
    if hijii_section_ids:
        client.table("section_knowledge_nodes").delete().in_(
            "section_id", hijii_section_ids
        ).execute()

    print("  Deleting section_prerequisites for Hijii sections...")
    if hijii_section_ids:
        client.table("section_prerequisites").delete().in_(
            "section_id", hijii_section_ids
        ).execute()

    print("  Deleting sections for Hijii...")
    if hijii_section_ids:
        client.table("sections").delete().in_(
            "id", hijii_section_ids
        ).execute()

    print("  Deleting knowledge_references for Hijii nodes...")
    hijii_node_ids = [n["id"] for n in ALL_NODES]
    if hijii_node_ids:
        client.table("knowledge_references").delete().in_(
            "node_id", hijii_node_ids
        ).execute()

    print("  Deleting check_points for Hijii nodes...")
    if hijii_node_ids:
        client.table("check_points").delete().in_(
            "node_id", hijii_node_ids
        ).execute()

    print("  Deleting understanding_goals for Hijii nodes...")
    if hijii_node_ids:
        client.table("understanding_goals").delete().in_(
            "node_id", hijii_node_ids
        ).execute()

    print("  Deleting knowledge_node_prerequisites for Hijii nodes...")
    if hijii_node_ids:
        client.table("knowledge_node_prerequisites").delete().in_(
            "node_id", hijii_node_ids
        ).execute()

    print("  Deleting knowledge_nodes for Hijii...")
    if hijii_node_ids:
        client.table("knowledge_nodes").delete().in_(
            "id", hijii_node_ids
        ).execute()

    print("  Deletion complete.")


def batch_insert(client, table, data, batch_size=100):
    """Insert data in batches to avoid request size limits."""
    for i in range(0, len(data), batch_size):
        batch = data[i:i + batch_size]
        client.table(table).insert(batch).execute()


def insert_data(client):
    """Insert all Hijii data."""
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

    print("\n--- Inserting cross_book_links ---")
    batch_insert(client, "cross_book_links", CROSS_BOOK_LINKS)
    print(f"  cross_book_links: {len(CROSS_BOOK_LINKS)}")


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
        description="Import 肘井の読解のための英文法 data into Supabase."
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

    print("=== Hijii Data Import ===")

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

    print("\nStep 1: Delete existing Hijii data")
    delete_existing(client)

    print("\nStep 2: Insert Hijii data")
    insert_data(client)

    print("\n=== Import complete! ===")
    print(f"  Nodes: {len(ALL_NODES)}")
    print(f"  Sections: {len(ALL_SECTIONS)}")
    print(f"  Sentences: {len(ALL_SENTENCES)}")
    print(f"  Cross-book links: {len(CROSS_BOOK_LINKS)}")


if __name__ == "__main__":
    main()
