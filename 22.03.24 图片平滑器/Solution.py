from itertools import product
from typing import List

dirs = list(product(*[[-1,0,1]] *2))

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m,n = len(img),len(img[0])
        ans = [[0]*n for _ in range(m)]
        for i, j in product(range(m),range(n)):
            total,cnt = 0,0
            for di in dirs:
                if 0 <= (nx := i + di[0]) < m and 0 <= (ny := j + di[1]) < n:
                    total += img[nx][ny]
                    cnt += 1
            ans[i][j] = total//cnt
        return ans


img = [[1,1,1],[1,0,1],[1,1,1]]
print(dirs)
solution = Solution()
print(solution.imageSmoother(img))