"""
Merge Sorted Array
"""


class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        write = len(nums1)
        while n and m:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[write - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[write - 1] = nums2[n - 1]
                n -= 1
            write -= 1
        while m:
            nums1[write - 1] = nums1[m - 1]
            m -= 1
            write -= 1
        while n:
            nums1[write - 1] = nums2[n - 1]
            n -= 1
            write -= 1


print(Solution().merge([2, 0], 1, [1], 1))
print(Solution().merge([1,2,3,0,0,0], 3, [2,5,6], 3))
