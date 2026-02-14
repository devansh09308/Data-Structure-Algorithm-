# Intersection of Two Arrays II – LeetCode 350
def intersection(nums1, nums2):
    freq = {}

    for n in nums1:
        freq[n] = freq.get(n, 0) + 1

    result = []

    for num in nums2:
        if num in freq and freq[num] > 0:
            result.append(num)
            freq[num] -= 1

    return result


nums1 = [4,9,5, 4]
nums2 = [9,4,9,8,4]

print(intersection(nums1, nums2))