from typing import List


class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        for i,row in enumerate(grid):
            for j,value in enumerate(row):
                if i == j or (i+j) == n-1:
                    if value == 0:
                        return False
                elif value != 0:
                    return False
        return True


grid = [[5,7,0],[0,3,1],[0,5,0]]
solution = Solution()
print(solution.checkXMatrix(grid))