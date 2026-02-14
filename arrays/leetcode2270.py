# 2270. Number of Ways to Split Array
def split(nums):
    totalSum = sum(nums)
    leftsum = 0
    count = 0

    for i in range(len(nums) - 1):
        leftsum += nums[i]
        rightsum = totalSum - leftsum

        if leftsum >= rightsum:
            count += 1

    return count

nums = [10,4,-8,7]
print(split(nums))