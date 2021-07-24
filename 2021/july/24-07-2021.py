"""
126. Word Ladder II
https://leetcode.com/problems/word-ladder-ii/
"""


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wildcard_dict = collections.defaultdict(list)
        for word in wordList + [beginWord]:
            for i in range(len(word)):
                w = word[:i] + '*' + word[i + 1:]
                wildcard_dict[w].append(word)

        queue = collections.deque([("", []), (beginWord, [beginWord])])
        visited = set()
        result = []
        tempVisited = set()
        while queue:
            word, path = queue.pop()
            if not word:
                visited = visited.union(tempVisited)
                tempVisited = set()
                if len(queue):
                    queue.appendleft(("", []))
                continue
            if word == endWord:
                result.append(path[:])
                continue
            for i in range(len(word)):
                wild = word[:i] + '*' + word[i + 1:]
                for w in wildcard_dict[wild]:
                    if w not in visited:
                        tempVisited.add(w)
                        path.append(w)
                        queue.appendleft((w, path[:]))
                        path.pop()

        return result
