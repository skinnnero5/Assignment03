from scryfall_fetcher import ScryfallFetcher
from redis_interface import RedisInterface
from card_charter import CardCharter
from card_aggregator import CardAggregator
from card_searcher import CardSearcher
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

data = redis_interface.get_cards(set)
#CardCharter.display_color_pie_chart(data, set)

CardAggregator.calculate_total_price(data, set)

card_type = "Planeswalker"
type_matches = CardSearcher.search_type(data, card_type)

print(f"{set} has {len(type_matches)} cards of the {card_type} type.")
if len(type_matches) > 0:
    for card in type_matches:
        print(card['name'])

