"""
The Skyline Problem
"""


class Maxpq:
    def __init__(self):
        self.container = []

    def front(self):
        # when there is no active building the skyline is ground.
        if not self.container: return 0, 2 ** 32
        t = self.container[0]
        return (-t[0], t[1])

    def push(self, t):
        heapq.heappush(self.container, (-t[0], t[1]))

    def pop(self):
        heapq.heappop(self.container)


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []  # x location, height(double as type), validity of the height
        closing_events = set()  # dedublicate
        for l, r, h in buildings:
            events.append((l, h, r))
            closing_events.add((r, 0, 0))
        events += list(closing_events)
        # sort by
        # 1. x - we sweep line from left to right
        # 2. event type - we add building before remove
        events.sort(key=lambda x: [x[0], -x[1]])

        skyline, pq = [], Maxpq()
        for x, h, r in events:
            # make sure tallest building is still valid
            while x >= pq.front()[1]: pq.pop()
            # if start event, add new building
            if h: pq.push((h, r))
            # update skyline if neccessary.
            if not skyline or skyline[-1][1] != pq.front()[0]:
                skyline.append([x, pq.front()[0]])
        return skyline