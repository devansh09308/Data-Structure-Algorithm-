def array_len(arr):
    c = 0
    for _ in arr:
        c += 1
    return c


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    j = low

    while j < high:
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1

    # place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

    return arr


numbers = [20, 2, 7, 12, 15, 1, 6, 8]
n = array_len(numbers)
sorted_arr = quick_sort(numbers, 0, n - 1)

for i in range(array_len(sorted_arr)):
    print(sorted_arr[i])
