# 二维数组n*m 每一行从左到右递增 每一列从上到下递增
#
# 整数值 二维数组里是否包含这个整数k
from typing import List


class Solution:
    def search(self,grid:List[List[int]],k:int)->bool:
        n = len(grid)
        m = len(grid[0])
        i,j = 0,m-1
        while i < n and j >= 0:
            if k > grid[i][j]:
                i += 1
            elif k < grid[i][j]:
                j -= 1
            else:
                return




grid = [[1,2,3],[2,3,4],[3,4,5]]
k = 3
soluiton = Solution()
soluiton.search(grid,k)




