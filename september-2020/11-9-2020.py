"""

"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return 0
        # result = nums[0]
        # for x in range(length):
        #     curr = 1
        #     for y in range(x, length):
        #         curr *= nums[y]
        #         result = max(result, curr)
        # return result
        curr_max = nums[0]
        curr_min = nums[0]
        result = nums[0]
        for x in nums[1:]:
            temp = curr_max
            curr_max = max(max(curr_max*x, curr_min*x), x)
            curr_min = min(min(temp*x, curr_min*x), x)
            result = max(curr_max, result)
        return result
