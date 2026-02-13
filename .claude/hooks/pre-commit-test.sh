#!/bin/bash
# git commit 前に seras-test-generator/ の変更があればテスト実行
INPUT=$(cat)
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // empty')

if [[ "$COMMAND" != *"git commit"* ]]; then
  exit 0
fi

# seras-test-generator/ の変更があるか確認
STAGED_FILES=$(cd "$CLAUDE_PROJECT_DIR" && git diff --cached --name-only)
if echo "$STAGED_FILES" | grep -q "^seras-test-generator/"; then
  echo "seras-test-generator/ の変更を検出。テスト実行中..." >&2
  TEST_OUTPUT=$(cd "$CLAUDE_PROJECT_DIR/seras-test-generator" && uv run pytest -q 2>&1)
  TEST_EXIT=$?
  if [ $TEST_EXIT -ne 0 ]; then
    echo "テストが失敗しています。修正してからコミットしてください:" >&2
    echo "$TEST_OUTPUT" >&2
    exit 2
  fi
  echo "テスト全パス" >&2
fi

exit 0
