"""
https://leetcode.com/problems/delete-node-in-a-bst/
"""

class Solution:
    def get_count(self, matrixA, matrixB):
        rows = len(matrixA)
        columns = len(matrixA[0])
        count = 0
        for x in range(rows):
            for y in range(columns):
                temp = 0
                for i in range(y, rows):
                    for j in range(x, columns):
                        if matrixA[i][j] == 1 and matrixB[i - y][j - x] == 1:
                            temp += 1
                count = max(count, temp)
        return count


def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
    return max(self.get_count(A, B), self.get_count(B, A))
