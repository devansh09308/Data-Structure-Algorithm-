def arr_len(arr):
    count = 0
    for _ in arr:
        count += 1
    return count

def lower_bound(arr, target):
    low = 0
    length = arr_len(arr)
    high = length - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] <= target:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return ans

number = [1,2,3,5,6,7,8]
target = 4
print(number[lower_bound(number, target)])