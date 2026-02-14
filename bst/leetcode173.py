class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root:TreeNode):
        self.stack = []
        self.pushLeft(root)

    def pushLeft(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        node = self.stack.pop()
        val = node.val

        if node.right:
            self.pushLeft(node.right)

        return val
    
    def hasNext(self):
        return len(self.stack) > 0
    
root = TreeNode(7)
root.left = TreeNode(3)
root.right = TreeNode(15)
root.right.left = TreeNode(9)
root.right.right = TreeNode(20)

it = BSTIterator(root)
result = []
while it.hasNext():
    result.append(it.next())

print(result)