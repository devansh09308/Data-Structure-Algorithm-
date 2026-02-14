# 303. Range Sum Query - Immutable
def sums(nums, left, right):

    sum = [0] * len(nums)
    sum[0] = nums[0]

    for i in range(1, len(nums)):
        sum[i] = sum[i-1] + nums[i]

    if left == 0:
        return sum[right]
    else:
        return sum[right] - sum[left - 1]


nums = [-2, 0, 3, -5, 2, -1]

left = 0
right = 2

print(sums(nums, left, right))