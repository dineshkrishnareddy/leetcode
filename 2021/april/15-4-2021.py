"""
Fibonacci Number
https://leetcode.com/problems/fibonacci-number/
"""


class Solution:
    def fib(self, n: int) -> int:
        dp = {}
        dp[0] = 0
        dp[1] = 1

        def sol(n):
            if n in dp:
                return dp[n]

            return sol(n - 1) + sol(n - 2)

        return sol(n)
