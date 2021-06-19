"""
N-Repeated Element in Size 2N Array
"""
from collections import Counter

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        return Counter(nums).most_common(1)[0][0]
