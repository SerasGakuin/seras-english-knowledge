"""Verify Supabase data integrity after import.

Usage:
    python scripts/supabase/verify_supabase.py

Environment variables:
    SUPABASE_URL       - Supabase project URL
    SUPABASE_KEY       - Supabase service_role key
"""

import os
import sys

from supabase import create_client


def get_client():
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    if not url or not key:
        print("Error: SUPABASE_URL and SUPABASE_KEY must be set")
        sys.exit(1)
    return create_client(url, key)


def count_rows(client, table: str) -> int:
    result = client.table(table).select("*", count="exact").execute()
    return result.count


def check_fk_integrity(client, table: str, fk_col: str, ref_table: str, ref_col: str = "id") -> list[str]:
    """Check that all FK values exist in referenced table."""
    rows = client.table(table).select(fk_col).execute().data
    ref_rows = client.table(ref_table).select(ref_col).execute().data
    ref_ids = {r[ref_col] for r in ref_rows}
    missing = []
    for r in rows:
        val = r[fk_col]
        if val and val not in ref_ids:
            missing.append(val)
    return missing


def main():
    client = get_client()
    errors = []
    warnings = []

    print("=== Supabase Data Verification ===\n")

    # --- Count checks ---
    counts = {}
    for table in [
        "knowledge_nodes", "knowledge_node_prerequisites",
        "understanding_goals", "check_points", "knowledge_references",
        "sections", "section_knowledge_nodes", "section_prerequisites",
        "sentences", "sentence_structures", "sentence_knowledge_tags",
    ]:
        c = count_rows(client, table)
        counts[table] = c
        print(f"  {table}: {c}")

    print()

    # Expected counts (はじめ84+肘井39=123 nodes, はじめ524+肘井405=929 sentences)
    expected = {
        "knowledge_nodes": 123,
        "sentences": 929,
    }

    for table, exp in expected.items():
        actual = counts[table]
        if actual != exp:
            errors.append(f"{table}: expected {exp}, got {actual}")
        else:
            print(f"  [OK] {table}: {actual} (expected {exp})")

    # Sections: はじめ41 + 肘井39 = 80
    sections_count = counts["sections"]
    if sections_count < 80:
        errors.append(f"sections: expected >= 41, got {sections_count}")
    else:
        print(f"  [OK] sections: {sections_count} (expected >= 41)")

    print()

    # --- FK integrity checks ---
    print("--- FK Integrity Checks ---")

    fk_checks = [
        ("knowledge_node_prerequisites", "node_id", "knowledge_nodes"),
        ("knowledge_node_prerequisites", "prerequisite_id", "knowledge_nodes"),
        ("understanding_goals", "node_id", "knowledge_nodes"),
        ("check_points", "node_id", "knowledge_nodes"),
        ("knowledge_references", "node_id", "knowledge_nodes"),
        ("section_knowledge_nodes", "section_id", "sections"),
        ("section_knowledge_nodes", "node_id", "knowledge_nodes"),
        ("section_prerequisites", "section_id", "sections"),
        ("section_prerequisites", "prerequisite_id", "sections"),
        ("sentences", "section_id", "sections"),
        ("sentence_structures", "sentence_id", "sentences"),
        ("sentence_knowledge_tags", "sentence_id", "sentences"),
        ("sentence_knowledge_tags", "node_id", "knowledge_nodes"),
    ]

    for table, fk_col, ref_table in fk_checks:
        missing = check_fk_integrity(client, table, fk_col, ref_table)
        if missing:
            errors.append(f"{table}.{fk_col} -> {ref_table}: missing refs: {missing[:5]}")
        else:
            print(f"  [OK] {table}.{fk_col} -> {ref_table}")

    print()

    # --- Category distribution ---
    print("--- Category Distribution ---")
    nodes = client.table("knowledge_nodes").select("category").execute().data
    categories = {}
    for n in nodes:
        major = n["category"].split("/")[0]
        categories[major] = categories.get(major, 0) + 1
    for cat, cnt in sorted(categories.items()):
        print(f"  {cat}: {cnt}")

    print()

    # --- Section type distribution ---
    print("--- Section Type Distribution ---")
    sections = client.table("sections").select("type").execute().data
    types = {}
    for s in sections:
        t = s["type"]
        types[t] = types.get(t, 0) + 1
    for t, cnt in sorted(types.items()):
        print(f"  {t}: {cnt}")

    print()

    # --- Summary ---
    print("=== Summary ===")
    if errors:
        print(f"\n  ERRORS ({len(errors)}):")
        for e in errors:
            print(f"    - {e}")
        sys.exit(1)
    else:
        print("  All checks passed!")

    if warnings:
        print(f"\n  WARNINGS ({len(warnings)}):")
        for w in warnings:
            print(f"    - {w}")


if __name__ == "__main__":
    main()
