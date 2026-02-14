def ship(arr, target):
    low = max(arr)
    high = sum(arr)

    while low < high:
        mid = (low + high) // 2

        current = 0
        needed = 1

        for i in arr:
            if current + i > mid:
                needed += 1
                current = 0
            current += i

        if needed > target:
            low = mid + 1
        else:
            high = mid

    return low

weights = [1,2,3,4,5,6,7,8,9,10]
days = 5

print(ship(weights, days))