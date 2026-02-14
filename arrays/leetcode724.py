# 724. Find Pivot Index
def pivotSum(nums):
    totalsum = sum(nums)
    leftsum = 0 

    for i, num in enumerate(nums):
        rightsum = totalsum - leftsum - num
        if rightsum == leftsum:
            return i
        leftsum += num
    
    return -1

nums = [1,7,3,6,5,6]

print(pivotSum(nums))