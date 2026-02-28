"""Validate nyumon YAML data files (CHECK-01 to CHECK-13).

Usage:
    python scripts/supabase/nyumon_data/validate.py

Checks:
  CHECK-01: YAML syntax (all files)
  CHECK-02: knowledge_nodes required fields
  CHECK-03: sentences required fields
  CHECK-04: knowledge_tags reference existing node IDs
  CHECK-05: no sentences with empty knowledge_tags
  CHECK-06: no nodes with zero sentences (warning for grammar_lecture nodes)
  CHECK-07: section_knowledge_nodes reference existing node IDs
  CHECK-08: no circular dependencies in prerequisites
  CHECK-09: ID naming consistency
  CHECK-10: manifest.yaml consistency (section/node/sentence counts)
  CHECK-11: understanding_goals count per node (3-6)
  CHECK-12: check_points count per node (3-5)
  CHECK-13: node/section ratio (0.7-1.5)
"""

import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Union

import yaml


BASE_DIR = Path(__file__).parent

# ID prefix patterns per category
VALID_NODE_PREFIXES = {"nbk", "nsv", "njd", "nks", "nst", "nhk", "nta"}
NODE_ID_PATTERN = re.compile(r"^(nbk|nsv|njd|nks|nst|nhk|nta)-\d{3}$")
SECTION_ID_PATTERN = re.compile(r"^Ny_(G\d{2}|\d{2})$")
SENTENCE_ID_PATTERN = re.compile(r"^ny-(G?\d{2})-s\d+$")


def load_yaml(path: Path) -> Optional[Any]:
    """Load a YAML file, return None on error."""
    try:
        with open(path) as f:
            return yaml.safe_load(f)
    except yaml.YAMLError as e:
        return e
    except FileNotFoundError:
        return None


def collect_files():
    """Collect all YAML data files."""
    knowledge_dir = BASE_DIR / "knowledge_nodes"
    sentences_dir = BASE_DIR / "sentences"
    sections_file = BASE_DIR / "sections.yaml"
    manifest_file = BASE_DIR / "manifest.yaml"

    files = {
        "knowledge_nodes": sorted(knowledge_dir.glob("*.yaml")) if knowledge_dir.exists() else [],
        "sentences": sorted(sentences_dir.glob("*.yaml")) if sentences_dir.exists() else [],
        "sections": sections_file,
        "manifest": manifest_file,
    }
    return files


def check_01_yaml_syntax(files) -> List[str]:
    """CHECK-01: YAML syntax check on all files."""
    errors = []
    all_files = files["knowledge_nodes"] + files["sentences"]
    if files["sections"].exists():
        all_files.append(files["sections"])
    if files["manifest"].exists():
        all_files.append(files["manifest"])

    for f in all_files:
        result = load_yaml(f)
        if isinstance(result, yaml.YAMLError):
            errors.append(f"CHECK-01: YAML syntax error in {f.name}: {result}")
    return errors


def load_all_knowledge_data(files):
    """Load and merge all knowledge node files."""
    nodes = []
    goals = []
    cps = []
    prereqs = []
    refs = []

    for f in files["knowledge_nodes"]:
        data = load_yaml(f)
        if data is None or isinstance(data, Exception):
            continue
        nodes.extend(data.get("knowledge_nodes", []))
        goals.extend(data.get("understanding_goals", []))
        cps.extend(data.get("check_points", []))
        prereqs.extend(data.get("node_prerequisites", []))
        refs.extend(data.get("knowledge_references", []))

    return nodes, goals, cps, prereqs, refs


def load_all_sentence_data(files):
    """Load and merge all sentence files."""
    sentences = []
    structures = []
    tags = []

    for f in files["sentences"]:
        data = load_yaml(f)
        if data is None or isinstance(data, Exception):
            continue
        sentences.extend(data.get("sentences", []))
        structures.extend(data.get("sentence_structures", []))
        tags.extend(data.get("sentence_knowledge_tags", []))

    return sentences, structures, tags


