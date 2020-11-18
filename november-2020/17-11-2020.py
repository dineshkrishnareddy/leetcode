"""
Mirror Reflection
https://leetcode.com/problems/mirror-reflection/
"""


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        m = n = 1

        while p * m != q * n:
            n += 1
            m = (q * n) // p

        if n % 2 == 0:
            return 2
        elif m % 2 == 0:
            return 0
        else:
            return 1
