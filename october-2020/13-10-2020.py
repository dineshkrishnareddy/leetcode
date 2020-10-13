"""
Buddy Strings
https://leetcode.com/problems/buddy-strings/
"""


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        len_a = len(A)
        len_b = len(B)

        if len_a != len_b or len_a < 1:
            return False

        if A == B:
            unique = set()

            for char in A:
                unique.add(char)

            if len(unique) < len_a:
                return True
            return False
        diff = []
        for index in range(len_a):
            if A[index] != B[index]:
                diff.append(index)

        if len(diff) == 2 and A[diff[0]] == B[diff[1]] and A[diff[1]] == B[diff[0]]:
            return True
        return False


print(Solution().buddyStrings("aa", "aa"))
