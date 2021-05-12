class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counter = 0
        for i in range(len(nums)):
            if nums[i] not in nums[i+1:] and nums[i] not in nums[:i]:
                counter += nums[i]
        return counter
