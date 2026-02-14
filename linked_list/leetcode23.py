# 23 – Merge k Sorted Lists

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeList(self, linkedList):
        if not linkedList:
            return None
        
        while len(linkedList) > 1:
            merged = []
            for i in range (0, len(linkedList), 2):
                l1 = linkedList[i]
                l2 = linkedList[i + 1] if (i + 1) < len(linkedList) else None
                merged.append(self.mergingList(l1, l2))
            linkedList = merged

        return linkedList[0]
    
    def mergingList(self, l1, l2):

        dummy = ListNode(-1)
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        curr.next = l1 if l1 else l2

        return dummy.next
    
def build_linked_list(arr):
    dummy = ListNode(-1)
    curr = dummy

    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next

    return dummy.next

lists = [[1,4,5],[1,3,4],[2,6]]

linked_lists = []
for arr in lists:
    linked_lists.append(build_linked_list(arr))

sol = Solution()
current = sol.mergeList(linked_lists)
while current:
    print(current.val)
    current = current.next