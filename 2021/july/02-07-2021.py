"""
658. Find K Closest Elements
https://leetcode.com/problems/find-k-closest-elements/
"""
import heapq


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        pq = []
        for num in arr:
            diff = abs(x - num)
            heapq.heappush(pq, (diff, num))
        result = []
        while k:
            diff, num = heapq.heappop(pq)
            result.append(num)
            k -= 1
        return sorted(result)
