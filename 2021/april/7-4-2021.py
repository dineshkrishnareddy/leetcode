"""
Determine if String Halves Are Alike
https://leetcode.com/problems/determine-if-string-halves-are-alike/
"""


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        a, b = s[:len(s) // 2], s[len(s) // 2:]
        a_count = Counter(a)
        b_count = Counter(b)
        a_sum = sum([a_count[char] for char in ['a', 'e', 'i', 'o', 'u']])
        b_sum = sum([b_count[char] for char in ['a', 'e', 'i', 'o', 'u']])
        return a_sum == b_sum
