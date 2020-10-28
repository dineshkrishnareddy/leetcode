"""
Summary Ranges
"""


class Solution:
    def summaryRanges(self, nums):
        length = len(nums)

        if length == 0:
            return []

        result = []
        curr_index = 0
        while True:
            start = nums[curr_index]
            while curr_index < length-1 and nums[curr_index] + 1 == nums[curr_index + 1]:
                curr_index += 1
            end = nums[curr_index]
            curr_index += 1
            if start != end:
                result.append('{start}->{end}'.format(start=start, end=end))
            else:
                result.append(str(end))
            if end == nums[-1]:
                break
        return result


print(Solution().summaryRanges([0,1,2,4,5,7]))
