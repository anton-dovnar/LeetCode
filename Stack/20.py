"""
Valid Parentheses

Runtime: 28 ms, faster than 84.89% of Python3 online submissions
for Valid Parentheses.
Memory Usage: 14.2 MB, less than 86.19% of Python3 online submissions
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
        return True if not stack else False
