"""
Remove Duplicates from Sorted Array II
"""


class Solution:
    def removeDuplicates(self, nums) -> int:
        length = len(nums)
        if length < 2:
            return length
        at_most = 2
        p1, p2 = 0, 0
        while p2 < length:
            count = 0
            curr = nums[p2]
            while p2 < length and count < at_most and curr == nums[p2]:
                nums[p1] = nums[p2]
                p1 += 1
                p2 += 1
                count += 1
            while p2 < length and curr == nums[p2]:
                p2 += 1
        return len(nums[:p1])


nums = [1, 1, 1, 1]
print(Solution().removeDuplicates(nums))
nums = [1, 1, 1, 2, 2, 3]
print(Solution().removeDuplicates(nums))
nums = [0,0,1,1,1,1,2,3,3]
print(Solution().removeDuplicates(nums))
