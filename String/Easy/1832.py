"""
Check if the Sentence is Pangram
"""
from string import ascii_lowercase

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return not (set(ascii_lowercase) - set(sentence))
