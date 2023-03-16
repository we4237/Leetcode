import random
from typing import List


class Solution:

    def __init__(self, rects: List[List[int]]):
        self.recs = rects

    def pick(self) -> List[int]:
        curSum = 0
        idx = 0
        for i,(x1,y1,x2,y2) in enumerate(self.recs):
            cur = (x2-x1+1)*(y2-y1+1)
            curSum += cur
            if random.randint(0,curSum)<cur:
                idx = i
        x1,y1,x2,y2 = self.recs[idx]
        return [random.randint(x1,x2),random.randint(y1,y2)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()