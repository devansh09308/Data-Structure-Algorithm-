class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def searchBst(root, target):
    if not root:
        return TreeNode(target)
    
    if target < root.val:
        root.left =  searchBst(root.left, target)
    else:
        root.right =  searchBst(root.right, target)
    
    return root

p = TreeNode(4)
p.left = TreeNode(2)
p.right = TreeNode(7)
p.left.left = TreeNode(1)
p.left.right = TreeNode(3)

target = 2

print(searchBst(p, target))
