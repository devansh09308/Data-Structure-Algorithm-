from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def queue_serialize(root):
    if not root:
        return []
    
    q = deque([root])
    result = []

    while q:
        level_size = len(q)
        for i in range(level_size):
            node = q.popleft()

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

            if i == level_size - 1:
                result.append(node.val)

    return result

p = TreeNode(1)

p.left = TreeNode(2)
p.right = TreeNode(3)

p.left.right = TreeNode(5)
p.right.right = TreeNode(4)

print(queue_serialize(p))
