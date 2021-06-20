"""
Uncommon Words from Two Sentences
"""


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split()
        s2 = s2.split()
        return [word for word in set(s1) ^ set(s2) if s1.count(word) + s2.count(word) == 1]
