def minimum_sum(arr, k):
    low = max(arr)
    high = sum(arr)

    while low < high:
        mid = (low + high) // 2

        current = 0
        needed = 1

        for i in arr:
            if current + i > mid:
                needed += 1
                current = 0
            current += i

        if needed > k:
            low = mid + 1
        else:
            high = mid

    return low

nums = [1, 100, 1, 100, 1]
k = 3

print(minimum_sum(nums, k))