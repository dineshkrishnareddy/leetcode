"""
378. Kth Smallest Element in a Sorted Matrix
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
"""


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        pq = []
        if matrix == []:
            return -1
        rows, cols = len(matrix), len(matrix[0])
        for row in range(len(matrix)):
            heapq.heappush(pq, [matrix[row][0], row, 0])
        result = -1
        while k:
            # print(pq, result)
            result,row, col = heapq.heappop(pq)
            col += 1
            if col < cols:
                heapq.heappush(pq, [matrix[row][col], row, col])
            k -= 1
        return result
