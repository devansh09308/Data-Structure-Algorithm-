# 24. Swap Nodes in Pairs

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        while prev.next and prev.next.next:
            first = prev.next
            second = first.next
            prev.next = second
            first.next = second.next
            second.next = first
            prev = first
        return dummy.next


# Example usage
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)

sol = Solution()
current = sol.swapPairs(head)
while current:
    print(current.val)
    current = current.next