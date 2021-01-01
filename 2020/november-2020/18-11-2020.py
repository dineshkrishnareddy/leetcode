"""
Merge Intervals
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        length = len(intervals)

        if length == 0:
            return []

        intervals.sort()
        result = []
        curr_index = 0
        while curr_index < length:
            start, end = intervals[curr_index]
            curr_index += 1
            while curr_index < length and end >= intervals[curr_index][0]:
                end = max(end, intervals[curr_index][1])
                curr_index += 1
            result.append([start, end])

        return result
