class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = set(numbers)
        for i, n in enumerate(numbers):
            diff = target - n
            if diff in nums:
                return i+1, len(numbers) - numbers[::-1].index(diff)
