from functools import lru_cache

class Solution:
    def countVowelPermutation(self, n: int) -> int:

        # A mapper mapped characters to their next characters
        mapper = {
            "": ["a", "e", "i", "o", "u"],
            "a": "e",
            "e": ["a", "i"],
            "i": ["a", "e", "o", "u"],
            "o": ["i", "u"],
            "u": ["a"],
        }

        @lru_cache(None)
        def dp(n, c):

            # If n == 1, we have reach base case and thus, return 1
            if n == 1:
                return 1

            # Initialize the total to 0
            total = 0

            # Recursively solve sub-problems until n is reduced to 1
            for char in mapper[c]:
                total = (total + dp(n - 1, char)) % 1000000007

            return total

        # Add 1 to n since we started with empty string instead of recursively called dp on each vowel
        return dp(n + 1, "")
