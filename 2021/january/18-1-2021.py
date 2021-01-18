"""
Max Number of K-Sum Pairs
https://leetcode.com/problems/max-number-of-k-sum-pairs/
"""


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        length = len(nums)

        if length == 0:
            return 0

        unique = {}
        result = 0

        for index, num in enumerate(nums):
            val = k - num
            if val not in unique:
                unique[val] = []
            unique[val].append(index)
        for index, num in enumerate(nums):
            for val in unique.get(num, []):
                if val != index:
                    unique[num].pop()
                    result += 1
                    break
        return result // 2

    def maxOperations(self, nums, k):
        ans = 0
        seen = defaultdict(int)
        for b in nums:
            a = k - b
            if seen[a] > 0:
                ans += 1
                seen[a] -= 1
            else:
                seen[b] += 1
        return ans
