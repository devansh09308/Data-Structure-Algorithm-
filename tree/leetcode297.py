class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    res = []

    def dfs(root):
        if not root:
            res.append(str("#"))
            return
        
        res.append(str(root.val))
        dfs(root.left)
        dfs(root.right)

    dfs(root)
    return ','.join(res)

def deserialize(data):
    values = iter(data.split(','))

    def dfs():
        val = next(values)
        if val == '#':
            return None
        
        node = TreeNode(int(val))
        node.left = dfs()
        node.right = dfs
        return node

    return dfs()

        
    


p = TreeNode(1)

p.left = TreeNode(2)
p.right = TreeNode(3)

p.right.left = TreeNode(4)
p.right.right = TreeNode(5)
