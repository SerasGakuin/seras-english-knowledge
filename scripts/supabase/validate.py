#!/usr/bin/env python3
"""構造化データの自動バリデーション（YAML版）

Gate 2 の 13項目チェックを実行する。
Usage: python scripts/supabase/validate.py <book_data_dir>
Example: python scripts/supabase/validate.py scripts/supabase/kakushin_data
"""

import sys
import os
import re
import yaml
from pathlib import Path
from collections import defaultdict


# 参考書別のバリデーション設定
BOOK_CONFIGS = {
    "kakushin": {
        "sentence_id_pattern": r"^kaku-\d{2}[a-c]?-[ecx]\d{2}$",
        "node_section_ratio": (2.0, 4.0),
    },
    "narikawa": {
        "sentence_id_pattern": r"^nar-\d{4}-[ev]\d{3}$",
        "node_section_ratio": (1.0, 2.0),
    },
    "nyumon": {
        "sentence_id_pattern": r"^ny-\d{2}-s\d+$",
        "node_section_ratio": (2.0, 4.0),
    },
}


def detect_book_slug(data_dir):
    """ディレクトリ名から book_slug を検出する（xxx_data → xxx）"""
    dir_name = Path(data_dir).name
    if dir_name.endswith("_data"):
        return dir_name[:-5]
    return dir_name


def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def collect_data(data_dir):
    """data_dir 配下の全YAMLを読み込み、統合データを返す"""
    data = {
        "knowledge_nodes": [],
        "understanding_goals": [],
        "check_points": [],
        "node_prerequisites": [],
        "knowledge_references": [],
        "sentences": [],
        "sentence_structures": [],
        "sentence_knowledge_tags": [],
        "sections": [],
        "section_knowledge_nodes": [],
        "section_prerequisites": [],
    }

    # knowledge_nodes/*.yaml
    kn_dir = Path(data_dir) / "knowledge_nodes"
    if kn_dir.exists():
        for f in sorted(kn_dir.glob("*.yaml")):
            d = load_yaml(f)
            if not d:
                continue
            for key in ["knowledge_nodes", "understanding_goals", "check_points",
                        "node_prerequisites", "knowledge_references"]:
                if key in d and d[key]:
                    data[key].extend(d[key])

    # sentences/*.yaml
    sent_dir = Path(data_dir) / "sentences"
    if sent_dir.exists():
        for f in sorted(sent_dir.glob("*.yaml")):
            d = load_yaml(f)
            if not d:
                continue
            for key in ["sentences", "sentence_structures", "sentence_knowledge_tags"]:
                if key in d and d[key]:
                    data[key].extend(d[key])

    # sections.yaml
    sec_path = Path(data_dir) / "sections.yaml"
    if sec_path.exists():
        d = load_yaml(sec_path)
        if d:
            for key in ["sections", "section_knowledge_nodes", "section_prerequisites"]:
                if key in d and d[key]:
                    data[key].extend(d[key])

    return data


