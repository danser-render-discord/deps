from osrparse import Replay
import argparse

parser = argparse.ArgumentParser(description='osu! replay parser')
parser.add_argument('replay_path', help='Path to the replay file')

# Add arguments for the desired information
parser.add_argument('-a', '--mode', action='store_true', help='Gamemode')
parser.add_argument('-b', '--user', action='store_true', help='Username')
parser.add_argument('-c', '--count300', action='store_true', help='300 count')
parser.add_argument('-d', '--count100', action='store_true', help='100 count')
parser.add_argument('-e', '--count50', action='store_true', help='50 count')
parser.add_argument('-f', '--gcount', action='store_true', help='Geki count')   
parser.add_argument('-g', '--misscount', action='store_true', help='Miss count')
parser.add_argument('-i', '--score', action='store_true', help='Score')
parser.add_argument('-j', '--maxcombo', action='store_true', help='Max combo')
parser.add_argument('-k', '--mods', action='store_true', help='Mods')
parser.add_argument('-l', '--time', action='store_true', help='Time')
parser.add_argument('-m', '--accuracy', action='store_true', help='Accuracy')
parser.add_argument('-n', '--beatmaphash', action='store_true', help='Beatmap hash')
parser.add_argument('-o', '--replayid', action='store_true', help='Replay ID')
parser.add_argument('-p', '--rawaccuracy', action='store_true', help='Raw accuracy')

args = parser.parse_args()

replay_path = args.replay_path

try:
    replay = Replay.from_path(replay_path)
except Exception as e:
    print(f"Error parsing replay file: {e}")
    exit(1)

r = replay

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

if args.mode:
    print(str(mode))
if args.user:
    print(str(user))
if args.count300:
    print(int(count300))
if args.count100:
    print(int(count100))
if args.count50:
    print(int(count50))
if args.gcount:
    print(int(gcount))
if args.misscount:
    print(int(misscount))
if args.score:
    print(int(score))
if args.maxcombo:
    print(int(maxcombo))
if args.mods:
    if mods != 0:
        print(str(mods))
if args.time:
    print(str(time))
if args.accuracy:
    print(str(accuracy) + "%")
if args.beatmaphash:
    print(str(beatmaphash))
if args.rawaccuracy:
    print(str(raw_accuracy))