from pathlib import Path
from uuid import uuid4


class Codec:

    def __init__(self):
        self.url_map = dict()

    def encode(self, long_url: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        hash_value = uuid4().hex[:10]
        self.url_map[hash_value] = long_url
        return 'http://tinyurl.com/' + hash_value

    def decode(self, short_url: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.url_map[Path(short_url).name]
