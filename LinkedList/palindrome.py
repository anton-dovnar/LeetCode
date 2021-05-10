# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        length = 0
        p = head
        while p:
            length += 1
            p = p.next

        half = length // 2 if length % 2 == 0 else (length // 2) + 1
        prev = None
        for _ in range(half):
            head.next, prev, head = prev, head, head.next

        if length % 2 != 0:
            prev = prev.next

        while prev and head and prev.val == head.val:
            prev = prev.next
            head = head.next

        if not prev and not head:
            return True

        return False
