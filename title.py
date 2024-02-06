from osrparse import Replay
import sys
import requests
import argparse

parser = argparse.ArgumentParser(description='osu! replay parser')
parser.add_argument('replay_path', help='Path to the replay file')
parser.add_argument('api_key', help='API key for osu! API')
args = parser.parse_args()

replay_path = args.replay_path
API_KEY = args.api_key

try:
    r = Replay.from_path(replay_path)
except Exception as e:
    print(f"Error parsing replay file: {e}")
    sys.exit(1)

HASH = r.beatmap_hash

url = f"https://osu.ppy.sh/api/get_beatmaps?k={API_KEY}&h={HASH}"
response = requests.get(url)
data = response.json()

if len(data) > 0:
    beatmap = data[0]
    diffr = round(float(beatmap["difficultyrating"]), 2)

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
raw_accuracy = ((50 * count50 + 100 * count100 + 300 * count300) / (300 * (count50 + count100 + count300 + misscount))) * 100
accuracy = round(raw_accuracy, 2)
beatmaphash = r.beatmap_hash
replayid = r.replay_id

print(f"Mode: {mode}")
print(f"User: {user}")
print(f"300 count: {count300}")
print(f"100 count: {count100}")
print(f"50 count: {count50}")
print(f"Geki count: {gcount}")
print(f"Miss count: {misscount}")
print(f"Score: {score}")
print(f"Max combo: {maxcombo}")
if mods != 0:
    print(f"Mods: {mods}")
print(f"Time: {time}")
print(f"Accuracy: {accuracy}%")
print(f"Beatmap hash: {beatmaphash}")
print(f"Replay ID: {replayid}")
if len(data) > 0:
    print(f"Difficulty rating: {diffr}")