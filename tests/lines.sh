#!/bin/sh
set -eu
check() {
  actual=$(printf '%s' "$1" | sh lines.sh)
  test "$actual" = "$2" || { echo "line count expected $2 got $actual" >&2; exit 1; }
}
check '' 0
check 'alpha' 1
check 'alpha
' 1
check 'alpha

beta' 3
check '

' 2
check_bytes() {
  actual=$(printf '%b' "$1" | sh lines.sh)
  test "$actual" = "$2" || { echo "byte input $1: line count expected $2 got $actual" >&2; exit 1; }
}
# Keep NUL bytes in the pipe: shell variables cannot represent them.
check_bytes '\000' 1
check_bytes '\n\000' 2
check_bytes '\000\000' 1
check_bytes '\000\n' 1
check_bytes '\000\n\000\n' 2
check_bytes 'alpha\000beta' 1
check_bytes '\000\n\n\000' 3
if sh lines.sh unexpected </dev/null >/dev/null 2>/dev/null; then
  echo 'arguments must be rejected' >&2; exit 1
fi
python3 -c 'import json; assert "lines" in json.load(open("catalog.json"))["features"]'
