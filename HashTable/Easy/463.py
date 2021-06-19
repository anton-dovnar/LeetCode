"""
Island Perimeter
"""
from itertools import chain


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = ('0' + ''.join(str(r) for r in row) + '0' for row in grid)
        columns = ('0' + ''.join(str(c) for c in col) + '0' for col in zip(*grid))
        return sum(row.count('01') + row.count('10')  for row in chain(rows, columns))
