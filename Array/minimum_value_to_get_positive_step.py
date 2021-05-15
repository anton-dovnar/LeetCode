from itertools import accumulate

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        return max(1, -min(accumulate(nums)) + 1)
