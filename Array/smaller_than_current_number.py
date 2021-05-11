class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(length := len(nums)):
            counter = 0
            for j in range(length):
                if nums[j] < nums[i]:
                    counter += 1
            result.append(counter)
        return result
