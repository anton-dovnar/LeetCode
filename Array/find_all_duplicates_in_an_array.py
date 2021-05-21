class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                result.append(num)
        return result
