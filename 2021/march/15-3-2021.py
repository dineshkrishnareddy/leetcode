"""
Encode and Decode TinyURL
https://leetcode.com/problems/encode-and-decode-tinyurl/
"""


class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        self.lut = {}  # look up table
        key = hex(abs(hash(longUrl)))
        self.lut[key] = longUrl
        return "http://tinyurl/" + key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        return self.lut[shortUrl.split("/")[-1]]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
