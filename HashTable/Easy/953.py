"""
Verifying an Alien Dictionary
"""


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hash_map = {value: key for key, value in enumerate(order)}
        trans = lambda x: tuple(hash_map[i] for i in x)
        return all(trans(words[i]) <= trans(words[i+1]) for i in range(len(words) - 1))
