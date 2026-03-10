def kokoBananas(piles, h):
    high = max(piles)
    low = 1

    while low < high:
        mid = (low + high) // 2
        hours = 0
        for pile in piles:
            hours += (pile + mid - 1) // mid

        if hours > h:
            low = mid + 1
        else:
            high = mid
        
    return low


piles = [3,6,7,11]
h = 8

print(kokoBananas(piles, h))