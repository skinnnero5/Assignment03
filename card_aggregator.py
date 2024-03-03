import json
import numbers

class CardAggregator:
    """Class for performing aggregation operations on the data."""

    DEBUG = False

    @staticmethod
    def calculate_total_price(data, set):
        """Return total price of all cards in a set"""

        unknown_price_cards = 0
        total_price = 0.00

        for card_data in data:
            card = json.loads(card_data)
            if CardAggregator.DEBUG:
                print(f"DEBUG| CardAggregator {card['name']} prices: {card['prices']}")
                print(f"DEBUG| CardAggregator {card['name']} prices[usd]: {card['prices']['usd']}")
            if not isinstance(float(card['prices']['usd']), numbers.Number):
                unknown_price_cards += 1
            else:
                total_price += float(card['prices']['usd'])
        
        if(unknown_price_cards > 0):
            print(f"Total price of cards in {set} is ${total_price}. {unknown_price_cards} did not have a valid price.")
        else:
            print(f"Total price of cards in {set} is ${total_price:.2f}.")
