"""
Search Suggestions System
https://leetcode.com/problems/search-suggestions-system/
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []
        self.word_count = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_product(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            if curr.word_count < 3:
                curr.words.append(word)
                curr.word_count += 1

    def search_product(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return []
            node = node.children[c]
        return node.words


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        t = Trie()

        products.sort()
        for p in products:
            t.add_product(p)

        return [t.search_product(searchWord[:i + 1]) for i in range(len(searchWord))]
