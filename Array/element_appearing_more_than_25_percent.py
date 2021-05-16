class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        target_times = len(arr) / 4
        prev = arr[0]
        occur = 1
        for i, v in enumerate(arr[1:], 1):
            if v == prev:
                occur += 1
            else:
                if occur > target_times:
                    return prev
                occur = 1
                prev = v
        return prev
