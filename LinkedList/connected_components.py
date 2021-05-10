# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, nums: List[int]) -> int:
        nums = set(nums)
        count, prev = 0, None
        while head:
            if head.val in nums and prev not in nums:
                count += 1
            prev, head = head.val, head.next
        return count
