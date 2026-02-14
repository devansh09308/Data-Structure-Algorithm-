# LeetCode 111

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert(root):
    if root is None:
        return 0
    
    root.left, root.right = root.right, root.left

    invert(root.left)
    invert(root.right)

    return root



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
root.left.left = TreeNode(5)
root.left.left.left = TreeNode(6)

print(invert(root))