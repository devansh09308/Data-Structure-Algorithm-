def arr_len(arr):
    count = 0
    for _ in arr:
        count += 1
    return count


def peak(arr):
    low = 0
    length = arr_len(arr)
    high = length - 1

    while low < high:
        mid = (low + high) // 2

        if arr[mid] <= arr[mid + 1]:
            low = mid + 1

        else: 
            high = mid

    return low

number = [4,5,0,3,2,4,5,6,5,4,3,2]

print(peak(number))
