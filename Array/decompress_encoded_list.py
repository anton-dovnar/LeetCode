class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        i = 0
        while i < len(nums):
            for _ in range(nums[i]):
                result.append(nums[i+1])
            i += 2
        return result
