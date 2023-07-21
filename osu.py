from osrparse import  Replay, parse_replay_data
import base64
import lzma
import argparse
replay = Replay.from_path("replay.osr")
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
raw_accuracy = ( ( 50 * count50 + 100 * count100 + 300 * count300 ) / ( 300 * (count50 + count100 + count300 + misscount) ) ) * 100
accuracy = round(raw_accuracy, 2)
beatmap_hash = r.beatmap_hash


parser = argparse.ArgumentParser(description='osu! replay parser')

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
parser.add_argument('-n', '--beatmap_hash', action='store_true', help='Beatmap hash')

args = parser.parse_args()

mode_value = args.mode
user_value = args.user
count300_value = args.count300
count100_value = args.count100
count50_value = args.count50
gcount_value = args.gcount
misscount_value = args.misscount
score_value = args.score
maxcombo_value = args.maxcombo
mods_value = args.mods
time_value = args.time
accuracy_value = args.accuracy
beatmap_hash_value = args.beatmap_hash


if mode_value :
    print(str(mode))
if user_value:
    print(str(user))
if count300_value:
    print(int(count300))
if count100_value:
    print(int(count100))
if count50_value:
    print(int(count50))
if gcount_value:
    print(int(gcount))
if misscount_value:
    print(int(misscount))
if score_value:
    print(int(score))
if maxcombo_value:
    print(int(maxcombo))
if mods_value:
    print(str(mods))
if time_value:
    print(str(time))
if accuracy_value:
    print(str(accuracy) + "%")
if beatmap_hash_value:
    print(str(beatmap_hash))