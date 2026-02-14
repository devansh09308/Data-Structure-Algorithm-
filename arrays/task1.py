def arr_len(arr):
    count = 0
    for _ in arr:
        count += 1
    return count

def search_index(arr, target):
    low = 0
    length = arr_len(arr)
    high = length - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        
        if arr[low] <= arr[mid]:
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
            
            
    return -1

nums = [4,5,6,7,0,1,2,3]
target = 3

print(search_index(nums, target))