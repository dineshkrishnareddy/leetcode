"""
Check If All 1's Are at Least Length K Places Away
https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/
"""


class Solution:
    def kLengthApart(self, nums, k: int) -> bool:
        length = len(nums)

        if length == 0:
            return True

        r1 = 0

        while r1 < length:
            if nums[r1] == 1:
                r2 = r1 + 1
                gap = 0
                while r2 < length:
                    gap += int(nums[r2] == 0)
                    if nums[r2] == 1:
                        if gap < k:
                            return False
                        else:
                            break
                    r2 += 1
            r1 += 1
        return True


print(Solution().kLengthApart([1,0,0,0,1,0,0,1], 2))
print(Solution().kLengthApart([1,0,0,0,1,0,1], 2))