def validate(data_dir):
    errors = []
    warnings = []

    data = collect_data(data_dir)
    nodes = data["knowledge_nodes"]
    goals = data["understanding_goals"]
    cps = data["check_points"]
    prereqs = data["node_prerequisites"]
    sents = data["sentences"]
    structs = data["sentence_structures"]
    tags = data["sentence_knowledge_tags"]
    sections = data["sections"]
    sec_nodes = data["section_knowledge_nodes"]

    node_ids = {n["id"] for n in nodes}
    sent_ids = {s["id"] for s in sents}
    section_ids = {s["id"] for s in sections}

    # CHECK-01: YAML構文チェック（読み込み成功で暗黙的にパス）
    print("CHECK-01: YAML構文チェック ... OK")

    # CHECK-02: knowledge_nodes の必須フィールド
    required_node_fields = ["id", "name", "category", "priority", "notes"]
    for n in nodes:
        for field in required_node_fields:
            if field not in n or not n[field]:
                errors.append(f"CHECK-02: ノード {n.get('id', '?')} に必須フィールド '{field}' がありません")
    if not any("CHECK-02" in e for e in errors):
        print(f"CHECK-02: knowledge_nodes 必須フィールド ... OK ({len(nodes)} nodes)")

    # CHECK-03: sentences の必須フィールド
    required_sent_fields = ["id", "section_id", "role", "english", "japanese"]
    for s in sents:
        for field in required_sent_fields:
            if field not in s or not s[field]:
                errors.append(f"CHECK-03: 英文 {s.get('id', '?')} に必須フィールド '{field}' がありません")
    if not any("CHECK-03" in e for e in errors):
        print(f"CHECK-03: sentences 必須フィールド ... OK ({len(sents)} sentences)")

    # CHECK-04: knowledge_tags が参照するノードIDが実在するか
    for t in tags:
        if t["node_id"] not in node_ids:
            errors.append(f"CHECK-04: knowledge_tag のノードID '{t['node_id']}' (英文: {t['sentence_id']}) が実在しません")
    if not any("CHECK-04" in e for e in errors):
        print(f"CHECK-04: knowledge_tags 参照整合性 ... OK ({len(tags)} tags)")

    # CHECK-05: knowledge_tags が空の英文がないか
    tagged_sents = {t["sentence_id"] for t in tags}
    for s in sents:
        if s["id"] not in tagged_sents:
            errors.append(f"CHECK-05: 英文 '{s['id']}' に knowledge_tag がありません")
    if not any("CHECK-05" in e for e in errors):
        print("CHECK-05: 全英文にknowledge_tags あり ... OK")

    # CHECK-06: 英文が0件のノードがないか（警告レベル）
    node_sent_count = defaultdict(int)
    for t in tags:
        node_sent_count[t["node_id"]] += 1
    for n in nodes:
        if node_sent_count[n["id"]] == 0:
            warnings.append(f"CHECK-06: ノード '{n['id']}' ({n['name']}) に紐づく英文が0件です")
    if not any("CHECK-06" in w for w in warnings):
        print("CHECK-06: 全ノードに英文あり ... OK")

    # CHECK-07: section_knowledge_nodes のノードIDが実在するか
    for sn in sec_nodes:
        if sn["node_id"] not in node_ids:
            errors.append(f"CHECK-07: section_knowledge_nodes のノードID '{sn['node_id']}' が実在しません")
    if not any("CHECK-07" in e for e in errors):
        print(f"CHECK-07: section_knowledge_nodes 参照整合性 ... OK")

    # CHECK-08: prerequisites の循環依存がないか
    adj = defaultdict(set)
    for p in prereqs:
        adj[p["node_id"]].add(p["prerequisite_id"])

    def has_cycle(node, visited, rec_stack):
        visited.add(node)
        rec_stack.add(node)
        for neighbor in adj[node]:
            if neighbor not in visited:
                if has_cycle(neighbor, visited, rec_stack):
                    return True
            elif neighbor in rec_stack:
                return True
        rec_stack.discard(node)
        return False

    visited, rec_stack = set(), set()
    cycle_found = False
    for nid in node_ids:
        if nid not in visited:
            if has_cycle(nid, visited, rec_stack):
                errors.append(f"CHECK-08: prerequisites に循環依存があります")
                cycle_found = True
                break
    if not cycle_found:
        print("CHECK-08: prerequisites 循環依存なし ... OK")

    # CHECK-09: ID命名規則の一貫性
    # ノードID: {prefix}-{3桁}
    book_slug = detect_book_slug(data_dir)
    book_cfg = BOOK_CONFIGS.get(book_slug, {})
    for n in nodes:
        if not re.match(r"^[a-z]{3}-\d{3}$", n["id"]):
            errors.append(f"CHECK-09: ノードID '{n['id']}' が命名規則に合致しません (期待: xxx-NNN)")
    # 英文ID: 参考書別パターン
    sent_id_pattern = book_cfg.get("sentence_id_pattern", r"^[a-z]+-\d+-[a-z]\d+$")
    for s in sents:
        if not re.match(sent_id_pattern, s["id"]):
            errors.append(f"CHECK-09: 英文ID '{s['id']}' が命名規則に合致しません (期待パターン: {sent_id_pattern})")
    if not any("CHECK-09" in e for e in errors):
        print("CHECK-09: ID命名規則 ... OK")

    # CHECK-10: manifest.yaml との整合性
    manifest_path = Path(data_dir) / "manifest.yaml"
    if manifest_path.exists():
        manifest = load_yaml(manifest_path)
        # チェック対象のセクションのみ
        print("CHECK-10: manifest.yaml 整合性 ... SKIP (パイロット段階)")
    else:
        warnings.append("CHECK-10: manifest.yaml が見つかりません")

    # CHECK-11: understanding_goals の数（ノードあたり 3〜6 個）
    goal_count = defaultdict(int)
    for g in goals:
        goal_count[g["node_id"]] += 1
    for n in nodes:
        cnt = goal_count[n["id"]]
        if cnt < 3 or cnt > 6:
            warnings.append(f"CHECK-11: ノード '{n['id']}' のunderstanding_goals数が {cnt} (期待: 3〜6)")
    if not any("CHECK-11" in w for w in warnings):
        print("CHECK-11: understanding_goals 数 ... OK")

    # CHECK-12: check_points の数（ノードあたり 3〜5 個）
    cp_count = defaultdict(int)
    for c in cps:
        cp_count[c["node_id"]] += 1
    for n in nodes:
        cnt = cp_count[n["id"]]
        if cnt < 3 or cnt > 5:
            warnings.append(f"CHECK-12: ノード '{n['id']}' のcheck_points数が {cnt} (期待: 3〜5)")
    if not any("CHECK-12" in w for w in warnings):
        print("CHECK-12: check_points 数 ... OK")

    # CHECK-13: ノード/セクション比率
    # パイロットセクションのみ計算
    completed_sections = set()
    for sn in sec_nodes:
        completed_sections.add(sn["section_id"])
    if completed_sections:
        ratio = len(nodes) / len(completed_sections)
        ratio_range = book_cfg.get("node_section_ratio", (2.0, 4.0))
        print(f"CHECK-13: ノード/セクション比率 = {ratio:.1f} (目安: {ratio_range[0]}〜{ratio_range[1]})")
        if ratio < ratio_range[0] or ratio > ratio_range[1]:
            warnings.append(f"CHECK-13: ノード/セクション比率が {ratio:.1f} (目安範囲: {ratio_range[0]}〜{ratio_range[1]})")

    # === サマリ ===
    print("\n" + "=" * 60)
    print(f"結果: エラー {len(errors)} 件, 警告 {len(warnings)} 件")
    print(f"ノード: {len(nodes)}, 英文: {len(sents)}, セクション(データあり): {len(completed_sections)}")
    if errors:
        print("\n--- エラー ---")
        for e in errors:
            print(f"  ❌ {e}")
    if warnings:
        print("\n--- 警告 ---")
        for w in warnings:
            print(f"  ⚠️  {w}")
    print("=" * 60)

    return len(errors) == 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <book_data_dir>")
        sys.exit(1)
    data_dir = sys.argv[1]
    if not os.path.isdir(data_dir):
        print(f"Error: '{data_dir}' is not a directory")
        sys.exit(1)
    success = validate(data_dir)
    sys.exit(0 if success else 1)
