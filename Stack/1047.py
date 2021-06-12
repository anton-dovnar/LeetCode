"""
Remove All Adjecent Duplicate In String

Runtime: 64 ms, faster than 88.22% of Python3 online submissions
for Remove All Adjacent Duplicates In String.
Memory Usage: 14.6 MB, less than 61.04% of Python3 online submissions
for Remove All Adjacent Duplicates In String.
"""


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for letter in s:
            if stack and stack[-1] == letter:
                stack.pop()
            else:
                stack.append(letter)
        return "".join(stack)
