# 61 – Rotate List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotatelist(self, head, k):
        if not head or not head.next or k == 0:
            return head
        count = 1
        tail = head

        while tail.next:
            tail = tail.next
            count += 1

        k = k % count
        if k == 0: 
            return head
        
        tail.next = head
        
        steps = count - k - 1

        temp = head
        for _ in range(steps):
            temp = temp.next
        
        new_node = temp.next
        temp.next = None

        return new_node

# Example usage
head = ListNode(1)
head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)
# head.next.next.next.next.next = ListNode(6)
# head.next.next.next.next.next.next = ListNode(7)
k = 2
sol = Solution()
current = sol.rotatelist(head, k)
while current:
    print(current.val)
    current = current.next