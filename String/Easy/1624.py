"""
Largest Substring Between Two Equal Characters
"""

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        if not s:
            return -1

        longest = 0
        match = False
        for letter in s:
            if (left_idx := s.index(letter)) != (right_idx := s.rindex(letter)):
                longest = max(right_idx - (left_idx + 1), longest)
                match = True

        return -1 if not longest and not match else longest
