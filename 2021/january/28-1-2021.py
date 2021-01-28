"""
Smallest String With A Given Numeric Value
https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/
"""


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        z = (k - n) // 25
        unique = chr(k - z * 25 - n + 97) if n - z else ""
        return "a" * (n - z - 1) + unique + "z" * z
