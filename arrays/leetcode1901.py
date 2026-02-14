def findPeakGrid(mat):
    m = len(mat)
    n = len(mat[0])

    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2

        max_row = 0
        for row in range(m):
            if mat[row][mid] > mat[max_row][mid]:
                max_row = row

        left_col = mat[max_row][mid - 1] if mid - 1 >= 0 else float('-inf')
        right_col = mat[max_row][mid + 1] if mid + 1 < n else float('-inf')
        mid_col = mat[max_row][mid]

        if mid_col >= left_col and mid_col >= right_col:
            return [max_row, mid]
        elif left_col > mid_col:
            right = mid - 1
        else:
            left = mid + 1
    return [-1, -1]


mat = [
    [10, 20, 15],
    [21, 30, 35],
    [7, 45, 32]
]

peak = findPeakGrid(mat)
print(peak)