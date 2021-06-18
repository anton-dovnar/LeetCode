"""
Maximum Repeating Substring
"""


class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        result = word
        while result in sequence:
            result += word
        return len(result) // len(word) - 1
