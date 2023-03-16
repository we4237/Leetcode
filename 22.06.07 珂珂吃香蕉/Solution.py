from bisect import bisect_left
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        return bisect_left(range(max(piles)),-h,1,key = lambda k:-sum((pile + k -1)//k for pile in piles))


piles = [3,6,7,11]
h = 8
solution = Solution()
print(solution.minEatingSpeed(piles,h))