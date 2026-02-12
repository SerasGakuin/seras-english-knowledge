#!/usr/bin/env python3
"""
知識ノード・英文データベース・セクションマッピングのバリデーションスクリプト

使い方:
  python scripts/validate.py              # 全チェック実行
  python scripts/validate.py --section Ch01  # Ch01関連のみ
  python scripts/validate.py --check 04   # CHECK-04のみ
"""

import argparse
import sys
from pathlib import Path

import yaml


PROJECT_ROOT = Path(__file__).resolve().parent.parent
KNOWLEDGE_DIR = PROJECT_ROOT / "knowledge"
SENTENCES_DIR = PROJECT_ROOT / "sentences" / "はじめの英文読解ドリル"
MAPPINGS_DIR = PROJECT_ROOT / "mappings"
MANIFEST_PATH = PROJECT_ROOT / "manifest.yaml"

# 知識ノードの必須フィールド
KNOWLEDGE_REQUIRED_FIELDS = ["id", "name", "category", "priority", "understanding_goals", "check_points"]

# 英文の必須フィールド
SENTENCE_REQUIRED_FIELDS = ["id", "drill", "english", "japanese", "knowledge_tags"]

# ID prefixの許可リスト
VALID_ID_PREFIXES = ["strc", "vtyp", "clau", "subj", "read"]


class ValidationResult:
    def __init__(self):
        self.errors = []
        self.warnings = []

    def error(self, check_id: str, message: str):
        self.errors.append(f"[ERROR] {check_id}: {message}")

    def warning(self, check_id: str, message: str):
        self.warnings.append(f"[WARN]  {check_id}: {message}")

    def summary(self) -> str:
        lines = []
        lines.append("=" * 60)
        lines.append("VALIDATION RESULT")
        lines.append("=" * 60)
        if self.errors:
            lines.append(f"\nErrors: {len(self.errors)}")
            for e in self.errors:
                lines.append(f"  {e}")
        if self.warnings:
            lines.append(f"\nWarnings: {len(self.warnings)}")
            for w in self.warnings:
                lines.append(f"  {w}")
        if not self.errors and not self.warnings:
            lines.append("\nAll checks passed!")
        lines.append("=" * 60)
        return "\n".join(lines)

    @property
    def ok(self) -> bool:
        return len(self.errors) == 0


def load_yaml_files(directory: Path) -> list[tuple[Path, dict]]:
    """ディレクトリ内の全YAMLファイルを読み込む"""
    results = []
    if not directory.exists():
        return results
    for f in sorted(directory.rglob("*.yaml")):
        try:
            with open(f, encoding="utf-8") as fh:
                data = yaml.safe_load(fh)
                if data:
                    results.append((f, data))
        except yaml.YAMLError as e:
            results.append((f, {"_parse_error": str(e)}))
    return results


def collect_knowledge_nodes(section_filter: str | None = None) -> list[tuple[Path, dict]]:
    """全知識ノードを収集"""
    all_nodes = []
    for f, data in load_yaml_files(KNOWLEDGE_DIR):
        if "_parse_error" in data:
            all_nodes.append((f, data))
            continue
        if section_filter and section_filter not in str(f):
            continue
        all_nodes.append((f, data))
    return all_nodes


def collect_sentences(section_filter: str | None = None) -> list[tuple[Path, dict]]:
    """全英文ファイルを収集"""
    all_files = []
    for f, data in load_yaml_files(SENTENCES_DIR):
        if section_filter and section_filter not in f.stem:
            continue
        all_files.append((f, data))
    return all_files


def collect_mappings() -> list[tuple[Path, dict]]:
    """全マッピングファイルを収集"""
    return load_yaml_files(MAPPINGS_DIR)


# ===== CHECK-01: YAML構文チェック =====
def check_01_yaml_syntax(result: ValidationResult, section_filter: str | None = None):
    """全YAMLファイルの構文をチェック"""
    dirs = [KNOWLEDGE_DIR, SENTENCES_DIR, MAPPINGS_DIR]
    for d in dirs:
        if not d.exists():
            continue
        for f in sorted(d.rglob("*.yaml")):
            try:
                with open(f, encoding="utf-8") as fh:
                    yaml.safe_load(fh)
            except yaml.YAMLError as e:
                result.error("CHECK-01", f"YAML parse error in {f.relative_to(PROJECT_ROOT)}: {e}")


# ===== CHECK-02: 知識ノード必須フィールド =====
def check_02_knowledge_required(result: ValidationResult, section_filter: str | None = None):
    """知識ノードの必須フィールド存在確認"""
    for f, data in collect_knowledge_nodes(section_filter):
        if "_parse_error" in data:
            continue
        for field in KNOWLEDGE_REQUIRED_FIELDS:
            if field not in data:
                result.error("CHECK-02", f"{f.relative_to(PROJECT_ROOT)}: missing field '{field}'")
            elif data[field] is None or data[field] == "":
                result.error("CHECK-02", f"{f.relative_to(PROJECT_ROOT)}: empty field '{field}'")


