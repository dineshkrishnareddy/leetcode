"""
Check Array Formation Through Concatenation
https://leetcode.com/problems/check-array-formation-through-concatenation/
"""


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        d = {x[0]: x for x in pieces}
        return list(chain(*[d.get(num, []) for num in arr])) == arr
