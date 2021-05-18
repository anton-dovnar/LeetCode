class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) < 2:
            return [str(n) for n in nums]
        result = []
        start = str(nums[0])
        end = '0'
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                end = str(nums[i-1])
                result.append([start, end])
                start = str(nums[i])
        result.append([start, str(nums[i])])
        return ['->'.join(r) if r[0] != r[1] else r[0] for r in result]
