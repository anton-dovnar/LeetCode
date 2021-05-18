class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        repeated = 0
        for i in range(m, len(arr)):
            repeated = repeated + 1 if arr[i] == arr[i-m] else 0
            if repeated == (k-1) * m:
                return True
        return False
