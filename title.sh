#!/bin/bash
ak="$1"
hash="$(python3 osu.py -n)"
#sr="$(python3 sr.py $ak $hash)"
user="$(python3 osu.py -b)"
#map="$(python3 map.py $ak $hash)"
mods="$(python3 osu.py -k)"
echo $user 
