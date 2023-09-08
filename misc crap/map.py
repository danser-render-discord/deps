import requests
import sys 

api_key = sys.argv[1]
beatmap_hash = sys.argv[2]

url = f'https://osu.ppy.sh/api/get_beatmaps?k={api_key}&h={beatmap_hash}'

response = requests.get(url)

if response.status_code == 200:

  data = response.json()

  # Get first beatmap
  beatmap = data[0] 

  name = beatmap['title']
  artist = beatmap['artist']
  difficulty = beatmap['version']

  print(f"{artist} - {name} [{difficulty}]")

else:
  print('Error retrieving beatmap data')