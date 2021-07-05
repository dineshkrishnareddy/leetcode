"""
566. Reshape the Matrix
https://leetcode.com/problems/reshape-the-matrix/
"""


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        if rows * cols != r * c:
            return mat

        result = [[0] * c for _ in range(r)]
        total = 0
        r1, c1 = 0, 0

        for row in range(rows):
            for col in range(cols):
                r1, c1 = divmod(total, c)
                result[r1][c1] = mat[row][col]
                total += 1
        return result
