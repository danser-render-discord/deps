#!/bin/bash
ak="$1"
hash="$(python osu.py -n)"
sr="$(python sr.py $ak $hash)"
user="$(python osu.py -b)"
map="$(python map.py $ak $hash)"
mods="$(python osu.py -k)"

echo "The first argument is: $var1"
