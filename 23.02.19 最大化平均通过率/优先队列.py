from heapq import heapify, heapreplace
from typing import List


class Entry:
    __slots__ = 'p','t'
    def __init__(self,p:int,t:int):
        self.p = p
        self.t = t

    def __lt__(self, j:'Entry') -> bool:
        return (j.t + 1) * (j.t) * (self.t - self.p) > (self.t + 1) * (self.t) * (j.t - j.p)


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        h = [Entry(*c) for c in classes] # 将列表解开（unpacke）成多个独立的参数
        heapify(h) # 将列表改变成heap结构
        for _ in range(extraStudents):
            heapreplace(h,Entry(h[0].p + 1 , h[0].t + 1))
        return sum(e.p/e.t for e in h) / len(h)


classes = [[1,2],[3,5],[2,2]]
extraStudents = 2
solution = Solution()
print(solution.maxAverageRatio(classes,extraStudents))