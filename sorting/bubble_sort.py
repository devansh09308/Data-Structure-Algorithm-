def array_len(array):
    count = 0
    for _ in array:
        count +=1
    return count

def bubble_sort(arr):
    i= 0
    len = array_len(arr)
    while i < len - 1:
        j = 0
        while j < len - i - 1:
            if arr[j] < arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j + 1]  = temp
            j += 1
        i += 1

    return arr

numbers = [64, 25, 12, 22, 11]
sorted_arr = bubble_sort(numbers)

for i in range(array_len(sorted_arr)):
    print(sorted_arr[i])
