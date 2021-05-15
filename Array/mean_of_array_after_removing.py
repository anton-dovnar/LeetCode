class Solution:
    def trimMean(self, arr: List[int]) -> float:
        length = len(arr)
        arr.sort()
        remaining = (length // 10) // 2
        result = arr[remaining:-remaining]
        return sum(result) / len(result)
