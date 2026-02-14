# 2 – Add Two Numbers
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution():
    def addSum(self, list1, list2):
        dummy = ListNode(-1)
        current = dummy
        carry = 0

        while list1 or list2 or carry:
            l1 = list1.val if list1 else 0
            l2 = list2.val if list2 else 0

            total = l1 + l2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            list1 = list1.next if list1 else None
            list2 = list2.next if list2 else None

        return dummy.next

# 342
list1 = ListNode(2)
list1.next = ListNode(4)
list1.next.next = ListNode(3)

# 465
list2 = ListNode(5)
list2.next = ListNode(6)
list2.next.next = ListNode(4)

sol = Solution()
current = sol.addSum(list1, list2)

while current:
    print(current.val)
    current = current.next