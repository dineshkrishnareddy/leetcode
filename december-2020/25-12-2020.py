"""
Decode Ways
https://leetcode.com/problems/decode-ways/
"""


from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def dfs(s):
            if not s: return 1
            if s[0] == '0': return 0
            return dfs(s[1:]) + (dfs(s[2:]) if 10 <= int(s[:2]) <= 26 else 0)
        return dfs(s)


s = "12"
print(Solution().numDecodings(s))
s = "202"
print(Solution().numDecodings(s))
s = "2022"
print(Solution().numDecodings(s))
s = "2202"
print(Solution().numDecodings(s))
