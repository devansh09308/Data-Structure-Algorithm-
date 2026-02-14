def nextGreaterElements(nums):
    n = len(nums)
    result = [-1] * n
    stack = []

    for i in range(2 * n):
        current_value = nums[i % n]

        while stack and nums[stack[-1]] < current_value:
            index = stack.pop()
            result[index] = current_value

        if i < n:
            stack.append(i)

    return result

# Example usage:
nums = [1, 2, 1]
print(nextGreaterElements(nums))  # Output: [2, -1, 2]