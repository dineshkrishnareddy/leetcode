"""
118. Pascal's Triangle
https://leetcode.com/problems/pascals-triangle/
"""


class Solution(object):
    def numMatchingSubseq(self, S, words):
        def subseq(word):
           it = iter(S)
           return all(x in it for x in word)

        return sum(subseq(word) for word in words)


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ans = 0
        heads = [[] for _ in range(26)]
        for word in words:
            it = iter(word)
            heads[ord(next(it)) - ord('a')].append(it)

        for letter in s:
            index = ord(letter) - ord('a')
            old_bucket = heads[index]
            heads[index] = []

            while old_bucket:
                it = old_bucket.pop()
                nxt = next(it, None)
                if nxt:
                    heads[ord(nxt) - ord('a')].append(it)
                else:
                    ans += 1
        return ans


print(Solution().numMatchingSubseq('abcde', ["a","bb","acd","ace"]))
