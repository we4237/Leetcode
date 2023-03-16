from typing import List


# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         ans = []
#         col = [0] * n
#         def valid(r,c):
#             for R in range(r):
#                 C = col[R]
#                 if r+c == R+C or r-c == R-C:
#                     return False
#             return True
#
#         def dfs(i:int,s:set):
#             if i == n:
#                 # 将全排列放到棋盘上
#                 ans.append(['.' * c + 'Q' + '.' * (n-1-c) for c in col])
#                 return
#
#             for x in s:
#                 if valid(i,x):
#                     col[i] = x
#                     dfs(i+1,s-{x})
#
#         dfs(0,set(range(n)))
#
#         return ans

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        col = [0] * n

        def dfs(r:int,s:set):
            if r == n:
                ans.append(['.' * c + 'Q' + '.' * (n-c-1) for c in col])
                return

            for c in s:
                # 当前每一个皇后的航和列做判断
                if all(R+col[R] != r+c and R-col[R] != r-c for R in range(r)):
                    col[r] = c
                    dfs(r + 1, s - {c})

        dfs(0, set(range(n)))

        return ans

n = 4
solution = Solution()
print(
    solution.solveNQueens(n)
)