"""
795. Number of Subarrays with Bounded Maximum
https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/
"""


class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        length = len(nums)

        start, end = 0, 0
        result, count = 0, 0

        while start <= end and end < length:
            if left <= nums[end] <= right:
                result += (end - start + 1)
                count = (end - start + 1)
            elif nums[end] > right:
                start = end + 1
                count = 0
            else:
                result += count
            end += 1
        return result


print(Solution().numSubarrayBoundedMax([2,1,4,3], 2, 3))
print(Solution().numSubarrayBoundedMax([2,9,2,5,6], 2, 8))
