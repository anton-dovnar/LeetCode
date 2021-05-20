class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        counter = 0
        for c in costs:
            if c > coins:
                break
            else:
                coins -= c
                counter += 1
        return counter
