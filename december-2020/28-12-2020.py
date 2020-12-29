"""
Pseudo-Palindromic Paths in a Binary Tree
https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import Counter


class Solution:
  def __init__(self):
    self.semi_palidrome_count = 0

  def check_for_semi_palidrome(self, values):
    counter = []
    for val in values:
      try:
        counter.pop(counter.index(val))
      except:
        counter.append(val)
    return len(counter) in [0, 1]

  def parse(self, root, values):
    values.append(root.val)
    if root.left is None and root.right is None:
      if self.check_for_semi_palidrome(values):
        self.semi_palidrome_count += 1

    if root.left is not None:
      self.parse(root.left, values)

    if root.right is not None:
      self.parse(root.right, values)
    values.pop()

  def pseudoPalindromicPaths(self, root: TreeNode) -> int:
    if root is None:
      return 0
    self.parse(root, [])
    return self.semi_palidrome_count