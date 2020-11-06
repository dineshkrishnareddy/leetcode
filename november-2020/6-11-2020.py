"""
Minimum Cost to Move Chips to The Same Position
https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/
"""

import math


class Solution:
    def get_sum_divisor(self, nums, mid):
        result = 0
        for num in nums:
            result += math.ceil(num / mid)
        return result

    def smallestDivisor(self, nums, threshold: int) -> int:
        length = len(nums)
        if length == 0:
            return 0
        low, high = 1, max(nums)

        while low < high:
            mid = low + (high - low) // 2
            sum_divisor = self.get_sum_divisor(nums, mid)
            if sum_divisor <= threshold:
                high = mid
            else:
                low = mid + 1

        return low


a=[1,2,5,9]
b=6
print(Solution().smallestDivisor(a,b))
a=[2,3,5,7,11]
b=11
print(Solution().smallestDivisor(a,b))
a=[19]
b=5
print(Solution().smallestDivisor(a,b))
a=[962551,933661,905225,923035,990560]
b=10
print(Solution().smallestDivisor(a,b))