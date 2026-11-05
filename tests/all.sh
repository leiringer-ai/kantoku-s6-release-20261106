#!/bin/sh
set -eu
python3 -m unittest discover -s tests -p test_stats.py -v
node --test tests/median.test.cjs
sh tests/lines.sh
python3 -c 'import json; f=json.load(open("catalog.json"))["features"]; assert sorted(f)==["lines","mean","median"], f'
