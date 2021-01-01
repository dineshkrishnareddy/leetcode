"""
Teemo Attacking
https://leetcode.com/problems/teemo-attacking/
"""


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if len(timeSeries) == 0:
            return 0
        result = 0
        for x in range(len(timeSeries) - 1):
            result += min(duration, timeSeries[x + 1] - timeSeries[x])

        return result + duration
