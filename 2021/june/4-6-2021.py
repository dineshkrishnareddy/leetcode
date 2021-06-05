"""
752. Open the Lock
https://leetcode.com/problems/open-the-lock/
"""

from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        set_deadends = set()
        visited = set()
        for deadend in deadends:
            set_deadends.add(deadend)
        if "0000" in set_deadends:
            return -1
        dq = deque()
        dq.append("0000")
        visited.add("0000")
        turns = 0
        while dq:
            len_dq = len(dq)
            for _ in range(len_dq):
                curr = dq.popleft()
                if curr == target:
                    return turns

                for i in range(4):
                    nxt1 = ""
                    nxt2 = ""
                    if curr[i] == '0':
                        nxt1 = curr[:i] + '9' + curr[i + 1:]
                        nxt2 = curr[:i] + '1' + curr[i + 1:]
                    elif curr[i] == '9':
                        nxt1 = curr[:i] + '0' + curr[i + 1:]
                        nxt2 = curr[:i] + '8' + curr[i + 1:]
                    else:
                        nxt1 = curr[:i] + chr(ord(curr[i]) + 1) + curr[i + 1:]
                        nxt2 = curr[:i] + chr(ord(curr[i]) - 1) + curr[i + 1:]

                    if nxt1 not in visited and nxt1 not in set_deadends:
                        visited.add(nxt1)
                        dq.append(nxt1)
                    if nxt2 not in visited and nxt2 not in set_deadends:
                        visited.add(nxt2)
                        dq.append(nxt2)
            turns += 1
        return -1
