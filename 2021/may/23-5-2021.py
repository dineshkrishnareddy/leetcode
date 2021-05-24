"""
N-Queens
https://leetcode.com/problems/n-queens/
"""


class Solution:
    def __init__(self, ans=None):
        self.ans = []

    def Valid(self, queen, n: int, row: int, col: int) -> bool:
        for i in range(n):
            if queen[i][col] == 'Q':
                return False
        for i in range(col, -1, -1):
            if queen[row][i] == 'Q':
                return False
        for (i, j) in zip(range(row, -1, -1), range(col, -1, -1)):
            if queen[i][j] == 'Q':
                return False
        for (i, j) in zip(range(row, n), range(col, -1, -1)):
            if queen[i][j] == 'Q':
                return False
        return True

    def SolveNQueens(self, queen, n: int, col: int) -> None:
        if col >= n:
            self.ans.append(["".join(queen[i]) for i in range(n)])
            return None
        for row in range(n):
            if self.Valid(queen, n, row, col):
                queen[row][col] = 'Q'
                self.SolveNQueens(queen, n, col + 1)
                queen[row][col] = '.'
        return None

    def solveNQueens(self, n: int):
        queen = [['.' for i in range(n)] for i in range(n)]

        self.SolveNQueens(queen, n, 0)
        return self.ans


print(Solution().solveNQueens(3))
