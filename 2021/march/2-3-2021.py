"""
Set Mismatch
https://leetcode.com/problems/set-mismatch/solution/
"""


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        length = len(nums)

        return [sum(nums) - sum(set(nums)), (length * (length + 1) // 2) - sum(set(nums))]
