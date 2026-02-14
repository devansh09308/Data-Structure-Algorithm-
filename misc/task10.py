def peak(arr):
    low = 0 
    high = len(arr) - 1

    while low < high:
        mid = (low + high) // 2

        if arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return low

arr = [1,2,3,4,5,3,1]
print(peak(arr))
