"""
Consecutive Characters
"""


class Solution:
    def maxPower(self, s: str) -> int:
        consecutive_max = 0
        counter = 0
        letter = s[0]
        for i in range(len(s)):
            if s[i] == letter:
                counter += 1
            else:
                consecutive_max = max(consecutive_max, counter)
                counter = 1
                letter = s[i]
        return max(consecutive_max, counter)
