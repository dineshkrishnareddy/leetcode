"""
N-Queens II
https://leetcode.com/problems/n-queens-ii/
"""


class Solution:
    def totalNQueens(self, n: int) -> int:
        self.ans = 0

        def place(i, vert, ldiag, rdiag):
            if i == n:
                self.ans += 1
            else:
                for j in range(n):
                    vmask, lmask, rmask = 1 << j, 1 << (i + j), 1 << (n - i - 1 + j)
                    if vert & vmask or ldiag & lmask or rdiag & rmask: continue
                    place(i + 1, vert | vmask, ldiag | lmask, rdiag | rmask)

        place(0, 0, 0, 0)
        return self.ans


print(Solution().totalNQueens(3))
