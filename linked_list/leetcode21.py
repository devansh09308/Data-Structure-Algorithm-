# 21. Merge Two Sorted Lists
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution():
    def mergedList(self, list1, list2):
        dummy = ListNode(-1)
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 or list2

        return dummy.next

# Example usage
list1 = ListNode(1)
list1.next = ListNode(3)
list1.next.next = ListNode(5)

list2 = ListNode(2)
list2.next = ListNode(4)
list2.next.next = ListNode(6)
list2.next.next.next = ListNode(7)
list2.next.next.next.next = ListNode(8)

sol = Solution()
current = sol.mergedList(list2, list1)

while current:
    print(current.val)
    current = current.next