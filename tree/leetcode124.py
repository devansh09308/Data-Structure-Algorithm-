# 124. Binary Tree Maximum Path Sum
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pathSum(root):
    maxSum = float('-inf')
    def dfs(node):
        if not node:
            return 0
        nonlocal maxSum
        left = max(0, dfs(node.left))
        right = max(0, dfs(node.right))

        maxSum = max(maxSum, node.val + left + right)

        return node.val + max(left, right)
    
    dfs(root)
    return maxSum

p = TreeNode(-10)
p.left = TreeNode(9)
p.right = TreeNode(20)
p.right.right = TreeNode(7)
p.right.left = TreeNode(15)

print(pathSum(p))