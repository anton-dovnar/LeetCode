class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result = []
        count = 0
        for n in nums:
            count = count << 1 | n
            result.append(count % 5 == 0)
        return result
