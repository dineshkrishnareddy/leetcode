"""
370. Range Addition
https://leetcode.com/problems/range-addition/
"""


class Solution:
    def getModifiedArray(self, length: int, updates):
        ans = [0] * length
        for si, ei, inc in updates:
            ans[si] += inc
            if ei + 1 < length: ans[ei + 1] -= inc
        for i in range(1, length): ans[i] += ans[i - 1]
        return ans


print(Solution().getModifiedArray(5, [[2, 4, 5]]))
