class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderTree(nums):
    
    stack = []
        
    for num in nums:
        curr = TreeNode(num)
        
        while stack and stack[-1].val < num:
            curr.left = stack.pop()
        
        if stack:
            stack[-1].right = curr
        
        stack.append(curr)
    
    return stack[0]



nums = [3,2,1,6,0,5]

print(preorderTree(nums))
