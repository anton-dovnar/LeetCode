from collections import Counter

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        frequency = Counter(nums).most_common()
        shortest = float('inf')
        common = frequency[0][1]
        for value, times in frequency:
            if times == common:
                start = nums.index(value)
                end = length - nums[::-1].index(value)
                distance = len(nums[start:end])
                shortest = min(shortest, distance)
            else:
                break
        return shortest
