"""
Valid Parentheses

Runtime: 24 ms, faster than 95.45% of Python3 online submissions
for Valid Parentheses.
Memory Usage: 14.1 MB, less than 86.19% of Python3 online submissions
for Valid Parentheses.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for bracket in s:
            if bracket not in brackets:
                stack.append(bracket)
            else:
                if not stack:
                    return False
                last_seen = stack.pop()
                if brackets[bracket] != last_seen:
                    return False
        return not stack
