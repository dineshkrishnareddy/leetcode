"""
Search a 2D Matrix
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False

        rows = len(matrix)
        columns = len(matrix[0])
        start, end = 0, (rows * columns) - 1

        while start <= end:
            mid = start + ((end - start) // 2)
            row = mid // columns
            column = mid % columns
            # print(start, mid, end)
            # print(row, column)
            # print(matrix[row][column])
            # print('-----')
            if matrix[row][column] == target:
                return True
            if matrix[row][column] > target:
                end = mid - 1
            else:
                start = mid + 1

        return False
