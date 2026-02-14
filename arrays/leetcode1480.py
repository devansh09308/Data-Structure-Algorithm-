# Running Sum — LC 1480
def running(nums):
    for i in range(1, len(nums)):
        nums[i] = nums[i] + nums[i-1]
    return nums

nums = [1,2,3,4]

print(running(nums))