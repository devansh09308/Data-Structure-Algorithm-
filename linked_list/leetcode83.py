# 83 – Remove Duplicates from Sorted List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def duplicate(self, head):
        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
            
        return head

# Example usage
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(4)

sol = Solution()
current = sol.duplicate(head)
while current:
    print(current.val)
    current = current.next