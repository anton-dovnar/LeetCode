"""
Check if One String Swap Can Make Strings Equal
"""
from collections import Counter

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        non_equal_elements = 0
        for letter_s1, letter_s2 in zip(s1, s2):
            if letter_s1 != letter_s2:
                non_equal_elements += 1

        s1_count = Counter(s1)
        s2_count = Counter(s2)
        intersection = s1_count & s2_count
        return non_equal_elements == 2 and sum(intersection.values()) == len(s1)
