"""
Design Circular Queue
https://leetcode.com/problems/design-circular-queue/
"""


class MyCircularQueue:

    def __init__(self, k: int):
        self.vals = [-1 for _ in range(k)]
        self.curr = 0
        self.max = k

    def enQueue(self, value: int) -> bool:
        if self.curr >= self.max:
            return False
        self.vals[self.curr] = value
        self.curr += 1
        return True

    def deQueue(self) -> bool:
        if self.curr == 0:
            return False
        self.vals.pop(0)
        self.vals.append(-1)
        self.curr -= 1
        return True

    def Front(self) -> int:
        if self.curr == 0:
            return -1
        return self.vals[0]

    def Rear(self) -> int:
        if self.curr == 0:
            return -1
        return self.vals[self.curr - 1]

    def isEmpty(self) -> bool:
        return self.curr == 0

    def isFull(self) -> bool:
        return self.curr == self.max

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
