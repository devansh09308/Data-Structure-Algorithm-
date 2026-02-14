# 217. Contains Duplicate
def repeat(nums):

    map = {}

    for i in nums:
        if i in map:
            return True
        else:
            map[i] = 1
    
    return False

nums = [1,1,1,3,3,4,3,2,4,2]
print(repeat(nums))