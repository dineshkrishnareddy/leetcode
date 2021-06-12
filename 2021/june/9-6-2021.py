"""
1696. Jump Game VI
https://leetcode.com/problems/jump-game-vi
"""
import heapq

class Solution:
    def maxResult1(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        for i in range(n):
            maxV = float('-inf')
            for j in range(i - k, i):
                if j >= 0:
                    maxV = max(maxV, dp[j])
            if maxV == float("-inf"):
                maxV = 0
            dp[i] = nums[i] + maxV
        return dp[n - 1]

    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        queue = []
        val = 0
        for i in range(n):
            maxV = 0
            if queue:
                maxV, indx = queue[0]
                while indx + k < i:
                    maxV, indx = heapq.heappop(queue)
                heapq.heappush(queue, [maxV, indx])
            val = nums[i] + (-1) * maxV
            heapq.heappush(queue, [-1 * val, i])
        return val
