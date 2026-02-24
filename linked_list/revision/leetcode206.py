# 206. Reverse Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reversedList(head):
    curr = head
    prev = None

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)


# newHead = reversedList(head)
newHead = head

while newHead:
    print(newHead.val, end=" -> ")
    newHead = newHead.next
