import requests
import sys

if len(sys.argv) < 3:
  print("Usage: python script.py <api_key> <hash>")
  sys.exit()

API_KEY = sys.argv[1]  
HASH = sys.argv[2]

url = f"https://osu.ppy.sh/api/get_beatmaps?k={API_KEY}&h={HASH}"

try:
  response = requests.get(url)
except Exception as e:
  print("Error:", e)
  exit()
  
if response.status_code != 200:
  print("Error getting beatmap info")
  exit()
  
data = response.json()

if len(data) > 0:
  beatmap = data[0]
  diffr = round(float(beatmap["difficultyrating"]), 2)
  print(diffr)
else: 
  print("Beatmap not found")
