"""
Complement of Base 10 Integer
"""


class Solution:
    def bitwiseComplement(self, N: int) -> int:
        binary = bin(N)[2:]
        result = ''
        for char in binary:
            char = '0' if char=='1' else '1'
            result += char
        return int(result, 2)
