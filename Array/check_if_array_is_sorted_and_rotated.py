class Solution:
    def check(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            if nums[i+1] < nums[i]:
                return nums[i+1:] + nums[:i+1] == sorted(nums)
        return True
