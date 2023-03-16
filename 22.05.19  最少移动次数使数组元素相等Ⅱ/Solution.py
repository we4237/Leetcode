from math import inf
from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        return sum(abs(mid - num) for num in nums) if (mid := sorted(nums)[len(nums)//2]) != inf else inf
