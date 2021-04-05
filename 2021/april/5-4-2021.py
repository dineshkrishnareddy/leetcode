"""
Global and Local Inversions
https://leetcode.com/problems/global-and-local-inversions/
"""


class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        return all([(i-1<=a<=i+1) for i,a in enumerate(A)])
