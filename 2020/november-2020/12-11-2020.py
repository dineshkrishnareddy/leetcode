"""
Permutations II
https://leetcode.com/problems/permutations-ii/
"""


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(a, k):
            if k == n:
                res.append(a.copy())
                return

            for v in counter:
                if counter[v] > 0:
                    a.append(v)
                    counter[v] -= 1
                    backtrack(a, k + 1)
                    counter[v] += 1
                    a.pop()

        res, n, counter = [], len(nums), Counter(nums)
        backtrack([], 0)
        return res
