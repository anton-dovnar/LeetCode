class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = sum(n for n in nums if not n % 2)
        result = []
        for v, i in queries:
            if not nums[i] % 2:
                even_sum -= nums[i]
            nums[i] += v
            if not nums[i] % 2:
                even_sum += nums[i]
            result.append(even_sum)
        return result
