#!/usr/bin/env python3
"""
check_points の文字列形式を辞書形式に変換するスクリプト

Before:
  check_points:
    - "「Q」→「A」と答えられるか"

After (Q/A型):
  check_points:
    - question: "Q"
      answer: "A"

After (実技評価型):
  check_points:
    - assessment: "テキスト"

使い方:
  python scripts/restructure_checkpoints.py --dry-run   # プレビュー
  python scripts/restructure_checkpoints.py              # 実行
"""

import argparse
import re
import sys
from pathlib import Path

import yaml

PROJECT_ROOT = Path(__file__).resolve().parent.parent
KNOWLEDGE_DIR = PROJECT_ROOT / "knowledge"

# 末尾の動詞パターン（長い順に試行）
TRAILING_SUFFIXES = [
    "のうち4つ以上答えられるか",
    "のうち5つ以上答えられるか",
    "から5つ以上答えられるか",
    "の7つを答えられるか",
    "の4つを答えられるか",
    "と答えられるか",
    "と即答できるか",
    "を答えられるか",
    "と訳せるか",
    "答えられるか",
]

# clau-011 の複合Q/Aエントリ（手動分割対象）
MANUAL_SPLIT = {
    "clau-011": {
        "original": "「how+形・副の訳は？」→「どれほど...か」。関係副詞の訳はある？→「ない」と答えられるか",
        "replacements": [
            {"question": "how+形・副の訳は？", "answer": "どれほど...か"},
            {"question": "how+形・副に関係副詞の訳はある？", "answer": "ない"},
        ],
    }
}


def parse_check_point(raw: str) -> dict:
    """
    check_pointの文字列をパースして辞書形式に変換する。

    Returns:
      {"question": Q, "answer": A}  or
      {"assessment": text}
    """
    # Step 1: → がなければ assessment
    if "→" not in raw:
        return {"assessment": raw}

    # Step 2: 「Q」→ の部分を抽出（最初の 」→ で分割）
    m = re.match(r"^「(.+?)」→\s*", raw)
    if not m:
        return {"assessment": raw}  # フォールバック

    question = m.group(1)
    remainder = raw[m.end() :]

    # Step 3: 末尾の動詞を除去
    for suffix in TRAILING_SUFFIXES:
        if remainder.endswith(suffix):
            remainder = remainder[: -len(suffix)]
            break

    # Step 4: 回答の「」を除去（バランスチェック付き）
    answer = remainder.strip()
    if answer.startswith("「") and answer.endswith("」"):
        inner = answer[1:-1]
        # ネストした「」のバランスが取れていればアンラップ
        if inner.count("「") == inner.count("」"):
            answer = inner

    return {"question": question, "answer": answer}


def format_qa_yaml(item: dict, indent: str = "  ") -> list[str]:
    """辞書形式のcheck_pointをYAML行に変換する。"""
    lines = []
    if "assessment" in item:
        val = item["assessment"]
        lines.append(f'{indent}- assessment: "{val}"')
    else:
        q = item["question"]
        a = item["answer"]
        lines.append(f'{indent}- question: "{q}"')
        lines.append(f'{indent}  answer: "{a}"')
    return lines


