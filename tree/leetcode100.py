class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSame(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    
    if p.val != q.val:
        return False
    
    return isSame(p.left, q.left) and isSame(p.right, q.right)
    

p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)
p.left.left = TreeNode(4)
p.left.right = TreeNode(5)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)
q.left.left = TreeNode(4)
q.left.right = TreeNode(6)

print(isSame(p, q))  # Output: True
