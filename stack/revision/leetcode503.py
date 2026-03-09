def greaterElement(nums):
    n = len(nums)
    result = [-1] * n
    stack = []

    for i in range(2 * n):
        idx = i % n

        while stack and nums[idx] > nums[stack[-1]]:
            result[stack.pop()] = nums[idx]
        
        if i < n:
            stack.append(i)

    return result
    
    
    
nums = [1,2,1]

print(greaterElement(nums))