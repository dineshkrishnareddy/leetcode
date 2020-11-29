"""
Jump Game III
https://leetcode.com/problems/jump-game-iii/
"""


class Solution:
    def explore(self, arr, index):
        if 0 > index or index > len(arr) - 1:
            return False
        print(arr, index)
        if arr[index] == 0:
            return True
        if arr[index] == -1:
            return False

        arr[index], temp = -1, arr[index]
        left = self.explore(arr, index - temp)
        right = self.explore(arr, index + temp)
        arr[index] = temp
        return left or right

    def canReach(self, arr: List[int], start: int) -> bool:
        if len(arr) == 0:
            return False

        return self.explore(arr, start)
