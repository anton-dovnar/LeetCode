class Solution:
    def specialArray(self, nums: List[int]) -> int:
        max_range = max(nums)
        for x in range(1, max_range+1):
            count = 0
            for n in nums:
                if n >= x:
                    count += 1
            if x == count:
                return x
        return -1
