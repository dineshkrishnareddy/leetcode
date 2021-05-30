"""
Maximum Gap
https://leetcode.com/problems/maximum-gap/
"""


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        hi, low, ans = max(nums), min(nums), 0
        bsize = (hi - low) // (len(nums) - 1) or 1
        buckets = [[] for _ in range(((hi - low) // bsize) + 1)]
        for n in nums:
            buckets[(n - low) // bsize].append(n)
        curr_hi = 0
        for b in buckets:
            if len(b) == 0:
                continue
            prev_hi, curr_low = curr_hi or b[0], b[0]
            for n in b:
                curr_hi, curr_low = max(curr_hi, n), min(curr_low, n)
            ans = max(ans, curr_low - prev_hi)
        return ans
