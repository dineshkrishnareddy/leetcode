"""
816. Ambiguous Coordinates
https://leetcode.com/problems/ambiguous-coordinates/
"""


class Solution:
    def ambiguousCoordinates(self, S: str):
        ans, xPoss = [], []
        def process(st: str, xy: int):
            if xy:
                for x in xPoss:
                    ans.append("(" + x + ", " + st + ")")
            else: xPoss.append(st)
        def parse(st: str, xy: int):
            if len(st) == 1 or st[0] != "0":
                process(st, xy)
            if len(st) > 1 and st[-1] != "0":
                process(st[:1] + "." + st[1:], xy)
            if len(st) > 2 and st[0] != "0" and st[-1] != "0":
                for i in range(2, len(st)):
                    process(st[:i] + "." + st[i:], xy)
        for i in range(2, len(S)-1):
            strs, xPoss = [S[1:i], S[i:-1]], []
            for j in range(2):
                if xPoss or not j: parse(strs[j], j)
        return ans


print(Solution().ambiguousCoordinates('(00011)'))
