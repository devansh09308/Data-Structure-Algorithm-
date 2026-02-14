# 138 – Copy List with Random Pointer

class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):

        if not head or not head.next:
            return None
        current = head
        while current:
            newNode = Node(current.val)
            newNode.next = current.next
            current.next = newNode
            current = newNode.next
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        current = head
        newHead = head.next
        newHeadcurr = newHead

        while current:
            current.next = newHeadcurr.next
            current = current.next
            if current:
                newHeadcurr.next = current.next
                newHeadcurr = newHeadcurr.next

        return newHead

nodes = [
    Node(7),
    Node(13),
    Node(11),
    Node(10),
    Node(1)
]
for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i + 1]
nodes[0].random = None        # 7 -> null
nodes[1].random = nodes[0]   # 13 -> 7
nodes[2].random = nodes[4]   # 11 -> 1
nodes[3].random = nodes[2]   # 10 -> 11
nodes[4].random = nodes[0]   # 1 -> 7

head = nodes[0]
sol = Solution()
current = sol.copyRandomList(head)

print('this is original node')
curr = head
index = 0
while curr:
    rand = curr.random.val if curr.random else None
    print(f"Node {index}: val={curr.val}, random={rand}")
    curr = curr.next
    index += 1

print('this is duplicate node')

curr = current
index = 0
while curr:
    rand = curr.random.val if curr.random else None
    print(f"Node {index}: val={curr.val}, random={rand}")
    curr = curr.next
    index += 1