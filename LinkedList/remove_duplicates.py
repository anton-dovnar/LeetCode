class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None

        curr = head
        next_node = curr.next
        while next_node:
            if next_node.val == curr.val:
                next_node = next_node.next
                if not next_node:
                    curr.next = None
            else:
                curr.next = next_node
                curr = next_node
                next_node = next_node.next
        return head
