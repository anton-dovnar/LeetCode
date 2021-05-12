class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        matrix_size = len(mat)
        if matrix_size == 1:
            return mat[0][0]

        counter = 0
        j = matrix_size - 1
        for i in range(matrix_size):
            counter += mat[i][i]
            mat[i][i] = 0
            counter += mat[i][j]
            j -= 1

        return counter
