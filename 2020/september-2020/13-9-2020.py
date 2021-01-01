"""
"""


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        curr, end = 0, len(intervals)
        result = []

        while curr < end and newInterval[0] > intervals[curr][1]:
            result.append(intervals[curr])
            curr += 1

        mix = newInterval
        while curr < end and newInterval[1] >= intervals[curr][0]:
            mix[0] = min(intervals[curr][0], mix[0])
            mix[1] = max(intervals[curr][1], mix[1])
            curr += 1
        result.append(mix)

        while curr < end:
            result.append(intervals[curr])
            curr += 1

        return result
