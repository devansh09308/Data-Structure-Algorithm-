def largestRectangleArea(heights):
    stack = []
    max_area = 0
    heights.append(0)

    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            height = heights[stack.pop()]

            if stack:
                width = i - stack[-1] - 1
            else:
                width = i
            max_area = max(max_area, height * width)
        
        stack.append(i)

    return max_area

heights = [2,1,5,6,2,3]
print(largestRectangleArea(heights))