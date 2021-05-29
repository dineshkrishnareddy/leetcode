"""
Maximum Erasure Value
https://leetcode.com/problems/maximum-erasure-value/
"""


class Solution:
    def maximumUniqueSubarray(self, nums) -> int:
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        start, end = 0, 1
        unique = {nums[0]: True}
        result = 0
        tmp = nums[0]

        while end < length:
            if nums[end] in unique:
                while nums[start] != nums[end]:
                    del unique[nums[start]]
                    tmp -= nums[start]
                    start += 1
                del unique[nums[start]]
                tmp -= nums[start]
                start += 1
            unique[nums[end]] = True
            tmp += nums[end]
            result = max(result, tmp)
            end += 1
        return result


print(Solution().maximumUniqueSubarray([5,2,1,2,5,2,1,2,5]))
