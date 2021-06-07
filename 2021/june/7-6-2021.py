"""
746. Min Cost Climbing Stairs
https://leetcode.com/problems/min-cost-climbing-stairs/
"""


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        dp = [0] * (length + 1)

        for i in range(2, length + 1):
            step_1 = dp[i - 1] + cost[i - 1]
            step_2 = dp[i - 2] + cost[i - 2]
            dp[i] = min(step_1, step_2)

        return dp[-1]
