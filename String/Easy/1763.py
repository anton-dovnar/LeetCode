"""
Longest Nice Substring
"""


class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        diff = set(s) - set(s.swapcase())
        if not diff:
            return s
        return max(map(self.longestNiceSubstring, s.split(diff.pop())), key=len)
