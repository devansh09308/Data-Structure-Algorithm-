num = [1,2,3,4,5,6,7,8,9,10]

def array_len(arr):
    count = 0
    for _ in arr:
        count += 1
    return count

def array_search(array, number):
    repeat = 1
    for i in range(array_len(array)):
        if number == array[i]:
            return [i, repeat]
        repeat += 1  
    return  -1

result = array_search(num, 10)

if result != -1:
    print('Number found at index', result[0])
    print(result)
    print(result[1])
else:
    print('number not found')
