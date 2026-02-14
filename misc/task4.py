
def koko(arr, target):
    low = 1
    high = max(arr)
    h = target

    while low < high:
        mid = (low + high) // 2

        hours = 0
        for i in arr:
            hours += (i + mid - 1) // mid

        if hours > h:
            low = mid + 1
        else:
            high = mid
        
    return low

piles = [5, 5, 5, 5]
h = 4

print(koko(piles, h))