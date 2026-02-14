# manual function to find array length
def array_len(arr):
    c = 0
    for _ in arr:
        c += 1
    return c

# manual function to find maximum value in arr
def find_max(arr):
    m = arr[0]
    i = 1
    n = array_len(arr)
    while i < n:
        if arr[i] > m:
            m = arr[i]
        i += 1
    return m

def counting_sort(arr):

    n = array_len(arr)
    max_val = find_max(arr)

    # create count array manually (size = max_val + 1)
    count = []
    i = 0
    while i <= max_val:
        count += [0]     # manual append
        i += 1

    # counting each element
    i = 0
    while i < n:
        count[arr[i]] = count[arr[i]] + 1
        i += 1

    # write sorted values back to arr
    i = 0      # index in count array
    k = 0      # index in original array

    # go through count array
    while i <= max_val:
        while count[i] > 0:
            arr[k] = i
            count[i] = count[i] - 1
            k += 1
        i += 1

    return arr


# Example
numbers = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(numbers)

# print results manually
i = 0
while i < array_len(sorted_arr):
    print(sorted_arr[i])
    i += 1
