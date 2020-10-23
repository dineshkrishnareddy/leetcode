"""
132 Pattern
https://leetcode.com/problems/132-pattern/
"""


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        length = len(nums)
        if length <= 2:
            return False
        aux = [nums[0]]
        for num in nums[1:]:
            aux.append(min(aux[-1], num))
        stack = []
        for index in range(length-1, -1, -1):
            while len(stack) and stack[-1] < nums[index]:
                if stack[-1] > aux[index]:
                    return True
                stack.pop()
            stack.append(nums[index])
        return False
