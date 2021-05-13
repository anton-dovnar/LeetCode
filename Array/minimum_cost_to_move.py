class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even = 0
        odd = 0
        for p in position:
            if p % 2:
                odd += 1
            else:
                even += 1
        return min(even, odd)
