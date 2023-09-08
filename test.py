import requests
import sys
import os

if len(sys.argv) != 3:
  print("Usage: python download_beatmap.py <beatmap_hash> <api_key>")
  sys.exit(1)

beatmap_hash = sys.argv[1]
api_key = sys.argv[2]

api_url = f"https://osu.ppy.sh/api/get_beatmaps?k={api_key}&h={beatmap_hash}"

response = requests.get(api_url)
response.raise_for_status()

beatmap = response.json()[0]
filename = beatmap['file_name']

download_url = f"{api_url}&m=0"
download_response = requests.get(download_url)

with open(filename, "wb") as f:
  f.write(download_response.content)

print(f"Downloaded {filename}")