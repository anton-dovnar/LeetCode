"""
Increasing Decreasing String
"""
from collections import Counter

class Solution:
    def sortString(self, s: str) -> str:
        available_chars = Counter(s)
        unique_chars = sorted(set(s))
        result = ""
        flag = sum(available_chars.values())
        while flag > 0:
            for x in range(len(unique_chars)):
                if available_chars[unique_chars[x]]:
                    result += unique_chars[x]
                    available_chars[unique_chars[x]] -= 1
                    flag -= 1

            for x in range(len(unique_chars)-1, -1, -1):
                if available_chars[unique_chars[x]]:
                    result += unique_chars[x]
                    available_chars[unique_chars[x]] -= 1
                    flag -= 1
        return result
