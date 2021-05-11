class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums

        counter = nums[0]
        for key, val in enumerate(nums[1:], 1):
            counter += val
            nums[key] = counter
        return nums
