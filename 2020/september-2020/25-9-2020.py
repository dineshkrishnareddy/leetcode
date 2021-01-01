"""
Largest Number
https://leetcode.com/problems/largest-number/
"""


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def largest(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0

        return str(int("".join(sorted(map(str, nums), key=cmp_to_key(lambda a, b: largest(a, b))))))
