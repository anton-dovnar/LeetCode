"""
Second Largest Digit in a String
"""


class Solution:
    def secondHighest(self, s: str) -> int:
        digits = sorted([int(character) for character in set(s) if character.isdigit()])
        return digits[-2] if len(digits) > 1 else -1
