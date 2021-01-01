"""
Flipping an Image
https://leetcode.com/problems/flipping-an-image/
"""


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        row_len = len(A)
        col_len = len(A[0])

        for row in range(row_len):
            start, end = 0, col_len - 1
            while start < end:
                A[row][start], A[row][end] = A[row][end], A[row][start]
                start += 1
                end -= 1
        for row in range(row_len):
            for col in range(col_len):
                A[row][col] = 0 if A[row][col] else 1

        return A

    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        for row in A:
            result.append(list(map(lambda x: 0 if x == 1 else 1, row[::-1])))
        return result
