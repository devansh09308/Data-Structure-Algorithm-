def arr_len(arr):
    count = 0
    for _ in arr:
        count += 1
    return count

def rotated_minimum(arr):
    low = 0
    length = arr_len(arr)
    high = length - 1

    if arr[low] <= arr[high]:
        return arr[high]
    
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] > arr[mid + 1]:
            return arr[mid]
        
        if arr[mid - 1] > arr[mid]:
            return arr[mid - 1]
        
        if arr[mid] >= arr[low]:
            low = mid + 1

        else:
            high = mid - 1

    return -1

number = [4,5,6,7,1,2,3]

print(rotated_minimum(number))