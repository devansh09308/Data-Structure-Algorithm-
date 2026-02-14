class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deleteNode(root, key):
    if not root:
        return None
    
    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            successor = getMin(root.right)
            root.val = successor.val
            root.right = deleteNode(root.right, successor.val)
    return root

def getMin(root):
    while root.left:
        root = root.left
    return root
    

root = TreeNode(50)

root.left = TreeNode(30)
root.right = TreeNode(70)

root.left.left = TreeNode(20)
root.left.right = TreeNode(40)

root.left.left.left = TreeNode(10)
root.left.left.right = TreeNode(25)

root.left.right.right = TreeNode(45)

root.right.left = TreeNode(60)
root.right.right = TreeNode(80)

root.right.left.right = TreeNode(65)
root.right.right.right = TreeNode(90)


def inorder(root):
    if not root:
        return None
    
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)

inorder(root)
print("------")
inorder(deleteNode(root, 25))

