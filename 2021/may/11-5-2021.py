"""
Maximum Points You Can Obtain from Cards
https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
"""


class Solution:
    def maxScore(self, cp: List[int], k: int) -> int:
        ans = tot_sum = sum(cp[:k])
        for i in range(1, k + 1):
            tot_sum = tot_sum + cp[len(cp) - i] - cp[k - i]
            ans = max(ans, tot_sum)
        return ans
