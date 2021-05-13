from operator import itemgetter

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        for i in range(len(mat)):
            mat[i] = i, sum(mat[i])
        return [i[0] for i in sorted(mat, key=itemgetter(1))[:k]]
