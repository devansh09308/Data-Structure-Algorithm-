# 92 – Reverse Linked List II

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reversedList2(self, head, left, right):
        if not head or left == right:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        current = prev.next
        for _ in range(right - left):
            temp = current.next
            current.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next

# Example usage
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)

left, right = 2, 5

sol = Solution()
current = sol.reversedList2(head, left, right)
while current:
    print(current.val)
    current = current.next