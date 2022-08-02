from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        index = defaultdict(int)
        heap = []
        n = len(matrix)
        for i in range(len(matrix)):
            heappush(heap, (matrix[i][index[i]],i))
            index[i] += 1
        while heap and k > 0:
            cur, i = heappop(heap)
            if index[i] < n:
                heappush(heap, (matrix[i][index[i]],i))
            index[i] += 1
            k -= 1
        return cur


print(Solution().kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))
