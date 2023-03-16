from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        xy = sum(i>0  for row in grid for i in row )
        yz = sum(map(max, zip(*grid)))
        xz = sum(map(max, grid))
        return xy+yz+xz
