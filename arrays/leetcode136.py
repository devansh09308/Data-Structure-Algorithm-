# Single Number – LeetCode 136
def single(nums):
    result = 0

    for n in nums:
        result = result ^ n
    return result
         

nums = [4,1,2,1,2]

print(single(nums))