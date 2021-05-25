"""
Evaluate Reverse Polish Notation
https://leetcode.com/problems/evaluate-reverse-polish-notation/
"""
from math import trunc


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in {"+", "-", "*", "/"}:
                stack.append(int(t))
            else:
                b, a = stack.pop(), stack.pop()
                if t == "+": stack.append(a + b)
                elif t == "-": stack.append(a - b)
                elif t == "*": stack.append(a * b)
                else: stack.append(trunc(a / b))
        return stack[0]


print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
