"""
https://leetcode.com/problems/pancake-sorting/
"""

class Solution:
    def pancakeSort(self, A):
        length = len(A)
        if length == 0:
            return []
        result = []
        curr_val = length
        while curr_val>1:
            index = A.index(curr_val)

            if index != curr_val:
                if index != 0:
                    A = A[:index + 1][::-1] + A[index + 1:]
                    result.append(index+1)

                A = A[:curr_val][::-1] + A[curr_val:]
                result.append(curr_val)
            curr_val -= 1

        return result

print(Solution().pancakeSort([3,2,4,1]))
