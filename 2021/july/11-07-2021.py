"""
295. Find Median from Data Stream
https://leetcode.com/problems/find-median-from-data-stream/
"""
from heapq import heappop, heappush, heappushpop


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.low, self.high = [], []

    def addNum(self, num: int) -> None:
        heappush(self.high, -heappushpop(self.low, -num))
        if len(self.low) < len(self.high):
            heappush(self.low, -heappop(self.high))

    def findMedian(self) -> float:
        return -self.low[0] if len(self.low) > len(self.high) else (-self.low[0] + self.high[0]) / 2
