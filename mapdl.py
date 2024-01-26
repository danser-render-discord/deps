import requests
import os
import sys

def download_beatmap(beatmap_id):
    url = f"https://api.chimu.moe/v1/download/{beatmap_id}"
    response = requests.get(url)
    if response.status_code == 200:
        filename = response.headers['Content-Disposition'].split('=')[1]
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Beatmap {beatmap_id} downloaded successfully!")
    else:
        print(f"Failed to download beatmap {beatmap_id}.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <beatmap_id>")
    else:
        beatmap_id = sys.argv[1]
        download_beatmap(beatmap_id)
