"""
Decrypt String from Alphabet to Integer Mapping
"""


class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = ""
        i = 0
        while i < len(s):
            if "#" in s[i:i+3]:
                result += chr(96 + int(s[i:i+2]))
                i += 3
            else:
                result += chr(96 + int(s[i]))
                i += 1
        return result
