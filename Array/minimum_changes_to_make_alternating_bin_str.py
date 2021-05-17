from itertools import zip_longest

class Solution:
    def minOperations(self, s: str) -> int:
        min_operations = float('inf')
        min_operations = min(min_operations, self.helper('1', '0', s))
        min_operations = min(min_operations, self.helper('0', '1', s))
        return min_operations

    def helper(self, a, b, s):
        counter = 0
        for i, k in zip_longest(s[1::2], s[0::2], fillvalue='01'):
            if a not in i:
                counter += 1
            if b not in k:
                counter += 1
        return counter
