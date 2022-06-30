class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        # with median

        # md = nums[n//2]                          # median
        # return sum([abs(e-md) for e in nums])    # return sum of abs of diff

        # with sum of diff of last and first element
        return sum([nums[-(i + 1)] - nums[i] for i in range(n // 2)])
