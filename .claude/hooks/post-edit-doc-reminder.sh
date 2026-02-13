#!/bin/bash
# seras-test-generator/ のコード変更時にドキュメント更新を促す
INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')

if [ -z "$FILE_PATH" ]; then
  exit 0
fi

# seras-test-generator/ の .py ファイル変更
if [[ "$FILE_PATH" == *"/seras-test-generator/"*.py ]]; then
  echo "seras-test-generator/ のコードが変更されました。" >&2
  echo "  以下のドキュメントが最新か確認してください:" >&2
  echo "  - docs/design/確認テスト生成API_設計書.md" >&2
  echo "  - CLAUDE.md（必要な場合）" >&2
  exit 0
fi

exit 0
