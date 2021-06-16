"""
Substrings of Size Three with Distinct Characters
"""


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if not s:
            return 0
        counter = 0
        for i in range(len(s)-2):
            if len(set(s[i:i+3])) == 3:
                counter += 1
        return counter
