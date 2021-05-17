class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if k < arr[0]:
            return k
        temp = set(arr)
        for i in self.infinite_sequence():
            if i not in temp:
                k -= 1
            if k == 0:
                return i

    def infinite_sequence(self):
        num = 1
        while True:
            yield num
            num += 1
