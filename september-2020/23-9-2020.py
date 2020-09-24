"""
Gas Station
https://leetcode.com/problems/gas-station/
"""


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        g,c,tank, start = 0,0,0,0
        length = len(gas)
        for x in range(length):
            g += gas[x]
            c += cost[x]
            tank += gas[x] - cost[x]
            if tank < 0:
                tank = 0
                start = x+1
        if g < c:
            return -1
        return start
