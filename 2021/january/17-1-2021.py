"""
Count Sorted Vowel Strings
https://leetcode.com/problems/count-sorted-vowel-strings/
"""
import itertools


class Solution:
    def countVowelStrings(self, n: int) -> int:
        return len(list(itertools.combinations_with_replacement(range(5), n)))
