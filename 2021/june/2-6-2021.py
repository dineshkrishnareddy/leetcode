"""
97. Interleaving String
https://leetcode.com/problems/interleaving-string/
"""
import functools


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        end_s1 = len(s1)
        end_s2 = len(s2)
        end_s3 = len(s3)

        @functools.lru_cache(None)
        def find(curr_s1, curr_s2, curr_s3):
            if curr_s1 < end_s1 and s1[curr_s1] == s3[curr_s3] and curr_s2 < end_s2 and s2[curr_s2] == s3[
                curr_s3] and curr_s3 < end_s3:
                return find(curr_s1 + 1, curr_s2, curr_s3 + 1) or find(curr_s1, curr_s2 + 1, curr_s3 + 1)

            if curr_s1 < end_s1 and curr_s3 < end_s3 and s1[curr_s1] == s3[curr_s3]:
                return find(curr_s1 + 1, curr_s2, curr_s3 + 1)

            if curr_s2 < end_s2 and curr_s3 < end_s3 and s2[curr_s2] == s3[curr_s3]:
                return find(curr_s1, curr_s2 + 1, curr_s3 + 1)

            return True if curr_s3 == end_s3 else False

        if end_s3 != end_s1 + end_s2:
            return False
        return find(0, 0, 0)


# print(Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac"))
print(Solution().isInterleave('a', 'b', 'a'))
