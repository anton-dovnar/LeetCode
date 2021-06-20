"""
Find the Difference
"""
from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ss = Counter(s)
        tt = Counter(t)
        ss.subtract(tt)
        difference = ""
        for key, value in ss.items():
            if value != 0:
                difference += key
        return difference
