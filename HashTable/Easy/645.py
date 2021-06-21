"""
Set Mismatch
"""
from collections import Counter


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        goal = set(range(1, len(nums) + 1))
        return [Counter(nums).most_common(1)[0][0], (goal - set(nums)).pop()]
