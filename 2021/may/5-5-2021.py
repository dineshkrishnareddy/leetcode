"""
Jump Game II
https://leetcode.com/problems/jump-game-ii/
"""


class Solution:
    def jump(self, nums: List[int]) -> int:
        curr_pos = -1
        next_pos = 0
        ans = 0
        length = len(nums) - 1
        i = 0
        while next_pos < length:
            if i > curr_pos:
                ans += 1
                curr_pos = next_pos
            next_pos = max(next_pos, nums[i] + i)
            i += 1
        return ans
