"""
Longest Substring with At Least K Repeating Characters
https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
"""


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        length = len(s)

        if length == 0 or length < k:
            return 0
        if k <= 1:
            return length

        counts = Counter(s)

        l = 0
        while l < length and counts[s[l]] >= k:
            l += 1
        if l >= length - 1:
            return l

        l1 = self.longestSubstring(s[:l], k)
        while l < length and counts[s[l]] < k:
            l += 1
        l2 = self.longestSubstring(s[l:], k) if l < length else 0
        return max(l1, l2)
