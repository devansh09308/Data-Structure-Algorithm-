# Intersection of Two Arrays – LeetCode 349
def intersection(nums1, nums2):
    set1 = set(nums1)
    result = set()

    for num in nums2:
        if num in set1:
            result.add(num)
        
    return result



nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

print(intersection(nums1, nums2))