class Solution:
    def uniquePaths(self, m, n):
        d = [[1 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == 1 or j == 1: continue
                d[i][j] = d[i - 1][j] + d[i][j - 1]

        return d[-1][-1]