# ===== CHECK-03: 英文データ必須フィールド =====
def check_03_sentence_required(result: ValidationResult, section_filter: str | None = None):
    """英文データの必須フィールド存在確認"""
    for f, data in collect_sentences(section_filter):
        if "_parse_error" in data:
            continue
        sentences = data.get("sentences", [])
        if not sentences:
            result.warning("CHECK-03", f"{f.relative_to(PROJECT_ROOT)}: no sentences found")
            continue
        for i, s in enumerate(sentences):
            for field in SENTENCE_REQUIRED_FIELDS:
                if field not in s:
                    sid = s.get("id", f"index {i}")
                    result.error("CHECK-03", f"{f.relative_to(PROJECT_ROOT)} [{sid}]: missing field '{field}'")


# ===== CHECK-04: knowledge_tagsの参照先が実在するか =====
def check_04_tags_exist(result: ValidationResult, section_filter: str | None = None):
    """knowledge_tagsが参照するノードIDが実在するか"""
    # 全知識ノードIDを収集
    all_node_ids = set()
    for f, data in collect_knowledge_nodes():
        if "_parse_error" not in data and "id" in data:
            all_node_ids.add(data["id"])

    if not all_node_ids:
        result.warning("CHECK-04", "No knowledge nodes found, skipping tag reference check")
        return

    # 全英文のknowledge_tagsをチェック
    for f, data in collect_sentences(section_filter):
        if "_parse_error" in data:
            continue
        for s in data.get("sentences", []):
            tags = s.get("knowledge_tags", [])
            if tags:
                for tag in tags:
                    if tag not in all_node_ids:
                        sid = s.get("id", "unknown")
                        result.error("CHECK-04", f"{f.relative_to(PROJECT_ROOT)} [{sid}]: "
                                     f"knowledge_tag '{tag}' does not match any knowledge node")


# ===== CHECK-05: knowledge_tagsが空の英文 =====
def check_05_empty_tags(result: ValidationResult, section_filter: str | None = None):
    """knowledge_tagsが空の英文がないか"""
    for f, data in collect_sentences(section_filter):
        if "_parse_error" in data:
            continue
        for s in data.get("sentences", []):
            tags = s.get("knowledge_tags", [])
            if not tags:
                sid = s.get("id", "unknown")
                result.error("CHECK-05", f"{f.relative_to(PROJECT_ROOT)} [{sid}]: "
                             f"knowledge_tags is empty (untagged sentence)")


# ===== CHECK-06: 英文が0件の知識ノード =====
def check_06_orphan_nodes(result: ValidationResult, section_filter: str | None = None):
    """英文が0件の知識ノード（この参考書では練習できない知識）"""
    # 全英文からタグを収集
    all_tags = set()
    for f, data in collect_sentences():
        if "_parse_error" in data:
            continue
        for s in data.get("sentences", []):
            for tag in s.get("knowledge_tags", []):
                all_tags.add(tag)

    # 知識ノードをチェック
    for f, data in collect_knowledge_nodes(section_filter):
        if "_parse_error" in data:
            continue
        node_id = data.get("id")
        if node_id and node_id not in all_tags:
            result.warning("CHECK-06", f"{f.relative_to(PROJECT_ROOT)} [{node_id}]: "
                           f"no sentences reference this node (orphan)")


# ===== CHECK-07: マッピングのknowledge_nodesが実在するか =====
def check_07_mapping_refs(result: ValidationResult, section_filter: str | None = None):
    """セクションマッピングのknowledge_nodesが実在するか"""
    all_node_ids = set()
    for f, data in collect_knowledge_nodes():
        if "_parse_error" not in data and "id" in data:
            all_node_ids.add(data["id"])

    if not all_node_ids:
        result.warning("CHECK-07", "No knowledge nodes found, skipping mapping reference check")
        return

    for f, data in collect_mappings():
        if "_parse_error" in data:
            continue
        for section in data.get("sections", []):
            sec_id = section.get("id", "unknown")
            if section_filter and section_filter not in sec_id:
                continue
            for node_ref in section.get("knowledge_nodes", []):
                if node_ref not in all_node_ids:
                    result.error("CHECK-07", f"{f.relative_to(PROJECT_ROOT)} [{sec_id}]: "
                                 f"knowledge_node '{node_ref}' does not exist")


