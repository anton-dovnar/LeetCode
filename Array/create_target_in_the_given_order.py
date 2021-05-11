class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        length = len(nums)
        if not nums or not index or length == 1:
            return nums

        target = [nums[0], ]
        for i in range(1, length):
            target.insert(index[i], nums[i])
        return target
