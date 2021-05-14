class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        vals = set(arr)
        min_diff = min([arr[i+1] - arr[i] for i in range(len(arr)-1)])
        result = []
        for i in arr:
            pair = i + min_diff
            if pair in vals:
                result.append([i, pair])
        return result
