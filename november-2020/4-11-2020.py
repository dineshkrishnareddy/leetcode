"""
Consecutive Characters
https://leetcode.com/problems/consecutive-characters/
"""


class Solution:
    def maxPower(self, s: str) -> int:
        length = len(s)

        if length == 0:
            return 0

        start, end = 0, 0
        result = 0
        while end < length:
            while end < length and s[start] == s[end]:
                end += 1
            result = max(result, end - start)
            start = end
        return result
