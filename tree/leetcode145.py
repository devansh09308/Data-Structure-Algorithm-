# 145. Binary Tree Postorder Traversal

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder(root):
    result = []
    def dfs(root):

        if root is None:
            return
        dfs(root.left)
        dfs(root.right)
        result.append(root.val)

    dfs(root)
    return result

p = TreeNode(1)
p.left = TreeNode(2)
p.left.left = TreeNode(4)
p.left.right = TreeNode(5)
p.right = TreeNode(6)
p.right.left = TreeNode(7)
p.right.right = TreeNode(8)

print(preorder(p))