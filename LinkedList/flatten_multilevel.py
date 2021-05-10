"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        self.traversal(head)
        return head

    def traversal(self, node):
        while node:
            next_node = node.next
            if not next_node:
                tail = node

            if node.child:
                node.child.prev = node
                node.next = node.child
                child_tail = self.traversal(node.child)
                if next_node:
                    next_node.prev = child_tail
                child_tail.next = next_node
                node.child = None
            node = node.next
        return tail
