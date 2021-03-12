"""
Coin Change
https://leetcode.com/problems/coin-change/solution/
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        # the amount of coins we need for 0 cents is 0
        dp[0] = 0

        for i in range(1, amount + 1):
            # dp[i] represents the min number of coins I need for i cents
            for j in range(len(coins)):
                # go through each coin and see if I should take it
                if coins[j] <= i:
                    # this will end up being the smallest of whatever was there before or the cost of taking
                    # the jth coin
                    dp[i] = min(dp[i], 1 + dp[i - coins[j]])

        # the final value wasn't able to be calculated
        return -1 if dp[amount] == float('inf') else dp[amount]
