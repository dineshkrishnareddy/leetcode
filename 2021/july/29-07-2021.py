"""
542. 01 Matrix
https://leetcode.com/problems/01-matrix/
"""


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        mat = mat
        n = len(mat)
        m = len(mat[0])
        # init with +inf
        ans = [[float('inf')]*m for _ in range(n)]

        # from top left to bottom right, as we usually do
        for i in range(n):
            for j in range(m):
                if mat[i][j]: # if non-zero value
					# we actually only consider the top and the left neighbour
					# why? those are the ones we've already seen, and are thus optimized
                    if j > 0: ans[i][j] = min(ans[i][j], ans[i][j-1]+1)
                    if i > 0: ans[i][j] = min(ans[i][j], ans[i-1][j]+1)
                else: # if zero, that is the answer
                    ans[i][j] = 0

        # this time both ranges are reversed
        for i in reversed(range(n)):
            for j in reversed(range(m)):
                if mat[i][j]:
                    if j+1 < m: ans[i][j] = min(ans[i][j], ans[i][j+1]+1)
                    if i+1 < n: ans[i][j] = min(ans[i][j], ans[i+1][j]+1)
                else:
                    ans[i][j] = 0
        return ans
