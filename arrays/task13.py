def search(nums):
    low = 0
    high = len(nums) - 1

    while low < high:
        mid = (low + high) // 2

        # Ensure mid is even for pairing check
        if mid % 2 == 1:
            mid -= 1

        if nums[mid] == nums[mid + 1]:
            low = mid + 2
        else:
            high = mid

    return nums[low]
            
        
 

nums = [1,1,2,3,3,4,4,8,8]

print(search(nums))