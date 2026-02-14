# 206. Reverse Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reversedList(head):
    prev = None
    current = head

    while current:
        nextNode = current.next
        current.next = prev
        prev = current
        current = nextNode

    return prev


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)


newHead = reversedList(head)

while newHead:
    print(newHead.val, end=" -> ")
    newHead = newHead.next
