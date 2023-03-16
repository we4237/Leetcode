from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m,n = len(grid),len(grid[0])
        ans = [[0]*n for _ in range(m)]
        for i,row in enumerate(grid):
            for j,line in enumerate(row):
                index1 =(i*n+j+k)%(m*n)
                ans[index1 // n][index1%n] = line
        return ans