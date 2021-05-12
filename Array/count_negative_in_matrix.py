class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        counter = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] < 0:
                    counter += 1
        return counter
