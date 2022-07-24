class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        row, col = len(matrix)-1, 0

        while row >=0 and col <= len(matrix[0])-1:
            cell = matrix[row][col]
            if cell > target:
                row-= 1
            elif cell < target:
                col+= 1
            else: return True

        return False


print(Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 25))
