"""
Length of Last Word
"""
import re

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(last_word[-1]) if (last_word := re.findall(r'[a-zA-Z]+', s)) else 0
