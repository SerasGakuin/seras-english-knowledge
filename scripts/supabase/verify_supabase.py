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


def fetch_all_rows(client, table: str, columns: str = "*") -> list[dict]:
    """Fetch all rows from a table, handling pagination (Supabase default limit is 1000)."""
    all_rows = []
    page_size = 1000
    offset = 0
    while True:
        rows = client.table(table).select(columns).range(offset, offset + page_size - 1).execute().data
        all_rows.extend(rows)
        if len(rows) < page_size:
            break
        offset += page_size
    return all_rows


def check_fk_integrity(client, table: str, fk_col: str, ref_table: str, ref_col: str = "id") -> list[str]:
    """Check that all FK values exist in referenced table."""
    rows = fetch_all_rows(client, table, fk_col)
    ref_rows = fetch_all_rows(client, ref_table, ref_col)
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
        "cross_book_links",
    ]:
        c = count_rows(client, table)
        counts[table] = c
        print(f"  {table}: {c}")

    print()

    # Expected minimum counts
    # はじめ84 + 肘井49 + 核心76 + 入門70 = 279 nodes
    # はじめ524 + 肘井405 + 核心473 + 入門210 = 1612 sentences
    expected = {
        "knowledge_nodes": 279,
        "sentences": 1612,
    }

    for table, exp in expected.items():
        actual = counts[table]
        if actual < exp:
            errors.append(f"{table}: expected >= {exp}, got {actual}")
        else:
            print(f"  [OK] {table}: {actual} (expected >= {exp})")

    # Sections: はじめ41 + 肘井39 + 核心26 + 入門85 = 191
    sections_count = counts["sections"]
    if sections_count < 191:
        errors.append(f"sections: expected >= 191, got {sections_count}")
    else:
        print(f"  [OK] sections: {sections_count} (expected >= 191)")

    # Cross-book links: hijii25 + kakushin47 + nyumon44 = 116
    links_count = counts["cross_book_links"]
    if links_count < 116:
        errors.append(f"cross_book_links: expected >= 116, got {links_count}")
    else:
        print(f"  [OK] cross_book_links: {links_count} (expected >= 116)")

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
