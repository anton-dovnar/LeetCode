# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head
        p1 = head
        p2 = head.next
        while p2:
            p1.val, p2.val = p2.val, p1.val
            p2 = p2.next
            p1 = p1.next
            if p2:
                p1 = p1.next
                p2 = p2.next
        return head
