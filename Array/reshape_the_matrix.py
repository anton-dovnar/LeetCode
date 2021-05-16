class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        temp = sum(mat, [])
        if len(temp) != r * c:
            return mat
        step = len(temp) // r
        return [temp[i:i+step] for i in range(0, len(temp), step)]
