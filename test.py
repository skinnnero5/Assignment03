import requests
import json
import redis

response = requests.get('https://api.scryfall.com/cards/search?q=mulldrifter+set%3ASLD')

data = response.json()

json_formatted_str = json.dumps(data, indent=2)

print(json_formatted_str)

import pandas as pd
from db_config import get_redis_connection

r = get_redis_connection()

## r.flushall()

r.json().set('cards:blue:mulldrifer', '.', json.dumps(data))

# Get JSON and decode 
json_data = r.json().get('cards:blue:mulldrifer')
data2 = json.loads(json_data)

# Extract fields  
name = data2['data'][0]['name']

print(f"Name: {name}")