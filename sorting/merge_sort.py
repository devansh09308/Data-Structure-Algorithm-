def array_len(array):
    count = 0
    for _ in array:
        count +=1
    return count

def merge_sort(arr):
    if array_len(arr) > 1:
        mid = array_len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < array_len(left_half) and j < array_len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < array_len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < array_len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

numbers = [64, 25, 12, 22, 11]
sorted_arr = merge_sort(numbers)

for i in range(array_len(sorted_arr)):
    print(sorted_arr[i])

