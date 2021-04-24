def swapNodes(self, head: ListNode, k: int) -> ListNode:
    length = 0
    temp = head
    while temp:
        length += 1
        temp = temp.next

    if k == 1 and length == 1:
        return head
    elif length == 2:
        head.val, head.next.val = head.next.val, head.val
        return head

    first = None
    second = None
    idx = 1
    walker = head
    while walker:
        if idx == k:
            first = walker
        if idx == length - k + 1:
            second = walker
        if first and second:
            break

        idx += 1
        walker = walker.next
    first.val, second.val = second.val, first.val
    return head
