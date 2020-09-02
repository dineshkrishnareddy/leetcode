"""
https://leetcode.com/problems/largest-time-for-given-digits/solution/
"""

class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        length = len(A)
        result = ""
        for x in range(length):
            for y in range(length):
                for z in range(length):
                    if (x==y or y == z or x == z): continue
                    hh = str(A[x]) + str(A[y])
                    mm = str(A[z]) + str(A[6-x-y-z])
                    time = hh + ":" + mm
                    if hh <= '23' and mm <= '59' and time > result:
                        result = time
        return result
