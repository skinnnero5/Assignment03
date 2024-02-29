from scryfall_fetcher import ScryfallFetcher
import json
import redis

set = 'RVR'
search_params = {'rarity': 'M'}

cards = ScryfallFetcher.fetch_cards(set, search_params)

for card in cards:
    print(card['name'])

import pandas as pd
from db_config import get_redis_connection

r = get_redis_connection()

r.flushall()

for card in cards:
    name = card['name']
    r.json().set('cards:' + set + ':' + name, '.', json.dumps(card))
    print(f"Name: {name}")

# Get JSON and decode 
json_data = r.json().get('cards:' + set + ':' + 'Karn, the Great Creator',)
data2 = json.loads(json_data)

# Extract fields  
name = data2['type_line']
print(name)
