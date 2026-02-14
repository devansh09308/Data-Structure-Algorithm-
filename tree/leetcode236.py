class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lsa(root, p , q):  
    if not root:
        return None
    
    if root.val == p or root.val == q:
        return root
    
    left = lsa(root.left, p, q)
    right = lsa(root.right, p, q)

    if left and right:
        return root
    
    return left if left else right
    


root = TreeNode(3)

root.left = TreeNode(5)
root.right = TreeNode(1)

root.left.left = TreeNode(6)
root.left.right = TreeNode(2)

root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
 
p, q = 5, 1

result = lsa(root, p, q)
print(result.val)