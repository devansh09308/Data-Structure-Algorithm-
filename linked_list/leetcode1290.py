# # 1290. palindrome linked list

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getBinary(self, head):
        result = 0
        current = head
        while current:
            result = result * 2 + current.val
            current = current.next
        return result
        

# Example usage
head = ListNode(1)
head.next = ListNode(0)
head.next.next = ListNode(1)
head.next.next.next = ListNode(0)
head.next.next.next.next = ListNode(1)

sol = Solution()
print(sol.getBinary(head))
