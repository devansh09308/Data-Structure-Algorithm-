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
    left_to_right = True

    while q:
        level_size = len(q)
        level = []

        for i in range(level_size):
            node = q.popleft()
            level.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        if not left_to_right:
            level.reverse()

        result.append(level)
        left_to_right = not left_to_right
        
    return result
            


p = TreeNode(3)

p.left = TreeNode(9)
p.right = TreeNode(20)

p.right.left = TreeNode(15)
p.right.right = TreeNode(7)

print(queue_serialize(p))
