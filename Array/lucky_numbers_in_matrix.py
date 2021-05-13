class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        min_rows = set()
        max_cols = set()
        for c in range(cols):
            max_col = 0
            for r in range(rows):
                min_rows.add(min(matrix[r]))
                max_col = max(max_col, matrix[r][c])
            max_cols.add(max_col)
        return min_rows & max_cols
