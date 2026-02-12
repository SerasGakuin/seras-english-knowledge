#!/bin/bash
# PostToolUse hook: knowledge/ や manifest.yaml の変更時にドキュメント更新を促す
INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')

if [ -z "$FILE_PATH" ]; then
  exit 0
fi

# knowledge/ の変更
if [[ "$FILE_PATH" == *"/knowledge/"* ]]; then
  echo "knowledge/ が変更されました。必要に応じて manifest.yaml を更新してください。" >&2
  exit 0
fi

# manifest.yaml の変更
if [[ "$FILE_PATH" == *"manifest.yaml"* ]]; then
  echo "manifest.yaml が変更されました。大きな進捗変化があれば docs/ROADMAP.md も更新してください。" >&2
  exit 0
fi

exit 0
