class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        length = len(arr)
        if length < 3:
            return False
        if length == 3 and sum(arr) % 2:
            return True
        for i in range(length - 3):
            if sum(arr[i:i+3]) % 2:
                return True
        return False
