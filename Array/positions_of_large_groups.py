from itertools import groupby

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        start = 0
        end = 0
        result = []
        for k, g in groupby(s):
            length = len(list(g))
            end += length
            if length >= 3:
                result.append([start, end-1])
            start = end
        return result
