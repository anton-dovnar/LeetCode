"""
Distribute Candies
"""


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        half = len(candyType) // 2
        return half if ( types := len(set(candyType))) > half else types
