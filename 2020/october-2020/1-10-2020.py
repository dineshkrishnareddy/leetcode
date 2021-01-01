"""

"""


class RecentCounter:
    LIMIT = 3000

    def __init__(self):
        self.recent = []

    def ping(self, t: int) -> int:
        min_limit = t - self.LIMIT
        index = 0
        while index < len(self.recent):
            if self.recent[index] >= min_limit:
                break
            index += 1
        self.recent = self.recent[index:]
        self.recent.append(t)
        return len(self.recent)

# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
t = [[642],[1849],[4921],[5936],[5957]]
obj.ping(t[0][0])
obj.ping(t[1][0])
obj.ping(t[2][0])
obj.ping(t[3][0])
obj.ping(t[4][0])
