class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarr  = float('-inf')
        curr_sum = 0
        for n in nums:
            curr_sum = max(n, curr_sum + n)
            max_subarr = max(max_subarr, curr_sum)
        return max_subarr
