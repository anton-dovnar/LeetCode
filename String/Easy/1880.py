"""
Check if Word Equals Summations of Two Words
"""

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def get_numeric_value(word):
            return int("".join([str(ord(letter) - 97) for letter in word]))
        return get_numeric_value(firstWord) + get_numeric_value(secondWord) == get_numeric_value(targetWord)
