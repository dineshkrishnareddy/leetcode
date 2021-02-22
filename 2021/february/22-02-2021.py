"""
Longest Word in Dictionary through Deleting
https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/
"""


class Solution:
    def is_substring(self, s1, s2):
        str1_len = len(s1)
        str2_len = len(s2)
        str1, str2 = 0, 0

        while str1 < str1_len and str2 < str2_len:
            if s1[str1] == s2[str2]:
                str2 += 1
            str1 += 1

        return str2 == str2_len

    def findLongestWord(self, s: str, d: List[str]) -> str:
        result = ''
        for item in d:
            if self.is_substring(s, item):
                if len(item) == len(result):
                    result = min(item, result)
                elif len(item) > len(result):
                    result = item
        return result
