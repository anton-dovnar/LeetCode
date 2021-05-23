import math


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        rotate = (length - k) % length
        if rotate == 0:
            return
        sets = math.gcd(rotate, length)
        for i in range(sets):
            temp = nums[i]
            j = i
            while True:
                k = j + rotate
                if k >= length:
                    k -= length
                if k == i:
                    break
                nums[j] = nums[k]
                j = k
            nums[j] = temp
