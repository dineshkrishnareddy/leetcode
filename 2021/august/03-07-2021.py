"""
90. Subsets II
https://leetcode.com/problems/subsets-ii/
"""


class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        n = len(nums)
        ans = []

        def dfs(idx, path):
            ans.append(path[:])

            for i in range(idx, n):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                dfs(i+1, path+[nums[i]])

        dfs(0, [])
        return ans


print(Solution().subsetsWithDup([1,2,2]))
