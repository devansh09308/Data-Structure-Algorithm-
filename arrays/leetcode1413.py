# 1413. Minimum Value to Get Positive Step by Step Sum
def startValue(nums):
    prefixSum = 0
    minSum = 0

    for num in nums:
        prefixSum += num
        minSum = min(prefixSum, minSum)

    return 1 - minSum



nums = [-3,2,-3,4,2]
print(startValue(nums))