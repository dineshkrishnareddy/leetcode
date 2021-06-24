"""
576. Out of Boundary Paths
https://leetcode.com/problems/out-of-boundary-paths/
"""
from functools import lru_cache


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        @lru_cache
        def backtrack(row, col, move):
            if (row < 0 or row >= m) or (col < 0 or col >= n):
                return 1
            if move == 0:
                return 0
            add = 0
            for d in directions:
                add += backtrack(row+d[0], col+d[1], move-1)
            return add % 1000000007
        return backtrack(startRow, startColumn, maxMove)

class Solution1:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        # define the dp array
        dp = [[[-1] * (maxMove + 1) for _ in range(n + 1)] for _ in range(m + 1)]

        def solve(i, j, maxMove):
            if maxMove < 0:
                return 0
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1

            # if the dp array at this position contains some value(not -1) then it means it has been computed earlier
            # so we don't need to compute again, hence return whatever value is present in dp.
            if dp[i][j][maxMove] != -1:
                return dp[i][j][maxMove]

            # otherwise compute the value
            a = solve(i - 1, j, maxMove - 1)
            b = solve(i + 1, j, maxMove - 1)
            c = solve(i, j - 1, maxMove - 1)
            d = solve(i, j + 1, maxMove - 1)

            # store the computed value in dp array so that we do not need to compute it again when the same input occurs again.
            dp[i][j][maxMove] = a + b + c + d
            return dp[i][j][maxMove]

        return solve(startRow, startColumn, maxMove) % 1000000007

# print(Solution().findPaths(2,2,2,0,0))
# print(Solution().findPaths(1,3,3,0,1))
# print(Solution().findPaths(7, 7, 11, 0, 4))
print(Solution().findPaths(8, 50, 23, 5, 26))
