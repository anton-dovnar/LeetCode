"""
Remove Outermost Parentheses

Runtime: 36 ms, faster than 80.25% of Python3 online submissions
for Remove Outermost Parentheses.
Memory Usage: 14.1 MB, less than 94.74% of Python3 online submissions
for Remove Outermost Parentheses.
"""


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        flag = False
        stack = []
        result = []
        brackets = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for bracket in s:
            if flag:
                result.append(bracket)
                if bracket not in brackets:
                    stack.append(bracket)
                else:
                    if not stack:
                        result.pop()
                        flag = False
                    else:
                        stack.pop()
            else:
                flag = True
        return "".join(result)
