"""
Maximum Product Difference Between Two Pairs
"""
import random
import math


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        def quicksort(nums):
            if len(nums) < 2:
                return nums
            else:
                pivot = random.choice(nums)
                less = [number for number in nums if number < pivot]
                equal = [number for number in nums if number == pivot]
                greater = [number for number in nums if number > pivot]
                return quicksort(less) + equal + quicksort(greater)

        nums = quicksort(nums)
        return math.prod(nums[-2:]) - math.prod(nums[:2])
