# 25 – Reverse Nodes in k-Group

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head,k):
        dummy = ListNode(-1)
        dummy.next = head
        prev_group = dummy
        while True:
            kth = prev_group
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
        
            prev = kth.next
            current = prev_group.next

            for _ in range(k):
                temp = current.next
                current.next = prev
                prev = current
                current = temp

            temp = prev_group.next
            prev_group.next = prev
            prev_group = temp

# Example usage
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)
k = 3
sol = Solution()
current = sol.swapPairs(head, k)
while current:
    print(current.val)
    current = current.next