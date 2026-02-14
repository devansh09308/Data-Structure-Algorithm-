class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def validateBst(root):
    def dfs(root, low, high):
        if not root:
            return True

        if not (low < root.val < high):
            return False
        
        return dfs(root.left, low, root.val) and dfs(root.right, root.val, high)
    
    return dfs(root, float('-inf'), float('inf'))

p = TreeNode(5)
p.left = TreeNode(1)
p.right = TreeNode(14)
p.right.left = TreeNode(13)
p.right.right = TreeNode(16)

print(validateBst(p))
