"""
Find and Replace Pattern
https://leetcode.com/problems/find-and-replace-pattern/
"""
from collections import defaultdict


class Solution:
    def findAndReplacePattern(self, words, pattern: str):
        result = []
        length_pattern = len(pattern)
        for word in words:
            if length_pattern == len(word):
                unique_pattern = defaultdict(str)
                unique_word = defaultdict(str)
                i = 0
                while i < length_pattern:
                    if pattern[i] in unique_pattern or word[i] in unique_word:
                        if unique_pattern[pattern[i]] != word[i] or unique_word[word[i]] != pattern[i]:
                            break
                    else:
                        unique_pattern[pattern[i]] = word[i]
                        unique_word[word[i]] = pattern[i]
                    i += 1
                if i == length_pattern:
                    result.append(word)
        return result


print(Solution().findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], "abb"))
