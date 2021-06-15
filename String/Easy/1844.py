"""
Replace All Digits with Characters
"""

from itertools import zip_longest


class Solution:
    def replaceDigits(self, s: str) -> str:
        return "".join([letter + chr(ord(letter) + int(number)) if number else letter for letter, number in zip_longest(s[::2], s[1::2])])
