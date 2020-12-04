"""
The kth Factor of n
"""


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        big = []
        small = []

        for small_num in range(1, int(math.sqrt(n)) + 1):
            if n % small_num == 0:
                big_num = n // small_num
                if small_num != big_num:
                    big.append(big_num)
                small.append(small_num)

        factors = small + big[::-1]
        print(factors)
        return factors[k - 1] if len(factors) > k - 1 else -1
