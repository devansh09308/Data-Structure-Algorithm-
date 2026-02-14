def nextGreaterElement(nums1, nums2):
    stack = []
    next_greater = {}

    for num in nums2:
        while stack and stack[-1] < num:
            prev = stack.pop()
            next_greater[prev] = num
        stack.append(num)

    while stack:
        next_greater[stack.pop()] = -1

    return [next_greater[num] for num in nums1]
# Example usage:

nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]

print(nextGreaterElement(nums1, nums2))  # Output: [-1, 3, -1]