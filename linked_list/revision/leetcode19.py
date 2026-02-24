# 19. Remove Nth Node From End of List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def duplicate(self, head, val):
        dummy = ListNode(-1)
        dummy.next = head
        slow = dummy
        fast = dummy

        for _ in range(val + 1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return dummy.next
# Example usage
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)

val = 3
sol = Solution()
current = sol.duplicate(head, val)
while current:
    print(current.val)
    current = current.next