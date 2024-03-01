import json
import yaml
import redis

class RedisInterface:
    """Class for inserting into and querying the RedisJSON database."""

    def __init__(self):
        """
        Initializes the RedisInterface based on config.yaml.
        """
        self.config = self.load_config()
        self.r = self.get_redis_connection()
        

    def insert_cards(self, set, cards):
        """
        Inserts JSONs into RedisJSON given a set and a list of cards.

        Parameters:
        - set (str): The Magic the Gathering set abbreviation (ex: 'RVR' for Ravnica Remastered).
        - cards (list): List of cards in JSON format from Scryfall API.

        Returns:
        - result: 0 if successful, 1 if error.
        """
        for card in cards:
            name = card['name']
            self.r.json().set('cards:' + set + ':' + name, '.', json.dumps(card))
            print(f"Name: {name}")

    def get_cards(self, set, name = None):
        """Retrieves cards from database, default all from a set, or selected by name."""

        if name:
            json_data = self.r.json().get('cards:' + set + ':' + name,)
        else:
            json_data = self.r.json().get('cards:' + set,)

        return json_data
    
    def flush(self):
        """Flushes database."""
        self.r.flushall()

    #From https://github.com/gchandra10/redis_python/blob/main/11_redisjson.py
    def load_config(self):
        """Load configuration from the YAML file.

        Returns:
            dict: Configuration data.
        """
        with open("config.yaml", "r") as file:
            return yaml.safe_load(file)

    #From https://github.com/gchandra10/redis_python/blob/main/11_redisjson.py    
    def get_redis_connection(self):
        """Create a Redis connection using the configuration.

        Returns:
            Redis: Redis connection object.
        """
        return redis.Redis(
            host=self.config["redis"]["host"],
            port=self.config["redis"]["port"],
            db=0,
            decode_responses=True,
            username=self.config["redis"]["user"],
            password=self.config["redis"]["password"],
        )




        
