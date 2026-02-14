def peak(nums, target):
    low = 0 
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return True
        if nums[low] == nums[mid] == nums[high]:
            low +=1
            high -= 1

        elif nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        
        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1


    return False

nums = nums = [1,1,1,1,3,1]
target = 1
print(peak(nums, target))
