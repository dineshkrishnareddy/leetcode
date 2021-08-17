"""
303. Range Sum Query - Immutable
https://leetcode.com/problems/range-sum-query-immutable/
"""


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        length = len(nums)
        self.prefix_sums = [0] * (length + 1)
        for j in range(1, length + 1):
            self.prefix_sums[j] = self.prefix_sums[j-1] + nums[j-1]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sums[right + 1] - self.prefix_sums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
