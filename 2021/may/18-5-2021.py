"""
Find Duplicate File in System
https://leetcode.com/problems/find-duplicate-file-in-system/
"""


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hashmap = dict()
        for i in paths:
            x = i.split(' ')
            folder = x[0]
            files = x[1:]

            for f in files:
                y = f.split('(')
                txt = y[0]
                content = ''.join(y[1][: (len(y[1]) - 1)])

                if content in hashmap:
                    hashmap[content].append(folder + "/" + txt)
                else:
                    hashmap[content] = [(folder + "/" + txt)]

        ans = filter(lambda x: len(x) > 1, list(hashmap.values()))
        return list(ans)
