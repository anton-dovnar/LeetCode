class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True
        counter = 0
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                counter += 1
                if counter >= 2:
                    return False
                elif i - 2 < 0 or nums[i-2] <= nums[i]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
        return True
