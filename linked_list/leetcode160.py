# 160 – Intersection of Two Linked Lists

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution():
    def intersectionList(self, list1, list2):
        if not list1 or not list2:
            return None
        pA , pB = list1, list2

        while pA != pB:
            pA = pA.next if pA else list2
            pB = pB.next if pB else list1
        return pA
    
common = ListNode(6)
common.next = ListNode(7)
common.next.next = ListNode(8)

list1 = ListNode(1)
list1.next = ListNode(3)
list1.next.next = ListNode(5)
list1.next.next.next = common

list2 = ListNode(2)
list2.next = ListNode(4)
list2.next.next = common


sol = Solution()
current = sol.intersectionList(list1, list2)
print(current.val)
# current = list2

# while current:
#     print(current.val)
#     current = current.next