def greaterElement(nums1, nums2):
    nxt = {}
    stack = []

    for v in nums2:
        while stack and v > stack[-1]:
            nxt[stack.pop()] = v
        stack.append(v)

    return [nxt.get(v, -1) for v in nums1]

nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(greaterElement(nums1, nums2))