class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def duplicate(self, head, x):
        curr = head
        small = ListNode(0)
        large = ListNode(0)
        smallp= small
        largep = large

        while curr != None:
            if curr.val < x:
                smallp.next = curr
                smallp = smallp.next
            else:
                largep.next = curr
                largep = largep.next
            curr = curr.next

        smallp.next = large.next
        largep.next = None

        return small.next
# Example usage
head = ListNode(1)
head.next = ListNode(4)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(2)

val = 3
sol = Solution()
current = sol.duplicate(head, val)
while current:
    print(current.val)
    current = current.next