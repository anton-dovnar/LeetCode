class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        peak = [[1]]
        peak.extend([[1,1] for i in range(numRows-1)])
        for row_idx in range(1, len(peak) - 1):
            offset = 0
            for col in range(row_idx):
                peak[row_idx+1].insert(col+1, sum(peak[row_idx][offset:offset+2]))
                offset += 1
        return peak
