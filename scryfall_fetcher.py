import requests
from urllib.parse import urlencode

class ScryfallFetcher:
    """Static class for retreiving card data from Scryfall API given a set & additional parameters."""

    BASE_URL = "https://api.scryfall.com/cards/search"

    DEBUG = True

    @staticmethod
    def fetch_cards(set, search_params=None):
        """
        Fetch cards from Scryfall based on set abbreviation and search parameters.

        Parameters:
        - set (str): The Magic the Gathering set abbreviation (ex: 'RVR' for Ravnica Remastered).
        - search_params (dict): Additional search parameters for the Scryfall API.

        Returns:
        - list: A list of card data based on the query.
        """
        if not search_params:
            search_params = {}

        search_params['set'] = set

        # print the search_params for debugging
        #print("Search Parameters:", search_params)

        encoded_params = urlencode(search_params)
        encoded_params = encoded_params.replace('&', '+')
        full_url = f"{ScryfallFetcher.BASE_URL}?q={encoded_params}"

        # print the final URL for debugging
        #print("Final URL:", full_url)

        response = requests.get(full_url)

        if response.status_code == 200:
            cards = response.json().get('data', [])
            if ScryfallFetcher.DEBUG:
                for card in cards:
                    print(f"DEBUG| ScryfallFetcher fetched {card['name']}")
            return cards
        else:
            print(f"Error fetching cards. Status Code: {response.status_code}")
            error_details = response.json()
            print("Error Details:")
            print(error_details)
            return []