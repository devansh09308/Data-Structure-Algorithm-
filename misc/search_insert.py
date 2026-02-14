def arr_len(arr):
    c = 0
    for _ in arr:
        c += 1
    return c


def search_insert(arr, target):

    low = 0
    high = arr_len(arr) - 1
    ans = arr_len(arr)    # default insert at end

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        # If element is greater than target → possible insert position
        if arr[mid] > target:
            ans = mid
            high = mid - 1

        # If element is smaller → go right
        else:
            low = mid + 1

    return ans

arr = [2, 4, 7, 11, 15]
target = 9

print(search_insert(arr, target))  # 3
