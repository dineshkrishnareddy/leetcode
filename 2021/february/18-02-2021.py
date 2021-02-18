"""
Arithmetic Slices
https://leetcode.com/problems/arithmetic-slices/
"""


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        count = comb = last_difference = 0
        for i in range(len(A) - 1):
            difference = A[i + 1] - A[i]
            if i != 0 and difference == last_difference:
                comb += 1
                count += comb
            else:
                comb = 0
            last_difference = difference
        return count
