class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postorder_iterative_using_two_stack(root):
    if root is None:
        return []
    
    stack1 = [root]
    stack2 = []

    while stack1:
        node = stack1.pop()
        stack2.append(node)

        if node.left:
            stack1.append(node.left)

        if node.right:
            stack1.append(node.right)

    while stack2:
        result = stack2.pop()
        print(result.val)


def postorder_iterative_using_one_stack(root):
    stack = []
    curr = root
    last = None
    result = []

    while curr or stack:
        if curr:
            stack.append(curr)
            curr = curr.left

        else:
            peek = stack[-1]
            
            if peek.right and last != peek.right:
                curr = peek.right
            else:
                result.append(peek.val)
                last = stack.pop()

    return result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(8)

# postorder_iterative_using_two_stack(root)
print(postorder_iterative_using_one_stack(root))