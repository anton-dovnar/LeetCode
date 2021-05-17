class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        peak = [1]
        for _ in range(rowIndex):
            peak = [x + y for x, y in zip([0]+peak, peak+[0])]
        return peak
