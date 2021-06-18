"""
Greatest Common Divisor of Strings
"""


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        while len(str1) != len(str2):
            if len(str1) < len(str2):
                str1, str2 = str2, str1
            if not str1.startswith(str2):
                return ""
            str1 = str1[len(str2): ]

        return str1 if str1 == str2 else ""
