# LeetCode 111

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDepth(root):
    if root is None:
        return 0
    
    if root.left is None:
        return 1 + minDepth(root.right)
    
    if root.right is None:
        return 1 + minDepth(root.left)
    
    return 1 + min(minDepth(root.left), minDepth(root.right))



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
root.left.left = TreeNode(5)
root.left.left.left = TreeNode(6)

print(minDepth(root))