# ===== CHECK-08: prerequisites循環依存 =====
def check_08_circular_deps(result: ValidationResult, section_filter: str | None = None):
    """prerequisitesの循環依存がないか"""
    # マッピングから依存関係グラフを構築
    deps = {}
    for f, data in collect_mappings():
        if "_parse_error" in data:
            continue
        for section in data.get("sections", []):
            sec_id = section.get("id")
            if sec_id:
                deps[sec_id] = section.get("prerequisites", [])

    # DFSで循環検出
    visited = set()
    in_stack = set()

    def dfs(node, path):
        if node in in_stack:
            cycle = path[path.index(node):]
            result.error("CHECK-08", f"Circular dependency detected: {' -> '.join(cycle + [node])}")
            return
        if node in visited:
            return
        visited.add(node)
        in_stack.add(node)
        for dep in deps.get(node, []):
            dfs(dep, path + [node])
        in_stack.discard(node)

    for node in deps:
        dfs(node, [])


# ===== CHECK-09: ID命名規則 =====
def check_09_id_naming(result: ValidationResult, section_filter: str | None = None):
    """ID命名規則の一貫性（prefix-NNN形式）"""
    import re
    pattern = re.compile(r"^[a-z]+-\d{3}$")

    for f, data in collect_knowledge_nodes(section_filter):
        if "_parse_error" in data:
            continue
        node_id = data.get("id", "")
        if not pattern.match(node_id):
            result.error("CHECK-09", f"{f.relative_to(PROJECT_ROOT)}: "
                         f"ID '{node_id}' does not match pattern 'prefix-NNN'")
        else:
            prefix = node_id.split("-")[0]
            if prefix not in VALID_ID_PREFIXES:
                result.warning("CHECK-09", f"{f.relative_to(PROJECT_ROOT)}: "
                               f"ID prefix '{prefix}' is not in the known prefix list {VALID_ID_PREFIXES}")


# ===== CHECK-10: manifestとの整合性 =====
def check_10_manifest_consistency(result: ValidationResult, section_filter: str | None = None):
    """manifest.yamlとの整合性"""
    if not MANIFEST_PATH.exists():
        result.error("CHECK-10", "manifest.yaml not found")
        return

    with open(MANIFEST_PATH, encoding="utf-8") as f:
        manifest = yaml.safe_load(f)

    sections = manifest.get("sections", {})

    # 各completedセクションについて、実際にファイルが存在するか確認
    for sec_id, sec_data in sections.items():
        if section_filter and section_filter not in sec_id:
            continue
        status = sec_data.get("status", "not_started")
        if status == "completed":
            node_count = sec_data.get("knowledge_nodes_created", 0)
            sentence_count = sec_data.get("sentences_created", 0)
            if node_count == 0 and sec_data.get("type") != "exam":
                result.warning("CHECK-10", f"manifest [{sec_id}]: "
                               f"status=completed but knowledge_nodes_created=0")
            if sentence_count == 0 and sec_data.get("type") == "drill":
                result.warning("CHECK-10", f"manifest [{sec_id}]: "
                               f"status=completed but sentences_created=0")


# ===== CHECK-11: check_points構造検証 =====
def check_11_checkpoint_structure(result: ValidationResult, section_filter: str | None = None):
    """check_pointsの項目が辞書形式であることを検証"""
    for f, data in collect_knowledge_nodes(section_filter):
        if "_parse_error" in data:
            continue
        for i, item in enumerate(data.get("check_points", [])):
            if isinstance(item, str):
                result.error("CHECK-11", f"{f.relative_to(PROJECT_ROOT)}: "
                             f"check_points[{i}] is string (unconverted)")
            elif isinstance(item, dict):
                has_qa = "question" in item and "answer" in item
                has_assess = "assessment" in item
                if not (has_qa or has_assess):
                    result.error("CHECK-11", f"{f.relative_to(PROJECT_ROOT)}: "
                                 f"check_points[{i}] has invalid keys {list(item.keys())}")
            else:
                result.error("CHECK-11", f"{f.relative_to(PROJECT_ROOT)}: "
                             f"check_points[{i}] has unexpected type {type(item).__name__}")


ALL_CHECKS = {
    "01": check_01_yaml_syntax,
    "02": check_02_knowledge_required,
    "03": check_03_sentence_required,
    "04": check_04_tags_exist,
    "05": check_05_empty_tags,
    "06": check_06_orphan_nodes,
    "07": check_07_mapping_refs,
    "08": check_08_circular_deps,
    "09": check_09_id_naming,
    "10": check_10_manifest_consistency,
    "11": check_11_checkpoint_structure,
}


def main():
    parser = argparse.ArgumentParser(description="Validate knowledge base files")
    parser.add_argument("--section", help="Filter by section (e.g., Ch01)")
    parser.add_argument("--check", help="Run specific check only (e.g., 04)")
    args = parser.parse_args()

    result = ValidationResult()

    if args.check:
        checks_to_run = {args.check: ALL_CHECKS[args.check]}
    else:
        checks_to_run = ALL_CHECKS

    for check_id, check_fn in checks_to_run.items():
        check_fn(result, args.section)

    print(result.summary())
    sys.exit(0 if result.ok else 1)


if __name__ == "__main__":
    main()
