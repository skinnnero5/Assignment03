import json

class CardSearcher:
    """Static class for performing search operations on the data."""

    @staticmethod
    def search_type(data, card_type):
        """
        Search for cards by type.

        Parameters:
        - data (list): List of JSON objects with Magic the Gathering card data.
        - card_type (str): Card type to search for. (ex: Land, Creature, Planeswalker)

        Returns:
        - result (list): A list of cards with a type_line that contains the given type.
        """

        result = []

        for card_data in data:
            card = json.loads(card_data)
            if card_type in card['type_line']:
                result.append(card)

        return result


