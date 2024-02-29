import requests
import json

response = requests.get('https://api.scryfall.com/cards/search?q=mulldrifter+set%3ASLD')

data = response.json()

json_formatted_str = json.dumps(data, indent=2)

print(json_formatted_str)