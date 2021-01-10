"""
Create Sorted Array through Instructions
"""

from sortedcontainers import SortedList


class Solution:
    def createSortedArray(self, instructions):
        SList = SortedList()
        ans = 0
        for num in instructions:
            ans += min(SList.bisect_left(num), len(SList) - SList.bisect_right(num))
            ans %= (10**9 + 7)
            SList.add(num)

        return ans


class Solution:
    def createSortedArray(self, instructions) -> int:
        length = len(instructions)

        if length == 0:
            return 0
        result = 0
        sorted_arr = []
        for num in instructions:
            sorted_arr_len = len(sorted_arr)

            left = 0
            curr = 0
            while curr < sorted_arr_len and sorted_arr[curr] < num:
                left += 1
                curr += 1

            right = 0
            curr = sorted_arr_len-1
            while curr > -1 and sorted_arr[curr] > num:
                right += 1
                curr -= 1

            place_to_add = left if left <= right else sorted_arr_len - right
            sorted_arr = sorted_arr[:place_to_add] + [num] + sorted_arr[place_to_add:]
            result += min(left, right)
        return result


print(Solution().createSortedArray([1,5,6,2]))
print(Solution().createSortedArray([1,2,3,6,5,4]))
