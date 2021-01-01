"""
Valid Mountain Array
https://leetcode.com/problems/valid-mountain-array
"""


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        length = len(arr)
        if length < 3:
            return False

        p1 = 0
        p2 = 1
        while p2 < length and arr[p1] < arr[p2]:
            p1 += 1
            p2 += 1
        if p1 == 0 or p2 == length:
            return False
        while p2 < length and arr[p1] > arr[p2]:
            p1 += 1
            p2 += 1
        if p2 != length:
            return False
        return True


a = [2,1]
print(Solution().validMountainArray(a))
a = [3,5,5]
print(Solution().validMountainArray(a))
a = [3,5,6,3]
print(Solution().validMountainArray(a))
a = [1]
print(Solution().validMountainArray(a))
a = [1,2]
print(Solution().validMountainArray(a))
a = [1,2,1]
print(Solution().validMountainArray(a))
