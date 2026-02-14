def array_len(array):
    count = 0
    for _ in array:
        count +=1
    return count

def insertion_sort(arr):
    i= 1
    len = array_len(arr)

    while i < len:
        key = arr[i]
        j = i - 1

        while j>=0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key

        i += 1
    return arr


numbers = [64, 25, 12, 22, 11]
sorted_arr = insertion_sort(numbers)

for i in range(array_len(sorted_arr)):
    print(sorted_arr[i])