# 543. Diameter of Binary Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameter(root):
    diameter = 0
    def dfs(node):
        nonlocal diameter

        if not node:
            return 0
        
        left = dfs(node.left)
        right = dfs(node.right)

        diameter = max(diameter, left + right)

        return 1 + max(left, right)
    
    dfs(root)
    return diameter

p = TreeNode(1)
p.left = TreeNode(2)
p.left.left = TreeNode(4)
p.left.right = TreeNode(5)
p.right = TreeNode(3)

print(diameter(p))