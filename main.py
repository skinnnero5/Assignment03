from scryfall_fetcher import ScryfallFetcher
from redis_interface import RedisInterface
from card_charter import CardCharter
import json

set = 'RVR'
search_params = {'rarity': 'M'}

#cards = ScryfallFetcher.fetch_cards(set, search_params)

redis_interface = RedisInterface()
#redis_interface.flush()
#redis_interface.insert_cards(set, cards)

card_name = 'Karn, the Great Creator'
json_data = redis_interface.get_cards(set, card_name,)
data = json.loads(json_data)
 
print(f"Type line for {card_name} is {data['type_line']}.")

data = redis_interface.get_cards(set)
CardCharter.display_pie_chart(data, set)

