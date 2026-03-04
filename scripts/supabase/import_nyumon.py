"""Import 入門英文問題精講 data into Supabase.

Phase F-2: Third textbook structuring with independent knowledge network.
Reads YAML files directly (unlike hijii which uses Python data modules).

Usage:
    python scripts/supabase/import_nyumon.py [--dry-run]

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
# Paths
# ============================================================

BASE_DIR = Path(__file__).resolve().parent / "nyumon_data"
KNOWLEDGE_DIR = BASE_DIR / "knowledge_nodes"
SENTENCES_DIR = BASE_DIR / "sentences"
SECTIONS_FILE = BASE_DIR / "sections.yaml"
CROSS_LINKS_FILE = BASE_DIR / "cross_book_links.yaml"

# Nyumon node/section/sentence prefixes for deletion
NYUMON_NODE_PREFIXES = ("nbk-", "nsv-", "njd-", "nks-", "nst-", "nhk-", "nta-")
NYUMON_SECTION_PREFIX = "Ny_"
NYUMON_SENTENCE_PREFIX = "ny-"


# ============================================================
# YAML Loading
# ============================================================

def load_yaml(path: Path) -> dict:
    """Load a YAML file."""
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def load_all_knowledge_data():
    """Load and merge all knowledge node YAML files."""
    nodes = []
    goals = []
    cps = []
    prereqs = []
    refs = []

    for f in sorted(KNOWLEDGE_DIR.glob("*.yaml")):
        data = load_yaml(f)
        nodes.extend(data.get("knowledge_nodes", []))
        goals.extend(data.get("understanding_goals", []))
        cps.extend(data.get("check_points", []))
        prereqs.extend(data.get("node_prerequisites", []))
        refs.extend(data.get("knowledge_references", []))

    return nodes, goals, cps, prereqs, refs


def load_all_sentence_data():
    """Load and merge all sentence YAML files."""
    sentences = []
    structures = []
    tags = []

    for f in sorted(SENTENCES_DIR.glob("*.yaml")):
        data = load_yaml(f)
        sentences.extend(data.get("sentences", []))
        structures.extend(data.get("sentence_structures", []))
        tags.extend(data.get("sentence_knowledge_tags", []))

    return sentences, structures, tags


def load_sections_data():
    """Load sections, section_knowledge_nodes, and section_prerequisites."""
    data = load_yaml(SECTIONS_FILE)

    # Sections: strip notes (not in DB schema) and ensure type field
    sections = []
    for s in data.get("sections", []):
        sections.append({
            "id": s["id"],
            "book": s["book"],
            "title": s["title"],
            "pages": s["pages"],
            "type": s.get("type", "exercise"),
        })

    sec_nodes = data.get("section_knowledge_nodes", [])

    # Section prerequisites: rename prerequisite_section_id → prerequisite_id
    sec_prereqs = []
    for sp in data.get("section_prerequisites", []):
        sec_prereqs.append({
            "section_id": sp["section_id"],
            "prerequisite_id": sp["prerequisite_section_id"],
        })

    return sections, sec_nodes, sec_prereqs


def load_cross_book_links():
    """Load cross-book links YAML."""
    if not CROSS_LINKS_FILE.exists():
        return []
    data = load_yaml(CROSS_LINKS_FILE)
    return data.get("cross_book_links", [])


# ============================================================
# Merge all data
# ============================================================

def deduplicate_refs(refs):
    """Deduplicate knowledge_references by (node_id, book).

    The DB has a UNIQUE constraint on (node_id, book).
    Nodes appearing in multiple sections are combined into one entry.
    """
    merged = {}
    for r in refs:
        key = (r["node_id"], r["book"])
        if key not in merged:
            merged[key] = dict(r)
        else:
            existing = merged[key]
            # Combine section_ids
            if r.get("section_id") and r["section_id"] not in (existing.get("section_id") or ""):
                existing["section_id"] = f"{existing.get('section_id', '')}, {r['section_id']}"
            # Combine pages
            if r.get("pages") and r["pages"] not in (existing.get("pages") or ""):
                existing["pages"] = f"{existing.get('pages', '')}, {r['pages']}"
    return list(merged.values())


ALL_NODES, ALL_GOALS, ALL_CHECKS, ALL_NODE_PREREQS, _RAW_REFS = load_all_knowledge_data()
ALL_REFS = deduplicate_refs(_RAW_REFS)
ALL_SENTENCES, ALL_STRUCTURES, ALL_TAGS = load_all_sentence_data()
ALL_SECTIONS, ALL_SEC_NODES, ALL_SEC_PREREQS = load_sections_data()
ALL_CROSS_LINKS = load_cross_book_links()


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
    """Delete existing Nyumon data in reverse dependency order (idempotent)."""
    print("  Deleting cross_book_links for Nyumon nodes...")
    for prefix in NYUMON_NODE_PREFIXES:
        client.table("cross_book_links").delete().like(
            "source_node", f"{prefix}%"
        ).execute()
        client.table("cross_book_links").delete().like(
            "target_node", f"{prefix}%"
        ).execute()

    print("  Deleting sentence_knowledge_tags for Nyumon sentences...")
    client.table("sentence_knowledge_tags").delete().like(
        "sentence_id", f"{NYUMON_SENTENCE_PREFIX}%"
    ).execute()

    print("  Deleting sentence_structures for Nyumon sentences...")
    client.table("sentence_structures").delete().like(
        "sentence_id", f"{NYUMON_SENTENCE_PREFIX}%"
    ).execute()

    nyumon_section_ids = [s["id"] for s in ALL_SECTIONS]
    if nyumon_section_ids:
        print("  Deleting sentences for Nyumon sections...")
        client.table("sentences").delete().in_(
            "section_id", nyumon_section_ids
        ).execute()

        print("  Deleting section_knowledge_nodes for Nyumon sections...")
        client.table("section_knowledge_nodes").delete().in_(
            "section_id", nyumon_section_ids
        ).execute()

        print("  Deleting section_prerequisites for Nyumon sections...")
        client.table("section_prerequisites").delete().in_(
            "section_id", nyumon_section_ids
        ).execute()

        print("  Deleting sections for Nyumon...")
        client.table("sections").delete().in_(
            "id", nyumon_section_ids
        ).execute()

    nyumon_node_ids = [n["id"] for n in ALL_NODES]
    if nyumon_node_ids:
        print("  Deleting knowledge_references for Nyumon nodes...")
        client.table("knowledge_references").delete().in_(
            "node_id", nyumon_node_ids
        ).execute()

        print("  Deleting check_points for Nyumon nodes...")
        client.table("check_points").delete().in_(
            "node_id", nyumon_node_ids
        ).execute()

        print("  Deleting understanding_goals for Nyumon nodes...")
        client.table("understanding_goals").delete().in_(
            "node_id", nyumon_node_ids
        ).execute()

        print("  Deleting knowledge_node_prerequisites for Nyumon nodes...")
        client.table("knowledge_node_prerequisites").delete().in_(
            "node_id", nyumon_node_ids
        ).execute()

        print("  Deleting knowledge_nodes for Nyumon...")
        client.table("knowledge_nodes").delete().in_(
            "id", nyumon_node_ids
        ).execute()

    print("  Deletion complete.")


def batch_insert(client, table, data, batch_size=100):
    """Insert data in batches to avoid request size limits."""
    for i in range(0, len(data), batch_size):
        batch = data[i:i + batch_size]
        client.table(table).insert(batch).execute()


def insert_data(client):
    """Insert all Nyumon data in dependency order."""
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
    batch_insert(client, "cross_book_links", ALL_CROSS_LINKS)
    print(f"  cross_book_links: {len(ALL_CROSS_LINKS)}")


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
    print(f"  Cross-book links:          {len(ALL_CROSS_LINKS)}")

    print("\n--- Nodes by category ---")
    categories = {}
    for n in ALL_NODES:
        categories[n["category"]] = categories.get(n["category"], 0) + 1
    for cat, cnt in sorted(categories.items()):
        print(f"  {cat}: {cnt}")

    print(f"\n--- Sections ({len(ALL_SECTIONS)}) ---")
    for s in ALL_SECTIONS[:5]:
        print(f"  {s['id']}: {s['title']} ({s['pages']}) type={s['type']}")
    if len(ALL_SECTIONS) > 5:
        print(f"  ... and {len(ALL_SECTIONS) - 5} more")

    print(f"\n--- Sentences ({len(ALL_SENTENCES)}) ---")
    for s in ALL_SENTENCES[:5]:
        eng = s["english"][:60] + "..." if len(s["english"]) > 60 else s["english"]
        print(f"  {s['id']}: drill={s['drill']} \"{eng}\"")
    if len(ALL_SENTENCES) > 5:
        print(f"  ... and {len(ALL_SENTENCES) - 5} more")


# ============================================================
# Main
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description="Import 入門英文問題精講 data into Supabase."
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

    print("=== Nyumon Data Import ===")

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

    print("\nStep 1: Delete existing Nyumon data")
    delete_existing(client)

    print("\nStep 2: Insert Nyumon data")
    insert_data(client)

    print("\n=== Import complete! ===")
    print(f"  Nodes: {len(ALL_NODES)}")
    print(f"  Sections: {len(ALL_SECTIONS)}")
    print(f"  Sentences: {len(ALL_SENTENCES)}")
    print(f"  Cross-book links: {len(ALL_CROSS_LINKS)}")


if __name__ == "__main__":
    main()
