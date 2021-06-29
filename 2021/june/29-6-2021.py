"""
1004. Max Consecutive Ones III
https://leetcode.com/problems/max-consecutive-ones-iii/
"""


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        p1, p2 = 0, 0
        length = len(nums)
        while p2 < length:
            if nums[p2] == 0:
                k -= 1
            if k < 0:
                if nums[p1] == 0:
                    k += 1
                p1 += 1
            p2 += 1
        return p2 - p1


print(Solution().longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
# print(Solution().longestOnes([0,0,1,1,1,0,0], 0))
