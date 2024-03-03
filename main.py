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

data = redis_interface.get_cards(set)

# Demonstrate graphing functionality
print("Displaying graph based on database:")
CardCharter.display_color_pie_chart(data, set)

# Demonstrate aggregation functionality
print("Aggregating USD price of cards in database:")
CardAggregator.calculate_total_price(data, set)

# Demonstrate search functionality
card_type = "Planeswalker"

print(f"Searching database for cards that match the specified type:")
type_matches = CardSearcher.search_type(data, card_type)

print(f"{set} has {len(type_matches)} cards of the {card_type} type.")
if len(type_matches) > 0:
    for card in type_matches:
        print(card['name'])

