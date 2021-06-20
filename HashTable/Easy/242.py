"""
Valid Anagram
"""
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = Counter(s)
        tt = Counter(t)
        ss.subtract(tt)
        for value in ss.values():
            if value != 0:
                return False
        return True
