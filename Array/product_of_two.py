from itertools import combinations

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = float('-inf')
        for a, b in combinations(nums, 2):
            max_product = max(max_product, (a - 1) * (b - 1))
        return max_product
