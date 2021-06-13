"""
Next Greater Element I

Runtime: 40 ms, faster than 96.28% of Python3 online submissions
for Next Greater Element I.
Memory Usage: 14.4 MB, less than 69.27% of Python3 online submissions
for Next Greater Element I.
"""


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater_map = {}
        for number in nums2:
            while stack and stack[-1] < number:
                next_greater_map[stack.pop()] = number
            stack.append(number)

        return [next_greater_map.get(x, -1) for x in nums1]
