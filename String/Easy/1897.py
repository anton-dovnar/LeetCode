from collections import Counter


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        characters = Counter("".join(words))
        for amount in characters.values():
            if amount % len(words):
                return False
        return True
