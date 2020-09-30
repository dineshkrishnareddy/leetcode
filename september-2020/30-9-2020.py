"""
First Missing Positive
"""


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return 1
        for index in range(len(nums)):
            correct_pos = nums[index] - 1
            while 1 <= nums[index] <= length and nums[index] != nums[correct_pos]:
                nums[index], nums[correct_pos] = nums[correct_pos], nums[index]
                correct_pos = nums[index] - 1
        print(nums)
        for i in range(length):
            if i + 1 != nums[i]:
                return i + 1
        return length + 1
