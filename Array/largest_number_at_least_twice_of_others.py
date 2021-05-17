class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num = max(nums)
        idx = nums.index(max_num)
        for i, n in enumerate(nums):
            if max_num < n * 2 and n != max_num:
                return -1
        return idx
