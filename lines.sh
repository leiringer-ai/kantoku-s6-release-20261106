#!/bin/sh

if [ "$#" -ne 0 ]; then
  printf '%s\n' 'Usage: lines.sh < input (no arguments accepted)' >&2
  exit 2
fi

# Shell read may discard NUL bytes. Replace them with a non-newline byte so
# even a NUL-only final unterminated line remains nonempty.
LC_ALL=C tr '\000' 'x' | {
  count=0
  while IFS= read -r line || [ -n "$line" ]; do
    count=$((count + 1))
  done
  printf '%s\n' "$count"
}
