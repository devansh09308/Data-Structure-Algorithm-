def find(nums, target):
    mp = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff in mp:
            return [mp[diff], i]
        mp[num] = i

nums = [2,7,11,15]
target = 9

print(find(nums, target))