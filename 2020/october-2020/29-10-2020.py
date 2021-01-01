"""
Maximize Distance to Closest Person
https://leetcode.com/problems/maximize-distance-to-closest-person/
"""


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        length = len(seats)

        maxi = 2 * (10 ** 4)
        temp = [0] * length
        i = 0
        while i < length:
            if seats[i] == 1:
                maxi = 0
            else:
                maxi += 1
            temp[i] = maxi
            i += 1
        print(temp)
        result = 1
        maxi = 2 * (10 ** 4)
        i = length - 1
        while i >= 0:
            if seats[i] == 1:
                maxi = 0
            else:
                maxi += 1
            temp[i] = min(temp[i], maxi)
            i -= 1
        print(temp)
        return max(temp)
