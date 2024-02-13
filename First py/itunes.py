import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()
    
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term="+ sys.argv[1])
file = response.json()

for result in file["results"]:
    print(result["trackName"])