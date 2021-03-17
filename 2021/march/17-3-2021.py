"""
Generate Random Point in a Circle
https://leetcode.com/problems/generate-random-point-in-a-circle/
"""
import random
import math


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.RAD = radius
        self.XC = x_center
        self.YC = y_center

    def randPoint(self) -> List[float]:
        ang = random.uniform(0, 1) * 2 * math.pi
        hyp = sqrt(random.uniform(0, 1)) * self.RAD
        adj = cos(ang) * hyp
        opp = sin(ang) * hyp
        return [self.XC + adj, self.YC + opp]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
