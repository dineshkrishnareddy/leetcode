"""
363. Max Sum of Rectangle No Larger Than K
https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/
"""


class Solution1:
    def kadane(self, arr, start, finish, n):
        # initialize sum, maxSum and
        add = 0
        maxSum = float('-inf')

        # Just some initial value to check
        # for all negative values case
        finish[0] = -1

        # local variable
        local_start = 0

        for i in range(n):
            add += arr[i]
            if add < 0:
                add = 0
                local_start = i + 1
            elif add > maxSum:
                maxSum = add
                start[0] = local_start
                finish[0] = i

        # There is at-least one
        # non-negative number
        if finish[0] != -1:
            return maxSum

        # Special Case: When all numbers
        # in arr[] are negative
        maxSum = arr[0]
        start[0] = finish[0] = 0

        # Find the maximum element in array
        for i in range(1, n):
            if arr[i] > maxSum:
                maxSum = arr[i]
                start[0] = finish[0] = i
        return maxSum

    def maxSumSubmatrix(self, M, k: int) -> int:
        row, col = len(M), len(M[0])
        maxSum = float('-inf')

        start = [0]
        finish = [0]

        for left in range(col):
            temp = [0] * row

            for right in range(left, col):
                for i in range(row):
                    temp[i] += M[i][right]

                add = self.kadane(temp, start, finish, row)

                print(add, left, right, temp)
                if add > maxSum and add <= k:
                    maxSum = add
        return maxSum


# print(Solution().maxSumSubmatrix([[5,-4,-3,4],[-3,-4,4,5],[5,1,5,-4]], 10))
"""
[
[5,-4,-3,4],
[-3,-4,4,5],
[5,1,5,-4]
]
"""

from sortedcontainers import SortedList
import math

class Solution:
    def maxSumSubmatrix(self, matrix, k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = -math.inf
        for r1 in range(m):
            arr = [0] * n  # arr[i] is sum(matrix[r1][c]...matrix[r2][c])
            for r2 in range(r1, m):
                for c in range(n): arr[c] += matrix[r2][c]
                tmp = self.maxSumSubAarray(arr, n, k)
                print(tmp, arr)
                ans = max(ans, tmp)
        return ans

    def maxSumSubAarray(self, arr, n, k):
        right = 0  # PrefixSum so far
        seen = SortedList([0])
        ans = -math.inf
        for i in range(n):
            right += arr[i]
            left = self.ceiling(seen, right - k)  # right - left <= k -> left >= right - k
            if left != None:
                ans = max(ans, right - left)
            seen.add(right)
        return ans

    def ceiling(self, sortedList, key):  # O(logN)
        idx = sortedList.bisect_left(key)
        if idx < len(sortedList): return sortedList[idx]
        return None


print(Solution().maxSumSubmatrix([[5,-4,-3,4],[-3,-4,4,5],[5,1,5,-4]], 10))
