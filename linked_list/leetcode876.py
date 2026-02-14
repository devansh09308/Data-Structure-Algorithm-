class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def functionName(self, head: ListNode) -> ListNode:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

# Example usage
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)

sol = Solution()
head = sol.functionName(head)

print(head.val)
# current = head
# while current:
#     print(current.val)
#     current = current.next