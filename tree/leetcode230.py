class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthsmallest(root, key):
    count = 0
    ans = 0

    def dfs(root, key):
        nonlocal ans
        nonlocal count
        if not root and ans is not None:
            return
        
        dfs(root.left, key)

        count += 1
        if count == key:
            ans = root.val
            return
        
        dfs(root.right, key)

    dfs(root, key)
    return ans
    

root = TreeNode(3)

root.left = TreeNode(1)
root.right = TreeNode(4)

root.left.right = TreeNode(2)

key = 3

print(kthsmallest(root, key))
