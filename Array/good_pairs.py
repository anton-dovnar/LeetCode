class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = 0
        for i in range(length := len(nums)):
            for j in range(i, length):
                if nums[i] == nums[j] and i < j:
                    pairs += 1
        return pairs
