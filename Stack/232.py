"""
Implement Queue using Stacks

Runtime: 32 ms, faster than 56.56% of Python3 online submissions
for Implement Queue using Stacks.
Memory Usage: 14.3 MB, less than 71.42% of Python3 online submissions
for Implement Queue using Stacks.
"""


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.stack.pop(0)


    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack[0]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
