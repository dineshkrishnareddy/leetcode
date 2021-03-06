"""
Minimum Number of Arrows to Burst Balloons
"""


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        points.sort(key=lambda x:x[1])
        print(points)
        end = points[0][1]
        result = 1
        for i in range(1, len(points)):
            if points[i][0] > end:
                result += 1
                end = points[i][1]
        return result
