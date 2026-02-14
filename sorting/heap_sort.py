def array_len(arr):
    c = 0
    for _ in arr:
        c += 1
    return c


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = array_len(arr)

    i = n // 2 - 1
    while i >= 0:
        heapify(arr, n, i)
        i -= 1

    end = n - 1
    while end >= 1:
        arr[0], arr[end] = arr[end], arr[0]
        heapify(arr, end, 0)
        end -= 1

    return arr


numbers = [20, 2, 7, 12, 15, 1, 6, 8]
n = array_len(numbers)
sorted_arr = heap_sort(numbers)

for i in range(array_len(sorted_arr)):
    print(sorted_arr[i])