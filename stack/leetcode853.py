def merge_sort(position):
    if len(position) <= 1:
        return position

    mid = len(position) // 2
    left = merge_sort(position[:mid])
    right = merge_sort(position[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][0] > right[j][0]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def carFleet(target, position, speed):
    zipped = []
    n = len(position)

    for i in range(n):
        zipped.append((position[i], speed[i]))

    descending = merge_sort(zipped)

    last_time = fleet = 0

    for pos, sp in descending:
        time = (target - pos) / sp
        if time > last_time:
            fleet += 1
            last_time = time
    
    return fleet


target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]


print(carFleet(target, position, speed))
