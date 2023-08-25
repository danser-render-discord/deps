#!/bin/bash
ak="$1"
hash="$(python3 $(pwd)/osu.py -n)"
sr="$(python3 $(pwd)/sr.py $ak $hash)"
user="$(python3 $(pwd)/osu.py -b)"
map="$(python3 $(pwd)/map.py $ak $hash)"
mods="$(python3 $(pwd)/osu.py -k)"
acc="$(python3 $(pwd)/osu.py -m)"
echo "$sr⭐ $user | $map $acc"
