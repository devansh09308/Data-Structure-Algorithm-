class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def createTree(num):
    def bst(left, right):
        if left > right:
            return None
        
        mid  = (left + right) // 2
        root = TreeNode(num[mid])

        root.left = bst(left, mid - 1)
        root.right = bst(mid + 1, right)

        return root
    
    return bst(0, len(num) - 1)

num = [-10, -3, 0, 5, 9]
result = createTree(num)

def inorder(root):
    if not root:
        return None
    
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)

inorder(result)

