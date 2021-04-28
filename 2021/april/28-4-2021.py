"""
Unique Paths II
https://leetcode.com/problems/unique-paths-ii/
"""


class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0

        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        obstacleGrid[0][0] = 1

        for i in range(1, rows):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i - 1][0] == 1)

        for i in range(1, cols):
            obstacleGrid[0][i] = int(obstacleGrid[0][i] == 0 and obstacleGrid[0][i - 1] == 1)

        for i in range(1, rows):
            for j in range(1, cols):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
                else:
                    obstacleGrid[i][j] = 0
        return obstacleGrid[rows - 1][cols - 1]

    def uniquePathsWithObstacles1(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0

        result = 0
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        directions = [[1, 0], [0, 1]]

        def traverse(x, y):
            nonlocal result
            if x >= rows or y >= cols:
                return
            if obstacleGrid[x][y] == 1:
                return
            if x == rows - 1 and y == cols - 1:
                result += 1
                return

            for direction in directions:
                x1 = x + direction[0]
                y1 = y + direction[1]
                traverse(x1, y1)

        traverse(0, 0)
        return result
