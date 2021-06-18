"""
Repeated Substring Pattern
"""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        double_string = (2*s)[1:-1]
        return double_string.find(s) != -1
