# 560. Subarray Sum Equals K


def subarraySum(nums, k):
    count = 0
    prefix = 0
    map1 = {0:1}

    for num in nums:
        prefix += num

        if (prefix - k) in map1:
            count += map1[prefix - k]
        map1[prefix] = map1.get(prefix, 0) + 1
    
    return count

nums = [1,2,3,-3,1,1,1,4,2,-3]
k = 3

print(subarraySum(nums, k))