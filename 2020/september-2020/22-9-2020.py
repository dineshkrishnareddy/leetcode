"""
Majority Element II
https://leetcode.com/problems/majority-element-ii/
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        tmp = {}
        for num in nums:
            if num not in tmp:
                tmp[num] = 0
            tmp[num] += 1
        threshold = int(len(nums) / 3)
        result = []
        for key in tmp.keys():
            if tmp[key] > threshold:
                result.append(key)
        return result