def check_02_node_fields(nodes) -> List[str]:
    """CHECK-02: knowledge_nodes required fields."""
    errors = []
    required = ["id", "name", "category", "priority", "notes"]
    for n in nodes:
        nid = n.get("id", "???")
        for field in required:
            if field not in n or n[field] is None:
                errors.append(f"CHECK-02: node {nid} missing field '{field}'")
    return errors


def check_03_sentence_fields(sentences) -> List[str]:
    """CHECK-03: sentences required fields."""
    errors = []
    required = ["id", "section_id", "drill", "number", "role", "english", "japanese"]
    for s in sentences:
        sid = s.get("id", "???")
        for field in required:
            if field not in s or s[field] is None:
                errors.append(f"CHECK-03: sentence {sid} missing field '{field}'")
    return errors


def check_04_tags_reference_nodes(tags, node_ids) -> List[str]:
    """CHECK-04: knowledge_tags reference existing node IDs."""
    errors = []
    for t in tags:
        if t.get("node_id") not in node_ids:
            errors.append(
                f"CHECK-04: tag for sentence {t.get('sentence_id', '???')} "
                f"references non-existent node '{t.get('node_id')}'"
            )
    return errors


def check_05_empty_tags(sentences, tags) -> List[str]:
    """CHECK-05: no sentences with empty knowledge_tags."""
    errors = []
    tagged_sentences = {t["sentence_id"] for t in tags}
    for s in sentences:
        if s["id"] not in tagged_sentences:
            errors.append(f"CHECK-05: sentence {s['id']} has no knowledge_tags")
    return errors


def check_06_nodes_without_sentences(nodes, tags, sections_data) -> List[str]:
    """CHECK-06: no nodes with zero sentences (warning level for grammar_lecture)."""
    warnings = []
    tagged_nodes = {t["node_id"] for t in tags}

    # Get section types from sections data
    grammar_sections = set()
    if sections_data:
        for sec in sections_data.get("sections", []):
            if sec.get("type") == "grammar_lecture":
                grammar_sections.add(sec["id"])

    # Get section_knowledge_nodes mapping
    skn = sections_data.get("section_knowledge_nodes", []) if sections_data else []
    grammar_nodes = set()
    for mapping in skn:
        if mapping.get("section_id") in grammar_sections:
            grammar_nodes.add(mapping.get("node_id"))

    for n in nodes:
        if n["id"] not in tagged_nodes:
            level = "WARNING" if n["id"] in grammar_nodes or n.get("category") == "基本講義" else "CHECK-06"
            warnings.append(f"{level}: node {n['id']} ({n['name']}) has no tagged sentences")
    return warnings


def check_07_section_nodes_exist(sections_data, node_ids) -> List[str]:
    """CHECK-07: section_knowledge_nodes reference existing node IDs."""
    errors = []
    if not sections_data:
        return errors
    for skn in sections_data.get("section_knowledge_nodes", []):
        if skn.get("node_id") not in node_ids:
            errors.append(
                f"CHECK-07: section {skn.get('section_id')} references "
                f"non-existent node '{skn.get('node_id')}'"
            )
    return errors


def check_08_circular_deps(prereqs) -> List[str]:
    """CHECK-08: no circular dependencies in prerequisites."""
    errors = []
    # Build adjacency list
    graph: Dict[str, Set[str]] = {}
    for p in prereqs:
        nid = p.get("node_id", "")
        pid = p.get("prerequisite_id", "")
        if nid not in graph:
            graph[nid] = set()
        graph[nid].add(pid)

    # DFS cycle detection
    visited: Set[str] = set()
    in_stack: Set[str] = set()

    def dfs(node: str) -> bool:
        if node in in_stack:
            return True  # cycle
        if node in visited:
            return False
        visited.add(node)
        in_stack.add(node)
        for dep in graph.get(node, set()):
            if dfs(dep):
                errors.append(f"CHECK-08: circular dependency involving node '{node}' -> '{dep}'")
                return True
        in_stack.discard(node)
        return False

    for node in graph:
        dfs(node)

    return errors


