def arr_len(arr):
    count = 0

    for _ in arr:
        count += 1
    return count

def first_occ(arr, target):
    low = 0
    length = arr_len(arr)
    high = length - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            ans = mid
            high = mid - 1
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return ans

def last_occ(arr, target):
    low = 0
    length = arr_len(arr)
    high = length - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            ans = mid
            low = mid + 1
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return ans

number = [1,3,3,3,5,7,9]
target = 3

first = first_occ(number, target)
last = last_occ(number, target)

total = (last - first) + 1

if first != -1 and last != -1:
    print(total)
else:
    print('number not found')
