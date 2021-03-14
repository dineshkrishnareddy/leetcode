"""
Binary Trees With Factors
https://leetcode.com/problems/binary-trees-with-factors/
"""


class Solution(object):
    def numFactoredBinaryTrees(self, A):
        MOD = 10 ** 9 + 7
        N = len(A)
        A.sort()
        dp = [1] * N
        index = {x: i for i, x in enumerate(A)}
        for i, x in enumerate(A):
            for j in range(i):
                if x % A[j] == 0: #A[j] will be left child
                    right = x / A[j]
                    if right in index:
                        dp[i] += dp[j] * dp[index[right]]
                        dp[i] %= MOD

        return sum(dp) % MOD


# print(Solution().numFactoredBinaryTrees([2, 4]))
print(Solution().numFactoredBinaryTrees([2, 4, 5, 10]))
