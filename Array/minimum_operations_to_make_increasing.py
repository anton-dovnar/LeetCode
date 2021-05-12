class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = prev = 0
        for n in nums:
            if n <= prev:
                prev += 1
                operations += prev - n
            else:
                prev = n
        return operations
