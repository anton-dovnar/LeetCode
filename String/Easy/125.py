"""
Valid palindrome
"""
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = re.findall(r'[a-zA-Z0-9]', s)
        sentence = "".join(letters).lower()
        print(sentence)
        return sentence == sentence[::-1]
