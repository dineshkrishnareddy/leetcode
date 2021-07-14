"""
791. Custom Sort String
https://leetcode.com/problems/custom-sort-string/
"""
from collections import Counter


class Solution:
    def customSortString(self, order: str, string: str) -> str:
        od = Counter(string)
        result = []
        for o in order:
            if o in od:
                result += [o] * od[o]
                del od[o]
        for key, val in od.items():
            result += [key] * val
        return ''.join(result)
