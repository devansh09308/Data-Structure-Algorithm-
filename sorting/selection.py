def array_len(array):
    count = 0
    for _ in array:
        count +=1
    return count

def selection_sort(arr):
    i= 0
    len = array_len(arr)

    while i < len - 1:
        j = i + 1
        min_idx = i

        while j < len:
            if arr[j] < arr[min_idx]:
                min_idx = j
            j += 1
            
        if min_idx != i:
            temp = arr[i]
            arr[i] = arr[min_idx]
            arr[min_idx] = temp
    
        i += 1    

    return arr

numbers = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(numbers)

for i in range(array_len(sorted_arr)):
    print(sorted_arr[i])