"""
Split a String in Balanced Strings
"""


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balancer = 0
        partitions = 0
        for letter in s:
            if letter == "L":
                balancer += 1
            else:
                balancer -= 1
            if balancer == 0:
                partitions += 1
        return partitions
