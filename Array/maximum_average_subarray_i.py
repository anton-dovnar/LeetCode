class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        entry_sum = sum(nums[:k])
        max_sum = entry_sum
        for i in range(k, len(nums)):
            entry_sum += nums[i] - nums[i-k];
            max_sum = max(max_sum, entry_sum);
        return max_sum / k
