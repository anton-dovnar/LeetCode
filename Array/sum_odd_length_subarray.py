class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        odd_numbers = list(range(1, 100, 2))
        length = len(arr)
        result = 0
        for i in odd_numbers:
            if i <= length:
                for j in range(length):
                    if len(arr[j:j+i]) == i:
                        result += sum(arr[j:j+i])
                    else:
                        break
        return result
