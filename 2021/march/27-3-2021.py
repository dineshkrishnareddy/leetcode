"""
Palindromic Substrings
https://leetcode.com/problems/palindromic-substrings/
"""


class Solution:
    def countSubstrings(self, s):
        length = len(s)
        index = 0
        result = 0
        while index < length:
            result += 1
            left, right = index-1, index+1
            while left >= 0 and right < length and s[left] == s[right]:
                result += 1
                left -= 1
                right += 1
            if index < length-1 and s[index] == s[index+1]:
                result += 1
                left, right = index - 1, index + 2
                while left >= 0 and right < length and s[left] == s[right]:
                    result += 1
                    left -= 1
                    right += 1
            index += 1
        return result


print(Solution().countSubstrings(s='aaa'))
