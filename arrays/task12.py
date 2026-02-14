def first(nums, target):
    low = 0
    high = len(nums) - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            ans = mid
            high = mid - 1   
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return ans

def last(nums, target):
    low = 0
    high = len(nums) - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            ans = mid
            low = mid + 1   
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return ans



nums = [5,7,7,8,8,10]
target = 8
arr1 = first(nums, target)
arr2 =  last(nums, target)

print([arr1, arr2])
