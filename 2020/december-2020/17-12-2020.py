"""
4Sum II
"""


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        unique = {}
        result = 0

        for a in A:
            for b in B:
                sum1 = a + b
                if sum1 in unique:
                    unique[sum1] += 1
                else:
                    unique[sum1] = 1

        for c in C:
            for d in D:
                sum2 = -(c + d)
                if sum2 in unique:
                    result += unique[sum2]

        return result
