"""
Letter Case Permutation
https://leetcode.com/problems/letter-case-permutation/
"""


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        length = len(S)
        result = []

        def dfs(index, curr_string):
            if len(curr_string) == length:
                result.append(curr_string)
                return

            if S[index].isalpha():
                dfs(index + 1, curr_string + S[index].lower())
                dfs(index + 1, curr_string + S[index].upper())
            else:
                dfs(index + 1, curr_string + S[index])

        dfs(0, '')
        return result
