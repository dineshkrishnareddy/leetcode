"""
Flatten Nested List Iterator
https://leetcode.com/problems/flatten-nested-list-iterator/
"""


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:

    def __init__(self, nestedList):
        self.data = []
        self.flatten(nestedList)

    def flatten(self, lst):
        for el in lst:
            if el.isInteger():
                self.data.append(el.getInteger())
            else:
                self.flatten(el.getList())

    def hasNext(self) -> bool:
        return len(self.data)

    def next(self) -> int:
        return self.data.pop(0)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
