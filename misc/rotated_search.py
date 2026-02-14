def arr_len(arr):
    count = 0
    for _ in arr:
        count += 1
    return count


def search_rotated(arr, target):
    low = 0
    high = arr_len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        # Target found
        if arr[mid] == target:
            return mid

        # LEFT HALF IS SORTED
        if arr[low] <= arr[mid]:
            # Check if target lies in LEFT half
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

        # RIGHT HALF IS SORTED
        else:
            # Check if target lies in RIGHT half
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1
number = [4,5,6,7,0,1,2,3]
target = 4
print(search_rotated(number, target))
