"""
Remove All Adjacent Duplicates in String II
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
"""


class Solution:
    def numSubmatrixSumTarget(self, matrix, target: int) -> int:
        if not matrix:
            return 0

        def get_sum(arr, k):
            add = 0
            mapping = {0: 1}
            res = 0
            for i in arr:
                add += i
                if add - k in mapping:
                    res += mapping[add - k]
                mapping[add] = mapping.get(add, 0) + 1
            return res

        m = len(matrix)
        n = len(matrix[0])
        result = 0
        for i in range(m):
            nums = [0] * n
            for j in range(i, m):
                for k in range(n):
                    nums[k] += matrix[j][k]
                result += get_sum(nums, target)

        return result

print(Solution().numSubmatrixSumTarget([[1,-1],[-1,1]], 0))
