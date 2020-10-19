"""
Minimum Domino Rotations For Equal Row
"""


class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        a_count = [0] * 7
        b_count = [0] * 7

        same = 0

        for i in range(len(A)):
            a_count[A[i]] += 1
            b_count[B[i]] += 1

            if A[i] == B[i]:
                same += 1

        for i in range(1, 7):
            if a_count[i] + b_count[i] - same == len(A):
                return len(A) - max(a_count[i], b_count[i])
        return -1
