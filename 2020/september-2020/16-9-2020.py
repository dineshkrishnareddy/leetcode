"""
Maximum XOR of Two Numbers in an Array
"""


class Solution:
    def findMaximumXOR(self, nums):
        # length = len(nums)
        # maxi = 0
        # for i in range(length):
        #     for j in range(i+1, length):
        #         maxi = max(maxi, nums[i]^nums[j])
        # return maxi
        mask, result = 0, 0
        for i in range(32, -1, -1):
            mask = mask | 1 << i
            found = set([n & mask for n in nums])

            temp = result | 1 << i
            for f in found:
                if f ^ temp in found:
                    result = temp
        return result

print(Solution().findMaximumXOR([3,10,5,25,2,8]))
