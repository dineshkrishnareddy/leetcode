class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        perimeter = sum(matchsticks)

        side = perimeter // 4
        if side * 4 != perimeter:
            return False
        matchsticks.sort(reverse = True)
        res = [0 for _ in range(4)]

        def backtrack(index):
            if index == len(matchsticks):
                return side == res[0] == res[1] == res[2]

            for i in range(4):
                if res[i] + matchsticks[index] <= side:
                    res[i] += matchsticks[index]
                    ret = backtrack(index + 1)
                    if ret:
                        return True
                    res[i] -= matchsticks[index]

                    if res[i] == 0:
                        break

            return False

        return backtrack(0)
