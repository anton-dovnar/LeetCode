"""
Crawler Log Folder

Runtime: 44 ms, faster than 80.74% of Python3 online submissions
for Crawler Log Folder.
Memory Usage: 14.3 MB, less than 81.07% of Python3 online submissions
for Crawler Log Folder.
"""


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for operation in logs:
            if operation != "./"  and operation != "../":
                stack.append(operation)
            elif operation == "../":
                if stack:
                    stack.pop()
        return len(stack)
