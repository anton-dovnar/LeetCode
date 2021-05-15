class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        count = 0
        cols = list(zip(*mat))
        for row in mat:
            if sum(row) == 1:
                if sum(cols[row.index(1)]) == 1:
                    count += 1
        return count
