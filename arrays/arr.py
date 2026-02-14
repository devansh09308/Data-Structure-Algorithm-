arr = []

arr.append(1)
arr.append(2)
arr.append(3)
arr.append(4)

# count = 0
# for i in range(len(arr)):
#     print(arr[i])
#     count +=1

# print(count)

# arr[3] = 5

# print(arr)

def array_length(arraylength):
    count = 0
    for _ in arraylength:
        count += 1
    return count

# def insert_arr(a, index, value):
#     new = []
#     i = 0

#     while i < index:
#         new.append(a[i])
#         i += 1

#     new.append(value)

#     while i < array_length(a):
#         new.append(a[i])
#         i += 1

#     return new


# value = 10
# index = 1

# new_arr = insert_arr(arr, index, value)
# print(new_arr)

def delete_element(a, index):
    i = 0
    new = []

    while i < array_length(a):
        if i != index:
            new.append(a[i])
        i += 1
    return new

print(arr)
del_arr = delete_element(arr, 3)
print(del_arr)