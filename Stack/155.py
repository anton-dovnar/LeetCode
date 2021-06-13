"""
Min Stack

Runtime: 44 ms, faster than 99.93% of Python3 online submissions
for Min Stack.
Memory Usage: 18 MB, less than 78.02% of Python3 online submissions
for Min Stack.
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minimum = [float('inf')]

    def push(self, val: int) -> None:
        if val <= self.minimum[-1]:
            self.minimum.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.minimum[-1]:
            self.minimum.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
