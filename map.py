import argparse
import requests

parser = argparse.ArgumentParser(description='Retrieve beatmap ID from beatmap hash')
parser.add_argument('api_key', help='osu! API key')
parser.add_argument('beatmap_hash', help='beatmap hash')
args = parser.parse_args()

url = f'https://osu.ppy.sh/api/get_beatmaps?k={args.api_key}&h={args.beatmap_hash}'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    if data:
        beatmap_id = data[0]['beatmap_id']
        print(beatmap_id)
    else:
        print(f'No beatmaps found for hash {args.beatmap_hash}')
else:
    print(f'Request failed with status code {response.status_code}')