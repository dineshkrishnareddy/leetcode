"""
Construct Target Array With Multiple Sums
https://leetcode.com/problems/construct-target-array-with-multiple-sums/
"""
from heapq import heapify, heappushpop


class Solution:
    def isPossible(self, target) -> bool:
        if len(target) == 1: return target[0] == 1
        # - is used everywhere to convery python's default min-heap to max-heap
        heap, total = [-t for t in target], sum(target)
        heapify(heap)
        while -heap[0] != 1:
            largest, largest_2, restArrSum = -heap[0], -heap[1], total + heap[0]
            n = max(1, (largest - largest_2) // restArrSum)
            largest -= restArrSum * n
            heappushpop(heap, -largest)
            total = restArrSum + largest
            if largest < 1: return False
        return True


print(Solution().isPossible([9, 3, 5]))
# print(Solution().isPossible([8, 5]))
