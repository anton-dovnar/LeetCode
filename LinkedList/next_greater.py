# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        result, stack = [], []
        length = 0
        while head:
            while stack and stack[-1][1] < head.val:
                result[stack.pop()[0]] = head.val
            stack.append([length, head.val])
            result.append(0)
            length += 1
            head = head.next
        return result
