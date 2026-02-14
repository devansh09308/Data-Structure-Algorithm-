# LeetCode 111

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder(root):
    if root is None:
        return
    
    print(root.val, end=" ")
    preorder(root.left)
    preorder(root.right)



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

preorder(root)