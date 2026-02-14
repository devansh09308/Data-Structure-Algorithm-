# 154. Find Minimum in Rotated Sorted Array II

def search(arr):
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = (low + high) // 2

        if arr[mid] > arr[high]:
            low = mid + 1
        elif arr[mid] < arr[high]:
            high = mid
        else:
            high -= 1
    return arr[low]

nums = [2,2,2,0,1]

print(search(nums))