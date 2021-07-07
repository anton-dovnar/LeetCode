"""
Kth Smallest Element in a Sorted Matrix
"""


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return sorted(sum(matrix, []))[k-1]
