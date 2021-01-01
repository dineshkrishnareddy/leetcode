"""
Can Place Flowers
https://leetcode.com/problems/can-place-flowers/
"""


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        count = 0

        for i in range(length):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] != 1) and (i == length - 1 or flowerbed[i + 1] != 1):
                flowerbed[i] = 1
                count += 1

        return count >= n
