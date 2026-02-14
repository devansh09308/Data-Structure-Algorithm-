def arr_len(arr):
    count = 0
    for _ in arr:
        count += 1
    return count

def first_search(arr, target):
    low = 0
    length = arr_len(arr)
    high = length - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            ans = mid
            high = mid - 1

        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return ans

def last_search(arr, target):
    low = 0
    length = arr_len(arr)
    high = length - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            ans = mid
            low = mid + 1

        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return ans


nums = [5,7,7,8,8,10]
target = 8

index1 = first_search(nums, target)
index2 = last_search(nums, target)

print(index1, index2)