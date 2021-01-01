"""
Remove Covered Intervals
"""


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        length = len(intervals)
        exclude = []
        curr = 0
        while curr < length:
            compare = curr+1
            while compare < length:
                if intervals[curr][0] <= intervals[compare][0] <= intervals[compare][1] <= intervals[curr][1]:
                    exclude.append(intervals[compare])
                    compare += 1
                else:
                    break
            curr = compare
        return length - len(exclude)


Solution().removeCoveredIntervals([[1,2],[1,4],[3,4]])
