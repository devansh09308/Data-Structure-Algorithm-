# 219. Contains Duplicate II
def duplicate(nums, k):
    map = {}

    for index, value in enumerate(nums):
        if value in map:
            if index - map[value] <= k:
                return True
        map[value] = index

    return False

nums = [1,2,3,1,2,3]
k = 2

print(duplicate(nums, k))