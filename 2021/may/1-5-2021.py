"""
Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/
"""
import collections


class WordFilter1:

    def __init__(self, words):
        self.words = words

    def f(self, prefix: str, suffix: str) -> int:
        search_word = suffix + '#' + prefix
        result = -1
        for index, word in enumerate(self.words):
            if search_word in word + '#' + word:
                result = index
        print(result)
        return result


Trie = lambda: collections.defaultdict(Trie)
WEIGHT = False

class WordFilter(object):
    def __init__(self, words):
        self.trie = Trie()

        for weight, word in enumerate(words):
            word += '#'
            for i in range(len(word)):
                cur = self.trie
                cur[WEIGHT] = weight
                for j in range(i, 2 * len(word) - 1):
                    cur = cur[word[j % len(word)]]
                    cur[WEIGHT] = weight

    def f(self, prefix, suffix):
        cur = self.trie
        for letter in suffix + '#' + prefix:
            if letter not in cur:
                return -1
            cur = cur[letter]
        return cur[WEIGHT]


w = WordFilter(["cabaabaaaa","ccbcababac","bacaabccba","bcbbcbacaa","abcaccbcaa","accabaccaa","cabcbbbcca","ababccabcb","caccbbcbab","bccbacbcba"])
w.f("bccbacbcba","a")
w.f("ab","abcaccbcaa")
w.f("a","aa")
w.f("cabaaba","abaaaa")
w.f("cacc","accbbcbab")
w.f("ccbcab","bac")
w.f("bac","cba")
w.f("ac","accabaccaa")
w.f("bcbb","aa")
w.f("ccbca","cbcababac")
