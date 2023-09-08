from osrparse import  Replay
import sys
import requests

if len(sys.argv) < 3:
  print("Usage: python script.py <api_key> <hash>")
  sys.exit()

API_KEY = sys.argv[1]  
HASH = r.beatmap_hash

url = f"https://osu.ppy.sh/api/get_beatmaps?k={API_KEY}&h={HASH}"
response = requests.get(url)
data = response.json()
if len(data) > 0:
  beatmap = data[0]
  diffr = round(float(beatmap["difficultyrating"]), 2)


r = Replay.from_path("/home/runner/replay.osr")
mode = r.mode
user = r.username
count300 = r.count_300
count100 = r.count_100
count50 = r.count_50
gcount = r.count_geki
misscount = r.count_miss
score = r.score
maxcombo = r.max_combo
mods = r.mods
time = r.timestamp
total_hits = count50 + count100 + count300
max_hits = total_hits + misscount
raw_accuracy = ( ( 50 * count50 + 100 * count100 + 300 * count300 ) / ( 300 * (count50 + count100 + count300 + misscount) ) ) * 100
accuracy = round(raw_accuracy, 2)
beatmaphash = r.beatmap_hash
replayid = r.replay_id
