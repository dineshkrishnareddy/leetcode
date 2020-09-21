"""
Car Pooling
https://leetcode.com/problems/car-pooling/
"""


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda item: (item[1], item[2]))
        tmp = {}
        for trip in trips:
            for x in range(trip[1], trip[2]):
                if x not in tmp:
                    tmp[x] = 0
                tmp[x] += trip[0]
                if tmp[x] > capacity:
                    return False
        return True
