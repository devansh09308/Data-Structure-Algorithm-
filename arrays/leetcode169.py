# Majority Element – LeetCode 169
def major(nums):
    count = 0 
    candidate = None

    for n in nums:
        if count == 0:
            candidate = n
        if n == candidate:
            count += 1
        else:
            count -= 1
    
    return candidate

nums = [5, 1, 2, 5, 5, 5, 3, 5, 4, 5, 6, 5, 7]
print(major(nums))