def process_file(filepath: Path, dry_run: bool) -> dict:
    """
    1ファイルを処理する。

    Returns:
      {"file": str, "before": int, "after": int, "items": list[dict], "warnings": list[str]}
    """
    result = {
        "file": str(filepath.relative_to(PROJECT_ROOT)),
        "before": 0,
        "after": 0,
        "items": [],
        "warnings": [],
    }

    text = filepath.read_text(encoding="utf-8")
    lines = text.split("\n")

    # YAML解析してnode IDとcheck_pointsを取得
    data = yaml.safe_load(text)
    if not data or "check_points" not in data:
        return result

    node_id = data.get("id", "unknown")
    original_cps = data["check_points"]
    result["before"] = len(original_cps)

    # check_points セクションの行範囲を特定
    cp_start = None
    cp_end = None
    for i, line in enumerate(lines):
        if line.rstrip() == "check_points:":
            cp_start = i
            continue
        if cp_start is not None and cp_end is None:
            # check_points セクション内の行を追跡
            stripped = line.lstrip()
            if stripped.startswith("- "):
                # リストアイテム — check_pointsの一部
                continue
            elif stripped == "" or stripped.startswith("#"):
                # 空行やコメントはスキップ
                continue
            else:
                # 新しいトップレベルキーに到達
                cp_end = i
                break

    if cp_start is None:
        result["warnings"].append(f"check_points: セクションが見つかりません")
        return result

    if cp_end is None:
        cp_end = len(lines)

    # 変換処理
    new_items = []
    for cp in original_cps:
        # clau-011 の手動分割チェック
        if node_id in MANUAL_SPLIT:
            manual = MANUAL_SPLIT[node_id]
            if cp == manual["original"]:
                new_items.extend(manual["replacements"])
                result["items"].extend(manual["replacements"])
                continue

        parsed = parse_check_point(cp)
        new_items.append(parsed)
        result["items"].append(parsed)

    result["after"] = len(new_items)

    # 新しいYAML行を生成
    new_cp_lines = ["check_points:"]
    for item in new_items:
        new_cp_lines.extend(format_qa_yaml(item))

    # 行を差し替え
    new_lines = lines[:cp_start] + new_cp_lines + lines[cp_end:]
    new_text = "\n".join(new_lines)

    # 検証: yaml.safe_load でパース可能か
    try:
        new_data = yaml.safe_load(new_text)
    except yaml.YAMLError as e:
        result["warnings"].append(f"YAML parse error after conversion: {e}")
        return result

    # 検証: check_pointsのエントリ数
    new_cps = new_data.get("check_points", [])
    if len(new_cps) != len(new_items):
        result["warnings"].append(
            f"Entry count mismatch: expected {len(new_items)}, got {len(new_cps)}"
        )

    # 検証: 全エントリが辞書形式
    for i, item in enumerate(new_cps):
        if not isinstance(item, dict):
            result["warnings"].append(f"check_points[{i}] is not a dict: {type(item)}")

    # ラウンドトリップ検証（手動分割分を除く）
    for i, (orig, parsed) in enumerate(zip(original_cps, new_items)):
        if node_id in MANUAL_SPLIT and orig == MANUAL_SPLIT[node_id]["original"]:
            continue  # 手動分割分はスキップ
        roundtrip = reconstruct(parsed)
        if roundtrip is not None and roundtrip != orig:
            result["warnings"].append(
                f"Roundtrip mismatch at [{i}]:\n"
                f"  orig:      {orig}\n"
                f"  roundtrip: {roundtrip}"
            )

    # ファイル書き出し
    if not dry_run and not result["warnings"]:
        filepath.write_text(new_text, encoding="utf-8")

    return result


def reconstruct(item: dict) -> str | None:
    """辞書形式から元の文字列を再構築する（ラウンドトリップ検証用）。

    完全な再構築は不可能（末尾動詞が多様なため）なので None を返す場合がある。
    """
    if "assessment" in item:
        return item["assessment"]
    # Q/A型の再構築は末尾動詞が多様なため省略
    return None


def main():
    parser = argparse.ArgumentParser(
        description="check_pointsを辞書形式に変換"
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="変換結果のプレビューのみ（ファイル書き出しなし）"
    )
    args = parser.parse_args()

    yaml_files = sorted(KNOWLEDGE_DIR.rglob("*.yaml"))
    print(f"対象ファイル: {len(yaml_files)}")
    print(f"モード: {'ドライラン' if args.dry_run else '本番実行'}")
    print("=" * 60)

    total_before = 0
    total_after = 0
    total_assessment = 0
    total_qa = 0
    all_warnings = []

    for filepath in yaml_files:
        result = process_file(filepath, args.dry_run)
        if result["before"] == 0:
            continue

        total_before += result["before"]
        total_after += result["after"]

        for item in result["items"]:
            if "assessment" in item:
                total_assessment += 1
            else:
                total_qa += 1

        if result["warnings"]:
            all_warnings.extend(
                (result["file"], w) for w in result["warnings"]
            )

        # ファイルごとのサマリー
        status = "OK" if not result["warnings"] else "WARNING"
        print(
            f"[{status}] {result['file']}: "
            f"{result['before']} → {result['after']} entries"
        )
        if args.dry_run:
            for item in result["items"]:
                if "assessment" in item:
                    print(f"    [A] {item['assessment'][:60]}...")
                else:
                    print(f"    [Q] {item['question'][:40]}")
                    print(f"    [A] {item['answer'][:40]}")

        for w in result["warnings"]:
            print(f"    ⚠ {w}")

    print("=" * 60)
    print(f"合計: {total_before} → {total_after} エントリ")
    print(f"  Q/A型: {total_qa}")
    print(f"  assessment型: {total_assessment}")
    print(f"  WARNING: {len(all_warnings)}")
    print("=" * 60)

    if all_warnings:
        print("\n⚠ WARNING が検出されました。手動確認が必要です:")
        for filepath, w in all_warnings:
            print(f"  [{filepath}] {w}")
        sys.exit(1)

    if not args.dry_run:
        print("\n✓ 変換完了。validate.py で検証してください。")
    else:
        print("\n✓ ドライラン完了。--dry-run を外して本番実行してください。")


if __name__ == "__main__":
    main()
