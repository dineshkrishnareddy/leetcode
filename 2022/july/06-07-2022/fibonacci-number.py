class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0

        fib, prev = 1, 0
        for _ in range(n - 1):
            fib, prev = fib + prev, fib

        return fib
