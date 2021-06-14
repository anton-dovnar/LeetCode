"""
Maximum Nesting Depth of the Parentheses
"""


class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        max_depth = 0
        for letter in s:
            if letter == "(":
                depth += 1
            elif letter == ")":
                max_depth = max(depth, max_depth)
                depth -= 1
        return max_depth
