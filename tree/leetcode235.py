class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lca(root, p, q):
    if not root:
        return
    
    if p.val < root.val and q.val < root.val:
        return lca(root.left, p, q)
    if p.val > root.val and q.val > root.val:
        return lca(root.right, p, q)
    
    return root.val
    

root = TreeNode(6)

p = root.left = TreeNode(2)
root.right = TreeNode(8)

root.left.left = TreeNode(0)
q = root.left.right = TreeNode(4)

root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

root.right.left = TreeNode(7)
root.right.right = TreeNode(9)


print(lca(root, p, q))
