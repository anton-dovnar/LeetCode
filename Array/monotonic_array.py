class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        incr, dcr = [True, False] if nums[-1] >= nums[0] else [False, True]
        for i in range(len(nums) - 1):
            if incr and nums[i+1] >= nums[i]:
                continue
            elif dcr and nums[i+1] <= nums[i]:
                continue
            else:
                return False
        return True
