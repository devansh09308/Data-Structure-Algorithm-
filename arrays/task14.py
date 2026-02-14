def findMedianSortedArrays(nums1, nums2):
    if len(nums2) > len(nums1):
        findMedianSortedArrays(nums2, nums1)
    
    m, n = len(nums1), len(nums2)

    low, high = 0, m

    while low <= high :
        i = (low + high) // 2
        j = (m + n + 1) // 2 - i

        left1 = float('-inf') if i == 0 else nums1[i-1]
        left2 = float('-inf') if j == 0 else nums2[j-1]

        right1 = float('inf') if i == m else nums1[i]
        right2 = float('inf') if j == n else nums2[j]

        if left1 <= right2 and left2 <= right1:
            if (m + n) % 2 == 1:
                return max(left1,left2)
            else:
                return (max(left1, left2) + min(right1, right2)) / 2
        elif left1 > right2:
            high = i - 1
        else:
            low = i + 1

    return 0

nums1 = [1, 3, 8, 9]
nums2 = [7, 11, 18, 19]



print(findMedianSortedArrays(nums1, nums2))
