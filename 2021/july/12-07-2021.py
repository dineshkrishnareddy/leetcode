"""
205. Isomorphic Strings
https://leetcode.com/problems/isomorphic-strings/
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        length_s = len(s)
        length_t = len(t)

        unique_s = {}
        unique_t = {}

        if length_s != length_t:
            return False

        start = 0
        while start < length_s:
            if s[start] in unique_s:
                if unique_t.get(t[start]) != s[start]:
                    return False
            elif unique_t.get(t[start]) == None and unique_s.get(s[start]) == None:
                unique_t[t[start]] = s[start]
                unique_s[s[start]] = t[start]
            else:
                return False
            start += 1
        return True
