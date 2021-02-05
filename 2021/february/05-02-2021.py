"""
Simplify Path
https://leetcode.com/problems/simplify-path/
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for elem in path.split("/"):
            if stack and elem == "..":
                stack.pop()
            elif elem not in [".", "", ".."]:
                stack.append(elem)

        return "/" + "/".join(stack)
