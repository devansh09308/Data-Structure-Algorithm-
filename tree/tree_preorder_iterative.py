class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder_iterative(root):
    if root is None:
        return
    
    stack = [root]

    while stack:
        node = stack.pop()
        print(node.val, end=" ")

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(preorder_iterative(root))