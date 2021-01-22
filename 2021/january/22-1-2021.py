"""
Determine if Two Strings Are Close
https://leetcode.com/problems/determine-if-two-strings-are-close/
"""


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        def ans(word):
            dict1 = {}
            for i in word:
                if i not in dict1:
                    dict1[i] = 1
                else:
                    dict1[i] += 1
            return sorted(dict1.values())

        return ans(word1) == ans(word2) and set(word1) == set(word2)
