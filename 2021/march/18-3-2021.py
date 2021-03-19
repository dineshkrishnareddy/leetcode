"""
Wiggle Subsequence
https://leetcode.com/problems/wiggle-subsequence/
"""


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        res = 1
        last, asc = nums[0], None
        for i in range(1, len(nums)):
            n = nums[i]
            if n == last: continue
            if asc is None:  # fill first 2 valid elements
                res += 1
                asc = n > last
            elif asc and n < last or not asc and n > last:
                res += 1
                asc = n > last
            last = n
        return res
