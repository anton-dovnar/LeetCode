"""
Partitioning into Minimum Number Of Deci-Binary Numbers
"""


class Solution:
    def minPartitions(self, n: str) -> int:
        return max(map(int, n))
