"""
Subarray Product Less Than K
https://leetcode.com/problems/subarray-product-less-than-k
"""


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if len(nums) == 0 or k <= 1:
            return 0
        # result = 0
        # for i in range(len(nums)):
        #     curr_prod = 1
        #     for j in range(i, len(nums)):
        #         curr_prod *= nums[j]
        #         if curr_prod >= k:
        #             break
        #         result += 1
        # return result
        prod = 1
        result = 0
        left, right = 0, 0

        while right < len(nums):
            prod *= nums[right]

            while prod >= k and left < len(nums):
                prod /= nums[left]
                left += 1

            result += (right - left + 1)
            right += 1
        return result
