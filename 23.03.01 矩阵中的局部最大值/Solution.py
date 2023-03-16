from typing import List

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        N = len(grid)
        ans = [[0]*(N-2) for _ in range(N-2)]
        n = N-2
        for i in range(1,n+1):
            for j in range(1,n+1):

                ans[i-1][j-1] = max(
                    [grid[x][y] for x in range(i-1,i+2) for y in range(j-1,j+2)]
                )
        return ans

grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
solution = Solution()
print(solution.largestLocal(grid))
