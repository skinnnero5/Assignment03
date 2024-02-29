import requests
import json
import redis

set_code = 'RVR'

response = requests.get('https://api.scryfall.com/cards/search?q=set%3A' + set_code + '+rarity>%3DR')

data = response.json()

json_formatted_str = json.dumps(data, indent=2)

#print(json_formatted_str)

import pandas as pd
from db_config import get_redis_connection

r = get_redis_connection()

r.flushall()

for card in data['data']:
    name = card['name']
    r.json().set('cards:' + set_code + ':' + name, '.', json.dumps(card))
    print(f"Name: {name}")

# Get JSON and decode 
json_data = r.json().get('cards:' + set_code + ':' + 'Karn, the Great Creator',)
data2 = json.loads(json_data)

# Extract fields  
name = data2['type_line']
print(name)

