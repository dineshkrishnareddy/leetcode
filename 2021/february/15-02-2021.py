"""
The K Weakest Rows in a Matrix
https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
"""


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])

        if not rows and not cols:
            return []

        counts = []
        for row in range(rows):
            try:
                counts.append([mat[row].index(0), row])
            except:
                counts.append([cols, row])

        counts.sort(key=lambda x: (x[0], x[1]))

        return [x[1] for x in counts[:k]]
