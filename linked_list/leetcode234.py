# 234. palindrome linked list

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def duplicate(self, head):
        if not head:
            return True
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev, curr = None, slow
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left, right = left.next, right.next
        return True

# Example usage
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(5)

sol = Solution()
print(sol.duplicate(head))
