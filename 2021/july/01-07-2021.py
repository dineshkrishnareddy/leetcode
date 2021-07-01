"""
89. Gray Code
https://leetcode.com/problems/gray-code/
"""


class Solution:
    def grayCode(self, n: int) -> List[int]:
        result=[]
        for i in range(2**n):
            i^=(i>>1)
            result.append(i)

        return result
