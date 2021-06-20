"""
Longest Harmonius Subsequence
"""
from collections import Counter


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        longest_harmonius = 0
        hash_map = Counter(nums)
        unique = set(nums)
        for number in unique:
            if number + 1 in unique:
                longest_harmonius = max(longest_harmonius, hash_map[number] + hash_map[number + 1])
        return longest_harmonius
