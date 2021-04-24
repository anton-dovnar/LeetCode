class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def middleNode(head: ListNode) -> ListNode:
    length = 0
    temp = head
    while temp:
        length += 1
        temp = temp.next

    idx = 0
    length = length + 1 if length % 2 == 0 else length
    while head:
        if idx == length // 2:
            return head
        head = head.next
        idx += 1


if __name__ == "__main__":
    data1 = [1, 2, 3, 4, 5]

    list1 = ListNode(data1[0])
    temp1 = list1

    for i in range(1, len(data1)):
        temp1.next = ListNode(data1[i])
        temp1 = temp1.next

    print(print_list(list1))
    result = middleNode(list1)
    print(print_list(result))
