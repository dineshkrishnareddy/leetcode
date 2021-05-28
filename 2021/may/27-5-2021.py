"""
Maximum Product of Word Lengths
https://leetcode.com/problems/maximum-product-of-word-lengths/
"""


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def common(chars1, chars2):
            for c1, c2 in zip(chars1, chars2):
                if c1 and c2: return True
            return False
        chars, ans = [[False]*26 for i in range(len(words))], 0
        for i, word in enumerate(words):
            for ch in word:
                chars[i][ord(ch) - ord('a')] = True
            for j in range(i):
                if not common(chars[i], chars[j]):
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans
