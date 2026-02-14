# 110. Balanced Binary Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(node):
    def dfs(node):
        if not node:
            return 0
        
        left = dfs(node.left)
        if left == -1:
            return -1
        
        right = dfs(node.right)
        if right == -1:
            return -1
        
        if abs(left - right) > 1:
            return -1
        
        return 1 + max(left, right)
    
    return dfs(node) != -1

p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)


print(isBalanced(p))