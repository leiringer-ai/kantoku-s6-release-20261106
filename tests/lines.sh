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
if sh lines.sh unexpected </dev/null >/dev/null 2>/dev/null; then
  echo 'arguments must be rejected' >&2; exit 1
fi
python3 -c 'import json; assert "lines" in json.load(open("catalog.json"))["features"]'
