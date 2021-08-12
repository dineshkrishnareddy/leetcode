"""
49. Group Anagrams
https://leetcode.com/problems/group-anagrams/
"""
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        unique = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            unique[sorted_word].append(word)

        return unique.values()
