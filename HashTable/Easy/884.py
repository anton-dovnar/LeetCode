"""
Uncommon Words from Two Sentences
"""


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        return set(s1.split()) ^ set(s2.split())
