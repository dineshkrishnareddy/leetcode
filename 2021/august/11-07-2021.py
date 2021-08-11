"""
926. Flip String to Monotone Increasing
https://leetcode.com/problems/flip-string-to-monotone-increasing/
"""


class Solution(object):
    def minFlipsMonoIncr(self, S):
        P = [0]
        for x in S:
            P.append(P[-1] + int(x))

        return min(P[j] + len(S)-j-(P[-1]-P[j])
                   for j in range(len(P)))


print(Solution().minFlipsMonoIncr('00110'))
