"""Import YAML data into Supabase.

Usage:
    python scripts/supabase/import_to_supabase.py

Environment variables:
    SUPABASE_URL       - Supabase project URL
    SUPABASE_KEY       - Supabase service_role key (NOT anon key)
"""

import os
import sys
from pathlib import Path

import yaml
from supabase import create_client

DATA_DIR = Path(__file__).resolve().parent.parent.parent
KNOWLEDGE_DIR = DATA_DIR / "knowledge"
MAPPINGS_DIR = DATA_DIR / "mappings"
SENTENCES_DIR = DATA_DIR / "sentences"


def load_yaml(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def get_client():
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    if not url or not key:
        print("Error: SUPABASE_URL and SUPABASE_KEY must be set")
        sys.exit(1)
    return create_client(url, key)


def truncate_all(client):
    """Delete all data in reverse dependency order."""
    # (table_name, filter_column) - use a column that exists in each table
    table_filters = [
        ("sentence_knowledge_tags", "sentence_id"),
        ("sentence_structures", "id"),
        ("sentences", "id"),
        ("section_prerequisites", "section_id"),
        ("section_knowledge_nodes", "section_id"),
        ("sections", "id"),
        ("knowledge_references", "id"),
        ("check_points", "id"),
        ("understanding_goals", "id"),
        ("knowledge_node_prerequisites", "node_id"),
        ("knowledge_nodes", "id"),
    ]
    print("  Truncating tables...")
    for table, col in table_filters:
        try:
            client.table(table).delete().gte(col, "").execute()
        except Exception:
            try:
                client.table(table).delete().gte(col, 0).execute()
            except Exception as e:
                print(f"  Warning: Could not truncate {table}: {e}")
    print("  Done.")


def import_knowledge_nodes(client):
    """Import knowledge nodes from YAML files."""
    print("\n--- Importing knowledge_nodes ---")
    nodes = []
    prerequisites = []
    goals = []
    checks = []
    refs = []

    for path in sorted(KNOWLEDGE_DIR.rglob("*.yaml")):
        raw = load_yaml(path)
        if not raw or "id" not in raw:
            continue

        node_id = raw["id"]
        nodes.append({
            "id": node_id,
            "name": raw["name"],
            "category": raw.get("category", ""),
            "priority": raw.get("priority", "P3"),
            "notes": raw.get("notes") or None,
        })

        for prereq_id in (raw.get("prerequisites") or []):
            prerequisites.append({
                "node_id": node_id,
                "prerequisite_id": prereq_id,
            })

        for seq, goal_text in enumerate(raw.get("understanding_goals") or [], start=1):
            goals.append({
                "node_id": node_id,
                "seq": seq,
                "goal": goal_text,
            })

        for seq, cp in enumerate(raw.get("check_points") or [], start=1):
            if "question" in cp:
                checks.append({
                    "node_id": node_id,
                    "seq": seq,
                    "question": cp["question"],
                    "answer": cp.get("answer", ""),
                })
            elif "assessment" in cp:
                checks.append({
                    "node_id": node_id,
                    "seq": seq,
                    "question": cp["assessment"],
                    "answer": "",
                })

        for book, ref_data in (raw.get("references") or {}).items():
            refs.append({
                "node_id": node_id,
                "book": book,
                "section_id": ref_data.get("section"),
                "pages": ref_data.get("pages"),
            })

    # Insert nodes first
    client.table("knowledge_nodes").insert(nodes).execute()
    print(f"  knowledge_nodes: {len(nodes)}")

    # Then dependent tables
    if prerequisites:
        client.table("knowledge_node_prerequisites").insert(prerequisites).execute()
    print(f"  knowledge_node_prerequisites: {len(prerequisites)}")

    if goals:
        # Insert in batches to avoid payload size limits
        batch_size = 100
        for i in range(0, len(goals), batch_size):
            client.table("understanding_goals").insert(goals[i:i+batch_size]).execute()
    print(f"  understanding_goals: {len(goals)}")

    if checks:
        batch_size = 100
        for i in range(0, len(checks), batch_size):
            client.table("check_points").insert(checks[i:i+batch_size]).execute()
    print(f"  check_points: {len(checks)}")

    if refs:
        client.table("knowledge_references").insert(refs).execute()
    print(f"  knowledge_references: {len(refs)}")


def import_sections(client):
    """Import sections from mapping YAML files."""
    print("\n--- Importing sections ---")
    sections = []
    section_nodes = []
    section_prereqs = []

    for path in sorted(MAPPINGS_DIR.rglob("*.yaml")):
        raw = load_yaml(path)
        if not raw:
            continue

        book = raw.get("book", path.stem)

        for section in raw.get("sections", []):
            section_id = section["id"]
            sections.append({
                "id": section_id,
                "book": book,
                "title": section.get("title", ""),
                "pages": section.get("pages", ""),
                "type": section.get("type", "drill"),
            })

            for seq, node_id in enumerate(section.get("knowledge_nodes") or [], start=1):
                section_nodes.append({
                    "section_id": section_id,
                    "node_id": node_id,
                    "seq": seq,
                })

            for prereq_id in (section.get("prerequisites") or []):
                section_prereqs.append({
                    "section_id": section_id,
                    "prerequisite_id": prereq_id,
                })

    client.table("sections").insert(sections).execute()
    print(f"  sections: {len(sections)}")

    if section_nodes:
        batch_size = 100
        for i in range(0, len(section_nodes), batch_size):
            client.table("section_knowledge_nodes").insert(
                section_nodes[i:i+batch_size]
            ).execute()
    print(f"  section_knowledge_nodes: {len(section_nodes)}")

    if section_prereqs:
        client.table("section_prerequisites").insert(section_prereqs).execute()
    print(f"  section_prerequisites: {len(section_prereqs)}")


def import_sentences(client):
    """Import sentences from YAML files."""
    print("\n--- Importing sentences ---")
    sentences = []
    structures = []
    tags = []

    for path in sorted(SENTENCES_DIR.rglob("*.yaml")):
        raw = load_yaml(path)
        if not raw:
            continue

        source = raw.get("source", {})
        section_id = source.get("section", path.stem)

        for s in raw.get("sentences", []):
            sentence_id = s["id"]
            sentences.append({
                "id": sentence_id,
                "section_id": section_id,
                "drill": s.get("drill", 0),
                "number": s.get("number", 0),
                "role": s.get("role", "practice"),
                "english": s["english"],
                "japanese": s["japanese"],
                "notes": s.get("notes") or None,
            })

            for label, value in (s.get("structure") or {}).items():
                structures.append({
                    "sentence_id": sentence_id,
                    "label": label,
                    "value": value,
                })

            for node_id in (s.get("knowledge_tags") or []):
                tags.append({
                    "sentence_id": sentence_id,
                    "node_id": node_id,
                })

    # Insert in batches
    batch_size = 100
    for i in range(0, len(sentences), batch_size):
        client.table("sentences").insert(sentences[i:i+batch_size]).execute()
    print(f"  sentences: {len(sentences)}")

    if structures:
        for i in range(0, len(structures), batch_size):
            client.table("sentence_structures").insert(
                structures[i:i+batch_size]
            ).execute()
    print(f"  sentence_structures: {len(structures)}")

    if tags:
        for i in range(0, len(tags), batch_size):
            client.table("sentence_knowledge_tags").insert(
                tags[i:i+batch_size]
            ).execute()
    print(f"  sentence_knowledge_tags: {len(tags)}")


def main():
    print("=== Supabase Data Import ===")
    client = get_client()

    print("\nStep 1: Truncate existing data")
    truncate_all(client)

    print("\nStep 2: Import knowledge nodes")
    import_knowledge_nodes(client)

    print("\nStep 3: Import sections")
    import_sections(client)

    print("\nStep 4: Import sentences")
    import_sentences(client)

    print("\n=== Import complete! ===")


if __name__ == "__main__":
    main()
