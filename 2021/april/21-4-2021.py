"""
Triangle
https://leetcode.com/problems/triangle/
"""


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @lru_cache(maxsize=None)
        def min_path(row, col):
            path = triangle[row][col]
            if row < len(triangle) - 1:
                path += min(min_path(row + 1, col), min_path(row + 1, col + 1))
            return path
        return min_path(0, 0)

    def minimumTotal1(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0

        minimum = float('inf')

        def traverse(path, x, y):
            nonlocal minimum
            # print(path, x,y, len(path), len(triangle))
            if len(path) == len(triangle):
                minimum = min(minimum, sum(path))
                return

            path.append(triangle[x][y])
            traverse(path, x+1, y)
            traverse(path, x+1, y+1)
            path.pop()

        traverse([], 0, 0)

        return minimum
