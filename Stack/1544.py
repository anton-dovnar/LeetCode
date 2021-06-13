"""
Make The String Great

Runtime: 32 ms, faster than 85.55% of Python3 online submissions
for Make The String Great.
Memory Usage: 14.3 MB, less than 48.11% of Python3 online submissions
for Make The String Great.
"""


class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for letter in s:
            if stack and stack[-1] == letter.swapcase():
                stack.pop()
            else:
                stack.append(letter)
        return "".join(stack)