def check_09_id_naming(nodes, sentences, sections_data) -> List[str]:
    """CHECK-09: ID naming consistency."""
    errors = []
    for n in nodes:
        if not NODE_ID_PATTERN.match(n.get("id", "")):
            errors.append(f"CHECK-09: node ID '{n.get('id')}' does not match pattern {{prefix}}-NNN")

    for s in sentences:
        if not SENTENCE_ID_PATTERN.match(s.get("id", "")):
            errors.append(f"CHECK-09: sentence ID '{s.get('id')}' does not match pattern ny-NN-sN")

    if sections_data:
        for sec in sections_data.get("sections", []):
            if not SECTION_ID_PATTERN.match(sec.get("id", "")):
                errors.append(f"CHECK-09: section ID '{sec.get('id')}' does not match pattern Ny_NN or Ny_GNN")

    return errors


def check_10_manifest_consistency(manifest_data, nodes, sentences, sections_data) -> List[str]:
    """CHECK-10: manifest.yaml consistency."""
    errors = []
    if not manifest_data:
        errors.append("CHECK-10: manifest.yaml not found or empty")
        return errors

    summary = manifest_data.get("summary", {})

    # Count completed sections from manifest
    manifest_sections = manifest_data.get("sections", {})
    completed = sum(1 for s in manifest_sections.values() if s.get("status") == "completed")
    manifest_total_sections = summary.get("total_sections", 0)

    # Count actual data
    actual_sections = len(sections_data.get("sections", [])) if sections_data else 0
    if manifest_total_sections != actual_sections:
        errors.append(
            f"CHECK-10: manifest total_sections ({manifest_total_sections}) "
            f"!= sections.yaml count ({actual_sections})"
        )

    # Sum up per-section counts from manifest
    manifest_nodes = sum(s.get("knowledge_nodes_created", 0) for s in manifest_sections.values())
    manifest_sentences = sum(s.get("sentences_created", 0) for s in manifest_sections.values())

    actual_nodes = len(nodes)
    actual_sentences = len(sentences)

    if manifest_nodes != actual_nodes:
        errors.append(
            f"CHECK-10: manifest total nodes ({manifest_nodes}) "
            f"!= actual node count ({actual_nodes})"
        )
    if manifest_sentences != actual_sentences:
        errors.append(
            f"CHECK-10: manifest total sentences ({manifest_sentences}) "
            f"!= actual sentence count ({actual_sentences})"
        )

    return errors


def check_11_goals_count(nodes, goals) -> List[str]:
    """CHECK-11: understanding_goals count per node (3-6)."""
    errors = []
    goals_per_node: Dict[str, int] = {}
    for g in goals:
        nid = g.get("node_id", "")
        goals_per_node[nid] = goals_per_node.get(nid, 0) + 1

    node_ids = {n["id"] for n in nodes}
    for nid in node_ids:
        count = goals_per_node.get(nid, 0)
        if count < 3 or count > 6:
            errors.append(f"CHECK-11: node {nid} has {count} understanding_goals (expected 3-6)")

    return errors


def check_12_checkpoints_count(nodes, cps) -> List[str]:
    """CHECK-12: check_points count per node (3-5)."""
    errors = []
    cps_per_node: Dict[str, int] = {}
    for cp in cps:
        nid = cp.get("node_id", "")
        cps_per_node[nid] = cps_per_node.get(nid, 0) + 1

    node_ids = {n["id"] for n in nodes}
    for nid in node_ids:
        count = cps_per_node.get(nid, 0)
        if count < 3 or count > 5:
            errors.append(f"CHECK-12: node {nid} has {count} check_points (expected 3-5)")

    return errors


def check_13_ratio(nodes, sections_data) -> List[str]:
    """CHECK-13: node/section ratio (0.7-1.5)."""
    errors = []
    if not sections_data:
        return errors

    num_sections = len(sections_data.get("sections", []))
    num_nodes = len(nodes)

    if num_sections == 0:
        return errors

    ratio = num_nodes / num_sections
    if ratio < 0.7 or ratio > 1.5:
        errors.append(
            f"CHECK-13: node/section ratio is {ratio:.2f} "
            f"({num_nodes} nodes / {num_sections} sections), expected 0.7-1.5"
        )

    return errors


