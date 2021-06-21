"""
118. Pascal's Triangle
https://leetcode.com/problems/pascals-triangle/
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        result = [[1], [1, 1]]
        prev = [1, 1]
        for i in range(3, numRows + 1):
            tmp = [1] * i
            for j in range(1, i - 1):
                tmp[j] = prev[j - 1] + prev[j]
            prev = tmp
            result.append(tmp)
        return result
