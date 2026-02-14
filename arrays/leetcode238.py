# 238. Product of Array Except Self (prefix + suffix)
def productExceptSelf(nums):
    output = [1] * len(nums)

    for i in range(1,len(nums)):
        output[i] = output[i-1] * nums[i-1]

    suffix = 1
    for i in range(len(nums)-1, -1, -1):
        output[i] *= suffix
        suffix *= nums[i]

    return output

nums = [-1,1,0,-3,3]
print(productExceptSelf(nums))