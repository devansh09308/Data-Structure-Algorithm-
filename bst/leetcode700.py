# 700. Search in a Binary Search Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def searchBst(root, target):
    if not root:
        return None
    
    if root.val == target:
        return root
   
    if target < root.val:
        return searchBst(root.left, target)
    else:
        return searchBst(root.right, target)

p = TreeNode(4)
p.left = TreeNode(2)
p.right = TreeNode(7)
p.left.left = TreeNode(1)
p.left.right = TreeNode(3)

target = 2

print(searchBst(p, target))
