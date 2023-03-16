from requests import get

from API.config import config


class Starships:
    def __init__(self):

        self.url = f"{config['url']}/starships"

    def get(self):
        return get(f"{self.url}/{9}")
