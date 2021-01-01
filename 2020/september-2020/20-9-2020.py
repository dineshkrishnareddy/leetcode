"""
Unique Paths III
https://leetcode.com/problems/unique-paths-iii/
"""


class Solution:
    def __init__(self):
        self.result = 0

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        total_zeros = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 0:
                    total_zeros += 1

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    self.dfs(grid, x, y, total_zeros)
        return self.result

    def dfs(self, grid, x, y, total_zeros):
        if x < 0 or y < 0 or x > len(grid) - 1 or y > len(grid[0]) - 1 or grid[x][y] == -1 or (
                grid[x][y] == 2 and total_zeros != 0):
            return

        if grid[x][y] == 2 and total_zeros == 0:
            self.result += 1
        if grid[x][y] == 0:
            total_zeros -= 1

        temp, grid[x][y] = grid[x][y], -1

        self.dfs(grid, x + 1, y, total_zeros)
        self.dfs(grid, x - 1, y, total_zeros)
        self.dfs(grid, x, y + 1, total_zeros)
        self.dfs(grid, x, y - 1, total_zeros)

        grid[x][y] = temp

