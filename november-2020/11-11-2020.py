"""
Valid Square
https://leetcode.com/problems/valid-square/
"""


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def get_dist(p1, p2):
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

        p = [p1, p2, p3, p4]
        p.sort()

        return get_dist(p[0], p[3]) == get_dist(p[1], p[2]) and get_dist(p[0], p[1]) == get_dist(p[0], p[2]) \
               and get_dist(p[0], p[3])
