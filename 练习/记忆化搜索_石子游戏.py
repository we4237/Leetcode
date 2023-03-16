from functools import cache
from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @cache
        def helper(i,j):
            if i == j:return piles[i]
            return max(piles[i]-helper(i+1,j),
                       piles[j]-helper(i,j-1))
        return helper(0,len(piles)-1)>0
