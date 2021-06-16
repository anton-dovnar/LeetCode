"""
Longest Uncommon Subsequence I
"""


class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a != b:
            if len(a) > len(b):
                return len(a)
            else:
                return len(b)
        return -1
