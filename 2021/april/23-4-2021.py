"""
Count Binary Substrings
https://leetcode.com/problems/count-binary-substrings/
"""


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        result, prev, curr = 0, 0, 1
        for i in range(1, len(s)):
            if s[i - 1] != s[i]:
                result += min(prev, curr)
                prev, curr = curr, 1
            else:
                curr += 1
        return result + min(prev, curr)

    def countBinarySubstrings1(self, s: str) -> int:
        length = len(s)
        result = 0
        for i in range(length):
            j = i
            count = 0
            curr = s[i]
            while j < length and curr == s[j]:
                j += 1
                count += 1
            curr = '1' if curr == '0' else '0'
            while count and j < length and curr == s[j]:
                j += 1
                count -= 1
            if not count:
                result += 1
        return result
