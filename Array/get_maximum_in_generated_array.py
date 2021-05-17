class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        result = [0, 1, 1]
        if n <= 2:
            return result[n]
        distance = n - 1 if n % 2 else n - 2
        nums = result + [0 for _ in range(distance)]
        i = 1
        while distance:
            nums[i * 2] = nums[i]
            nums[i * 2 + 1] = nums[i] + nums[i+1]
            i += 1
            distance -= 2
        return max(nums)
