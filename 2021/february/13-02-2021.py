"""
Shortest Path in Binary Matrix
https://leetcode.com/problems/shortest-path-in-binary-matrix/
"""


class Solution:
    def shortestPathBinaryMatrix(self, grid):
        N = len(grid)
        neibs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        queue = deque([(1, 0, 0)]) if grid[0][0] == 0 else deque()
        visited = set()

        while queue:
            dist, x, y = queue.popleft()
            if (x, y) == (N - 1, N - 1): return dist
            for dx, dy in neibs:
                if 0 <= x + dx < N and 0 <= y + dy < N and grid[x + dx][y + dy] == 0 and (
                x + dx, y + dy) not in visited:
                    visited.add((x + dx, y + dy))
                    queue.append((dist + 1, x + dx, y + dy))

        return -1

    def shortestPathBinaryMatrix1(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0]) if rows else 0

        if (not rows and not cols) or (grid[0][0] != 0 or grid[rows - 1][cols - 1] != 0):
            return -1

        def bfs(row, col, steps, result):
            if (row < 0 or col < 0 or row >= rows or col >= cols) or grid[row][col] != 0:
                return result

            if row == rows - 1 and col == cols - 1:
                result = min(result, steps)

            grid[row][col] = -1
            result = bfs(row - 1, col, steps + 1, result)
            result = bfs(row, col - 1, steps + 1, result)
            result = bfs(row + 1, col, steps + 1, result)
            result = bfs(row, col + 1, steps + 1, result)
            result = bfs(row - 1, col - 1, steps + 1, result)
            result = bfs(row - 1, col + 1, steps + 1, result)
            result = bfs(row + 1, col - 1, steps + 1, result)
            result = bfs(row + 1, col + 1, steps + 1, result)
            grid[row][col] = 0
            return result

        result = bfs(0, 0, 1, float('inf'))
        return result if result != float('inf') else -1
