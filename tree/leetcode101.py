# 101. Symmetric Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root):
    def isSame(p, q):
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        return isSame(p.left, q.left) and isSame(p.right, q.right)
    
    return isSame(root.left, root.right)
        
    

p = TreeNode(1)
p.left = TreeNode(2)
p.left.left = TreeNode(4)
p.left.right = TreeNode(5)
p.right = TreeNode(2)
p.right.left = TreeNode(4)
p.right.right = TreeNode(5)

print(isSymmetric(p))


