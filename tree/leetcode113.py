# 112. Path Sum

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumCheck(root, target):
    result = []

    def dfs(node, targetsum, path):
        if not node:
            return
        
        path.append(node.val)
        targetsum -= node.val

        if not node.left and not node.right and targetsum == 0:
            result.append(path[ :])

        dfs(node.left, targetsum, path)
        dfs(node.right, targetsum, path)

        path.pop()


    dfs(root, target, [])
    return result

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)
root.right.right.left = TreeNode(5)

target = 22

print(sumCheck(root, target))