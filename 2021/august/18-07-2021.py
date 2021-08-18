"""
91. Decode Ways
https://leetcode.com/problems/decode-ways/
"""


import functools
"""
num(x) = num(x[1:]) + num(x[2:])
"""
class Solution:

    @functools.lru_cache(maxsize=None)
    def numHelper(self, index, s) -> int:
        if index == len(s):
            return 1
        if s[index] == '0':
            return 0
        if index == len(s) - 1:
            return 1

        answer = self.numHelper(index + 1, s)
        if int(s[index: index + 2]) <= 26:
            answer += self.numHelper(index + 2, s)

        return answer

    def numDecodings(self, s: str) -> int:
        return self.numHelper(0, s)
