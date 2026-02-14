class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def greaterTree(root):
    total = 0

    def dfs(root):
        nonlocal total
        if not root:
            return 
        dfs(root.right)

        total += root.val
        root.val = total

        dfs(root.left)

    dfs(root)
    return root

root = TreeNode(4)

# level 1
root.left = TreeNode(1)
root.right = TreeNode(6)

# level 2
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)

root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

# level 3
root.left.right.right = TreeNode(3)
root.right.right.right = TreeNode(8)


def inorder(root):
    if not root:
        return None
    
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)

inorder(root)
print("------")
inorder(greaterTree(root))

