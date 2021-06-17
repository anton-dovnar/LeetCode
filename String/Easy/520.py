"""
Detect Capital
"""

import re


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capital_letters = re.findall(r'[A-Z]', word)
        return not capital_letters or (len(capital_letters) == 1 and word[0].isupper()) or len(word) == len(capital_letters)
