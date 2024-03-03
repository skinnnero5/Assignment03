import json

class CardSearcher:
    """Class for performing search operations on the data."""

    @staticmethod
    def search_type(data, card_type):
        """Search for cards by type."""

        result = []

        for card_data in data:
            card = json.loads(card_data)
            if card_type in card['type_line']:
                result.append(card)

        return result


