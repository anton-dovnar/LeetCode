"""
Merge Strings Alternately
"""
from itertools import zip_longest

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return "".join([a + b if a and b else a or b for a, b in list(zip_longest(word1, word2))])
