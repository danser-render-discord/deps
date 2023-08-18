#!/bin/bash
ak="$1"
hash="$(python3 /home/runner/osu.py -n)"
sr="$(python3 /home/runner/sr.py $ak $hash)"
user="$(python3 /home/runner/osu.py -b)"
map="$(python3 /home/runner/map.py $ak $hash)"
mods="$(python3 /home/runner/osu.py -k)"
acc="$(python3 /home/runner/osu.py -m)"
echo "$sr⭐ $user | $map $acc"
