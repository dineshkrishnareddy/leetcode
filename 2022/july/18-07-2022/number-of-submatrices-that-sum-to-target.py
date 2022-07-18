from collections import defaultdict

class Solution:
    def numSubmatrixSumTarget(self, matrix, target: int) -> int:
        # find the rows and columns of the matrix
        n,m = len(matrix) , len(matrix[0])
        # find the prefix sum for each row
        for i in range(n):
            for j in range(1,m):
                matrix[i][j] += matrix[i][j-1]
        ans = 0
        # fix the left boundary of the column
        for start in range(m):
            # fix the right boundary of the column
            for end in range(start,m):
                # a dictionary to map data
                d = defaultdict(lambda:0)
                d[0] = 1
                summ = 0
                # now we do check at each row
                for i in range(n):
                    curr = matrix[i][end]
                    if start > 0:
                        curr -= matrix[i][start-1]
                    summ += curr
                    ans += d[summ - target]
                    d[summ] += 1
        return ans


print(Solution().numSubmatrixSumTarget([[0,1,0],[1,1,1],[0,1,0]], 0))
