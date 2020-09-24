"""
Find the Difference
"""


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # s = sorted(s)
        # t = sorted(t)
        # for index in range(len(s)):
        #     if s[index] != t[index]:
        #         return t[index]
        # return t[-1]
        result = 0
        for i in s: result ^= ord(i)
        for i in t: result ^= ord(i)
        return chr(result)
