# 124. Binary Tree Maximum Path Sum
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelorder(root):
    result = []
    
    def dfs(node):
        if not root:
            return 
        
        if not node.left and not node.right:
            result.append(node)


p = TreeNode(3)
p.left = TreeNode(9)
p.right = TreeNode(20)
p.right.right = TreeNode(7)
p.right.left = TreeNode(15)

print(levelorder(p))