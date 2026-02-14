def arr_len(arr):
    count = 0 
    for _ in arr:
        count += 1
    return count

def func(arr,k):

    for i in arr:
        if i <= k:
            k += 1
        else:
            break
    return k
nums = [2,3,4,7,11]

k= 5

print(func(nums,k))