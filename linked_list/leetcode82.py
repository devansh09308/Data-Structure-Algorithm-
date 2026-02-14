# 82 – Remove Duplicates from Sorted List II

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def duplicate(self, head):
        dummy = ListNode(-1)
        dummy.next = head

        prev = dummy
        current = head

        while current:
            if current.next and current.val == current.next.val:
                dup_val = current.val

                while current and current.val == dup_val:
                    current = current.next

                prev.next = current
            
            else:
                prev = current
                current = current.next

        return dummy.next

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