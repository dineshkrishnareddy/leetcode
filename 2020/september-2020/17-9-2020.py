"""
Robot Bounded In Circle
"""


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x,y = 0,0
        d = 0
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        for i in instructions:
            if i == 'G':
                x += directions[d%4][0]
                y += directions[d%4][1]
            elif i == 'L':
                d -= 1
            else:
                d += 1
        return (x, y) == (0, 0) or (d%4 != 0)
