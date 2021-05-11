class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_sum = 0
        for l in accounts:
            counter = 0
            for j in l:
                counter += j
            max_sum = max(max_sum, counter)
        return max_sum
