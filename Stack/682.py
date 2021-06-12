"""
Baseball Game

Runtime: 32 ms, faster than 96.09% of Python3 online submissions
for Baseball Game.
Memory Usage: 14.5 MB, less than 14.42% of Python3 online submissions
for Baseball Game.
"""


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for operation in ops:
            if operation == "+":
                stack.append(stack[-2] + stack[-1])
            elif operation == "C":
                stack.pop()
            elif operation == "D":
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(operation))
        return sum(stack)
