def arr_len(arr):
    count = 0 
    for _ in arr:
        count += 1
    return count

def peak(arr, low, high):


    while low <= high:
        mid = (low + high) // 2

        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return mid
        else:
            peak(arr, low, mid-1)
            peak(arr, mid+1, high)

    return -1

nums = [1,2,3,1]

length = arr_len(nums)
high = length - 1

print(peak(nums,0,high))