num = [1,2,3,4,5,6,7,8,9,10]

def array_len(arr):
    count = 0
    for _ in arr:
        count += 1
    return count

def array_binary_search(array, number):
    low = 0
    high = array_len(array) - 1
    count = 0
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == number:
            return [mid, count]
        elif number < array[mid]:
            high = mid - 1
        else:
            low = mid + 1
        count += 1
        
    return -1


result = array_binary_search(num, 0)

if result != -1:
    print('Number found at index', result[0])
    print(result[1])
else:
    print('number not found')
