class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        result = 1
        counter = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                counter += 1
            else:
                result = max(result, counter)
                counter = 1
        return max(result, counter)
