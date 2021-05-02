"""
Course Schedule III
https://leetcode.com/problems/course-schedule-iii/
"""
from heapq import heappop, heappush


class Solution:
    def scheduleCourse(self, courses) -> int:
        courses.sort(key=lambda x: x[1])
        total = 0
        heap = []
        for dur, end in courses:
            if total + dur <= end:
                total += dur
                heappush(heap, -dur)
            elif heap and -heap[0] > dur:
                total += dur + heappop(heap)
                heappush(heap, -dur)
            print(heap)
        return len(heap)


print(Solution().scheduleCourse([[7,17],[3,12],[10,20],[9,10],[5,20],[10,19],[4,18]]))
