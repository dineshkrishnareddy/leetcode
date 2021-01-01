"""
Decode String
"""


class Solution:
    def decodeString(self, s):
        stack, currNum, curString = [], 0, ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(currNum)
                curString = ''
                currNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num * curString
            elif c.isdigit():
                currNum = currNum * 10 + int(c)
            else:
                curString += c
        return curString


print(Solution().decodeString("3[a]2[bc]"))
