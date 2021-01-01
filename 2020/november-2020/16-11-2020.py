"""
Longest Mountain in Array
https://leetcode.com/problems/longest-mountain-in-array/
"""


class Solution:
    def longestMountain(self, A) -> int:
        length = len(A)

        if length == 0:
            return 0
        curr = 0
        result = 0
        while curr < length-1:
            start = curr
            while curr + 1 < length and A[curr] < A[curr + 1]:
                curr += 1
            mid = curr
            while curr + 1 < length and A[curr] > A[curr + 1]:
                curr += 1
            end = curr
            if start != mid and mid != end:
                result = max(result, end - start + 1)
            elif start == end:
                curr += 1
        return result


print(Solution().longestMountain([2,1,4,7,3,2,5]))
print(Solution().longestMountain([2,2,2]))