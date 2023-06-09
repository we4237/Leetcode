from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        m,n = len(mat),len(mat[0])
        for i in range(m+n-1):
            if i % 2 != 0: # 奇数
                # 起始点
                x = 0 if i < n else i - n + 1
                y = i if i < n else n-1
                while x < m and y >= 0:
                    ans.append(mat[x][y])
                    x += 1
                    y -= 1
            else: # 偶数
                x = i if i < m else m - 1
                y = 0 if i < m else i - m + 1
                while x >= 0 and y < n:
                    ans.append(mat[x][y])
                    x -= 1
                    y += 1
        return ans

