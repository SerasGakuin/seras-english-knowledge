#!/bin/bash
# PreToolUse hook: git commit 前に validate.py を実行
INPUT=$(cat)
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // empty')

# git commit コマンドかどうかチェック
if [[ "$COMMAND" == *"git commit"* ]]; then
  # validate.py を実行
  VALIDATION_OUTPUT=$("$CLAUDE_PROJECT_DIR/.venv/bin/python" "$CLAUDE_PROJECT_DIR/scripts/validate.py" 2>&1)
  VALIDATION_EXIT=$?

  if [ $VALIDATION_EXIT -ne 0 ]; then
    echo "バリデーションエラーがあります。修正してからコミットしてください:" >&2
    echo "$VALIDATION_OUTPUT" >&2
    exit 2
  fi
fi

exit 0
