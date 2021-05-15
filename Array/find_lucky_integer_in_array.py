from itertools import groupby

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr.sort(reverse=True)
        for k, g in groupby(arr):
            if len(list(g)) == k:
                return k
        return -1