def main():
    files = collect_files()

    print("=== nyumon YAML Validation ===\n")

    all_errors: list[str] = []
    all_warnings: list[str] = []

    # CHECK-01: YAML syntax
    print("CHECK-01: YAML syntax...")
    errs = check_01_yaml_syntax(files)
    all_errors.extend(errs)
    print(f"  {'FAIL' if errs else 'OK'} ({len(errs)} errors)")
    if errs:
        for e in errs:
            print(f"    {e}")
        print("\n  Cannot continue with syntax errors. Fix and re-run.")
        sys.exit(1)

    # Load all data
    nodes, goals, cps, prereqs, refs = load_all_knowledge_data(files)
    sentences, structures, tags = load_all_sentence_data(files)
    sections_data = load_yaml(files["sections"]) if files["sections"].exists() else None
    manifest_data = load_yaml(files["manifest"]) if files["manifest"].exists() else None
    node_ids = {n["id"] for n in nodes}

    print(f"\n  Loaded: {len(nodes)} nodes, {len(sentences)} sentences, "
          f"{len(goals)} goals, {len(cps)} check_points, {len(tags)} tags\n")

    # CHECK-02 to CHECK-13
    checks = [
        ("CHECK-02", "Node required fields", lambda: check_02_node_fields(nodes)),
        ("CHECK-03", "Sentence required fields", lambda: check_03_sentence_fields(sentences)),
        ("CHECK-04", "Tags reference existing nodes", lambda: check_04_tags_reference_nodes(tags, node_ids)),
        ("CHECK-05", "No empty knowledge_tags", lambda: check_05_empty_tags(sentences, tags)),
        ("CHECK-06", "Nodes without sentences", lambda: check_06_nodes_without_sentences(nodes, tags, sections_data)),
        ("CHECK-07", "Section nodes exist", lambda: check_07_section_nodes_exist(sections_data, node_ids)),
        ("CHECK-08", "No circular dependencies", lambda: check_08_circular_deps(prereqs)),
        ("CHECK-09", "ID naming consistency", lambda: check_09_id_naming(nodes, sentences, sections_data)),
        ("CHECK-10", "Manifest consistency", lambda: check_10_manifest_consistency(manifest_data, nodes, sentences, sections_data)),
        ("CHECK-11", "Goals count (3-6/node)", lambda: check_11_goals_count(nodes, goals)),
        ("CHECK-12", "Check_points count (3-5/node)", lambda: check_12_checkpoints_count(nodes, cps)),
        ("CHECK-13", "Node/section ratio (0.7-1.5)", lambda: check_13_ratio(nodes, sections_data)),
    ]

    for check_id, desc, fn in checks:
        print(f"{check_id}: {desc}...")
        results = fn()
        errors = [r for r in results if not r.startswith("WARNING")]
        warnings = [r for r in results if r.startswith("WARNING")]
        all_errors.extend(errors)
        all_warnings.extend(warnings)
        status = "FAIL" if errors else ("WARN" if warnings else "OK")
        print(f"  {status} ({len(errors)} errors, {len(warnings)} warnings)")
        for e in errors:
            print(f"    {e}")
        for w in warnings:
            print(f"    {w}")

    # Summary
    print("\n=== Summary ===")
    print(f"  Nodes: {len(nodes)}")
    print(f"  Sentences: {len(sentences)}")
    print(f"  Goals: {len(goals)}")
    print(f"  Check points: {len(cps)}")
    print(f"  Tags: {len(tags)}")

    if all_errors:
        print(f"\n  ERRORS ({len(all_errors)}):")
        for e in all_errors:
            print(f"    - {e}")
    if all_warnings:
        print(f"\n  WARNINGS ({len(all_warnings)}):")
        for w in all_warnings:
            print(f"    - {w}")

    if all_errors:
        print(f"\n  FAILED with {len(all_errors)} errors")
        sys.exit(1)
    else:
        print("\n  All checks passed!")


if __name__ == "__main__":
    main()
