"""
Verifying an Alien Dictionary
https://leetcode.com/problems/verifying-an-alien-dictionary/
"""


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {}
        for index, val in enumerate(order):
            order_map[val] = index

        for i in range(len(words) - 1):

            for j in range(len(words[i])):
                if j >= len(words[i + 1]): return False

                if words[i][j] != words[i + 1][j]:
                    if order_map[words[i][j]] > order_map[words[i + 1][j]]:
                        return False
                    break

        return True

    def isAlienSorted1(self, words: List[str], order: str) -> bool:
        order_chars = {ele: ods for ods, ele in enumerate(order)}

        sorted_words = sorted(words, key=lambda x: [order_chars[c] for c in x])

        return words == sorted_words
