# 347. Top K Frequent Elements

def find(nums, k):
    map = {}

    for i in nums:
        if i not in map:
            map[i] = 0
        map[i] += 1
    
    sorted_row = sorted(map, key=lambda x: map[x], reverse=True)

    return sorted_row[:k]


nums = [1,1,1,2,2,3,3,3,3,3,3,4]
k = 2

print(find(nums, k))