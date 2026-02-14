def arr_len(arr):
    count = 0 
    for _ in arr:
        count += 1
    return count


def missing(arr, k):
    low = 0
    length = arr_len(arr)
    high = length - 1

    while low <= high:
        mid = (low + high) // 2
        missing = arr[mid] - (mid + 1)
        if missing < k:
            low = mid + 1
        else:
            high = mid - 1

    return low + k

nums = [2,3,4,7,11]
k = 5

print(missing(nums, k))
