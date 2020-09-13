"""
https://leetcode.com/problems/combination-sum-iii/
"""


class Solution:
    def __init__(self):
        self.result = []

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k == 0:
            return []
        for x in range(1, 10):
            self.dfs(x, [x], k, n)
        return self.result

    def dfs(self, index, arr, k, n):
        if len(arr) == k:
            if sum(arr) == n:
                self.result.append(arr.copy())
            return
        for x in range(index + 1, 10):
            arr.append(x)
            self.dfs(x, arr, k, n)
            arr.pop()
