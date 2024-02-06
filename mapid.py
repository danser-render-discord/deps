import argparse
import requests
from osrparse import Replay

def get_beatmapset_id(api_key, replay_path):
    replay = Replay.from_path(replay_path)
    beatmap_hash = replay.beatmap_hash

    url = f'https://osu.ppy.sh/api/get_beatmaps?k={api_key}&h={beatmap_hash}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data:
            beatmapset_id = data[0]['beatmapset_id']
            return beatmapset_id
        else:
            return f'No beatmaps found for hash {beatmap_hash}'
    else:
        return f'Request failed with status code {response.status_code}'

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Retrieve beatmap ID from beatmap hash')
    parser.add_argument('api_key', help='osu! API key')
    parser.add_argument('replay_path', help='Path to the osu! replay file')
    args = parser.parse_args()

    result = get_beatmapset_id(args.api_key, args.replay_path)
    print(result)
