"""
Kth Missing Positive Number
"""


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        nums = [i for i in range(1, 3000)]

        for num in arr:
            nums.pop(nums.index(num))

        return nums[k - 1]
