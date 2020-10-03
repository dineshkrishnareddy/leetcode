"""
K-diff Pairs in an Array
"""


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        result = 0
        unique = {}
        for val in nums:
            unique[val] = unique.get(val, 0) + 1
        for val in unique:
            if k == 0:
                if unique[val] >= 2:
                    result += 1
            else:
                if val+k in unique:
                    result += 1
        return result


# nums = [3,1,4,1,5]
# k = 2
# Solution().findPairs(nums, k)
# nums = [1,3,1,5,4]
# k = 0
# Solution().findPairs(nums, k)
nums = [1,2,3,4,5]
k = 0
Solution().findPairs(nums, k)