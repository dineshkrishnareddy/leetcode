"""
Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length == 0:
            return 0
        chars = {}
        start, end = 0, 0
        result = 0
        while end < length:
            if s[end] not in chars:
                chars[s[end]] = 1
                result = max(result, end - start + 1)
                end += 1
            else:
                while s[end] in chars:
                    del chars[s[start]]
                    start += 1
        return result


print(Solution().lengthOfLongestSubstring("abcabcbb"))
