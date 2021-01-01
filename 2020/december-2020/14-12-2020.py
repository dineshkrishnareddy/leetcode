"""
Palindrome Partitioning
https://leetcode.com/problems/palindrome-partitioning/
"""


class Solution:

    def __init__(self):
        self.res = []
        self.mem = {}

    def isPalindrome(self, s, i, j):
        return self.mem.setdefault((i, j), s[i:j] == s[i:j][::-1])

    def helper(self, s, n, i=0, partition=[]):
        if i == n:
            self.res.append(partition)
            return
        for j in range(i + 1, n + 1):
            if self.isPalindrome(s, i, j):
                self.helper(s, n, j, partition + [s[i:j]])

    def partition(self, s: str) -> List[List[str]]:
        self.helper(s, len(s))
        print(self.mem)
        return self.res

