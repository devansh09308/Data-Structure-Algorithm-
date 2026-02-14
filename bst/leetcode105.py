class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderTree(preorder, inorder):
    idx_map = {val: i for i, val in enumerate(inorder)}
    pre_idx = 0

    def bst(left, right):
        nonlocal pre_idx
        if left > right:
                return None
        root_val = preorder[pre_idx]
        pre_idx += 1
        root = TreeNode(root_val)

        mid = idx_map[root_val]

        root.left = bst(left, mid - 1)
        root.right = bst(mid + 1, right)

        return root
    
    return bst(0, len(inorder) - 1)


preorder = [3, 9, 20, 15, 7]
inorder  = [9, 3, 15, 20, 7]

print(preorderTree(preorder, inorder))
