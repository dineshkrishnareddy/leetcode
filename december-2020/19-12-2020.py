"""
Decoded String at Index
https://leetcode.com/problems/decoded-string-at-index/
"""


class Solution(object):
    def decodeAtIndex(self, S, K):
        size = 0
        # Find size = length of decoded string
        for c in S:
            if c.isdigit():
                size *= int(c)
            else:
                size += 1

        for c in reversed(S):
            K %= size
            if K == 0 and c.isalpha():
                return c

            if c.isdigit():
                size /= int(c)
            else:
                size -= 1

#     def decodeAtIndex(self, S: str, K: int) -> str:
#         if len(S) == 0:
#             return ''

#         decode_str = ''

#         for s in S:
#             if s.isdigit():
#                 decode_str = decode_str * int(s)
#             else:
#                 decode_str += s

#         return decode_str[K-1]

S = "leet2code3"
K = 10
Solution().decodeAtIndex(S, K)
