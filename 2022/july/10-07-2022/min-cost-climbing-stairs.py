class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp, length = {}, len(cost)

        def getResult(index):
            if index >= length:
                return 0
            if index in dp:
                return dp[index]

            dp[index] = cost[index] + min(getResult(index + 1), getResult(index + 2))
            return dp[index]

        getResult(0)
        return min(dp[0], dp[1])
