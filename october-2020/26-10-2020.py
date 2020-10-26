"""
Champagne Tower
https://leetcode.com/problems/champagne-tower/
"""


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0 for _ in range(x)] for x in range(1, query_row + 2)]

        dp[0][0] = poured

        for row in range(query_row):
            for column in range(len(dp[row])):
                temp = (dp[row][column] - 1) / 2
                if temp > 0:
                    dp[row + 1][column] += temp
                    dp[row + 1][column + 1] += temp
        return dp[query_row][query_glass] if dp[query_row][query_glass] < 1 else 1
