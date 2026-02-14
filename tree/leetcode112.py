# 112. Path Sum

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumCheck(root, target):
    if root is None:
        return False
    if not root.left and not root.right:
        return target == root.val
    
    target -= root.val

    return sumCheck(root.left, target) or sumCheck(root.right, target)
        

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

target = 22

print(sumCheck(root, target))