class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        for i in nums:
            if i % 2:
                odd.append(i)
            else:
                even.append(i)
        nums[::2], nums[1::2] = even, odd
        return nums
