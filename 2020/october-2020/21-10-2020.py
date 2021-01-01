"""
Asteroid Collision
https://leetcode.com/problems/asteroid-collision/
"""


class Solution:

    def asteroidCollision(self, asteroids):
        if len(asteroids) == 0:
            return []

        result = [asteroids[0]]

        for asteroid in asteroids[1:]:
            if asteroid < 0:
                curr = abs(asteroid)
                available = True
                while len(result) and 0 < result[-1]:
                    prev = abs(result[-1])
                    if prev == curr:
                        result.pop()
                        available = False
                        break
                    elif prev < curr:
                        result.pop()
                    else:
                        available = False
                        break

                if available:
                    result.append(asteroid)
            else:
                result.append(asteroid)

        return result


print(Solution().asteroidCollision([5,10,-5]))
print(Solution().asteroidCollision([10,2,-5]))
print(Solution().asteroidCollision([5,-5]))
print(Solution().asteroidCollision([-2,-1,1,2]))
print(Solution().asteroidCollision([-2,-2,1,-2]))
print(Solution().asteroidCollision([-2,-2,-1,-2]))
