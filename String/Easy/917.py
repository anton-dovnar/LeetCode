"""
Remove Only Letters
"""
import re
from string import ascii_letters


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = re.findall(r'[a-zA-Z]+', s)
        reversed_letters = "".join([letter[::-1] for letter in letters[::-1]])
        for i in range(len(s)):
            if s[i] not in ascii_letters:
                reversed_letters = reversed_letters[:i] + s[i] + reversed_letters[i:]
        return reversed_letters
