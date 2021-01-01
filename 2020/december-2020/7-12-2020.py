"""
Spiral Matrix II
https://leetcode.com/problems/spiral-matrix-ii/
"""

class Solution:
    def generateMatrix(self, n: int):
        if n == 0:
            return []
        if n == 1:
            return [[1]]

        directions = {
            'U': [-1, 0],
            'R': [0, 1],
            'L': [0, -1],
            'D': [1, 0]
        }
        count = n**2
        curr = 1
        result = [[-1 for i in range(n)] for j in range(n)]
        curr_direction = 'R'
        curr_x = 0
        curr_y = 0
        while curr < count:
            if curr_direction == 'R':
                result[curr_x][curr_y] = curr
                temp_x = curr_x + directions[curr_direction][0]
                temp_y = curr_y + directions[curr_direction][1]
                if temp_y >= n or result[temp_x][temp_y] != -1:
                    curr_direction = 'D'
                    continue
                else:
                    curr_x = temp_x
                    curr_y = temp_y

            elif curr_direction == 'D':
                result[curr_x][curr_y] = curr
                temp_x = curr_x + directions[curr_direction][0]
                temp_y = curr_y + directions[curr_direction][1]
                if temp_x >= n or result[temp_x][temp_y] != -1:
                    curr_direction = 'L'
                    continue
                else:
                    curr_x = temp_x
                    curr_y = temp_y

            elif curr_direction == 'L':
                result[curr_x][curr_y] = curr
                temp_x = curr_x + directions[curr_direction][0]
                temp_y = curr_y + directions[curr_direction][1]
                if temp_y < 0 or result[temp_x][temp_y] != -1:
                    curr_direction = 'U'
                    continue
                else:
                    curr_x = temp_x
                    curr_y = temp_y

            elif curr_direction == 'U':
                result[curr_x][curr_y] = curr
                temp_x = curr_x + directions[curr_direction][0]
                temp_y = curr_y + directions[curr_direction][1]
                if temp_x < 0 or result[temp_x][temp_y] != -1:
                    curr_direction = 'R'
                    continue
                else:
                    curr_x = temp_x
                    curr_y = temp_y

            curr += 1
        result[curr_x][curr_y] = count
        return result


print(Solution().generateMatrix(3))
