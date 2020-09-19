"""
Sequential Digits
"""


class Solution:
    def digits_count(self, num):
        return len(str(num))

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        low_count = self.digits_count(low)
        high_count = self.digits_count(high)

        result = []
        for count in range(low_count, high_count + 1):
            for start in range(1, 10 - count + 1):
                num = int(''.join([str(x) for x in range(start, start + count)]))
                if num < low:
                    continue
                elif num > high:
                    break
                result.append(num)
        return result
