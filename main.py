from scryfall_fetcher import ScryfallFetcher
from redis_interface import RedisInterface
import json

set = 'RVR'
search_params = {'rarity': 'M'}

cards = ScryfallFetcher.fetch_cards(set, search_params)

for card in cards:
    print(card['name'])

redis_interface = RedisInterface()

redis_interface.flush()

redis_interface.insert_cards(set, cards)

# Get JSON and decode 
json_data = redis_interface.get_cards(set, 'Karn, the Great Creator',)
data = json.loads(json_data)

# Extract fields  
print(data['type_line'])
