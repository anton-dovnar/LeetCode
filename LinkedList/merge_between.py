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


def mergeInBetween(list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
    dummy = temp = ListNode(0)
    idx = 0
    while list1:
        if idx == a and list2:
            while list2:
                temp.next = list2
                list2 = list2.next
                temp = temp.next
        else:
            if idx >= a and idx <= b:
                list1 = list1.next
            else:
                temp.next = list1
                list1 = list1.next
                temp = temp.next
            idx += 1
    return dummy.next



if __name__ == "__main__":
    data1 = [0, 1, 2, 3, 4, 5]
    data2 = [1000000, 1000001, 1000002]
    a = 3
    b = 4
    output = [0, 1, 2, 1000000, 1000001, 1000002, 5]

    list1 = ListNode(data1[0])
    list2 = ListNode(data2[0])
    temp1 = list1
    temp2 = list2

    for i in range(1, len(data1)):
        temp1.next = ListNode(data1[i])
        temp1 = temp1.next

    for i in range(1, len(data2)):
        temp2.next = ListNode(data2[i])
        temp2 = temp2.next

    print(print_list(list1))
    print(print_list(list2))
    result = mergeInBetween(list1, a, b, list2)
    print(print_list(result))
