"""
Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""


class Solution:
    def letterCombinations(self, digits: str):
        if len(digits) == 0:
            return []

        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        results = []

        def backtracking(index, vals):
            if len(vals) == len(digits):
                results.append(''.join(vals))
                return

            possible_letters = letters[digits[index]]
            for letter in possible_letters:
                vals.append(letter)
                backtracking(index + 1, vals)
                vals.pop()

        backtracking(0, [])
        return results


print(Solution().letterCombinations('23'))
