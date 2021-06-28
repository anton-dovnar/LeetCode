"""
Sort an Array
"""
import random


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        else:
            pivot = random.choice(nums)
            less = [number for number in nums if number < pivot]
            equal = [number for number in nums if number == pivot]
            greater = [number for number in nums if number > pivot]
        return self.sortArray(less) + equal + self.sortArray(greater)
