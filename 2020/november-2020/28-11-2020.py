"""
Sliding Window Maximum
"""


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k < 1 or k > len(nums):
            return []

        output = []
        dq = []

        for i, n in enumerate(nums):
            if len(dq) and dq[0] < i - k + 1:
                dq.pop(0)

            while len(dq) and nums[dq[-1]] < n:
                dq.pop()

            dq.append(i)

            if i >= k - 1:
                output.append(nums[dq[0]])

        return output
