"""
Build an Array With Stack Operations

Runtime: 28 ms, faster than 89.88% of Python3 online submissions
for Build an Array With Stack Operations.
Memory Usage: 14.3 MB, less than 48.84% of Python3 online submissions
for Build an Array With Stack Operations.
"""


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        pointer = 0
        for number in range(1, n + 1):
            if pointer > len(target) - 1:
                break
            stack.append("Push")
            if number != target[pointer]:
                stack.append("Pop")
                pointer -= 1
            pointer += 1
        return stack
