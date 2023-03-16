from functools import cache
from typing import List

#记忆化搜索1
# class Solution:
#     def dieSimulator(self, n: int, rollMax: List[int]) -> int:
#         MOD = 10 ** 9 + 7
#         @cache
#         def dfs(i:int,last:int,left:int) -> int:
#             if i == 0:
#                 return 1
#             res = 0
#             for j, mx in enumerate(rollMax):
#                 if j != last:
#                     res += dfs(i-1, j, mx-1)
#                 elif left:
#                     res += dfs(i-1, j, left-1)
#             return res % MOD
#         return sum(dfs(n-1,j,mx-1) for j,mx in enumerate(rollMax)) % MOD

#记忆化搜索2
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10 ** 9 + 7
        @cache
        def dfs(i,j,x):
            if i >= n:
                return 1
            ans = 0
            for k in range(1,7):
                if k != j :
                    ans += dfs(i+1,k,1)
                elif x<rollMax[j-1]:
                    ans += dfs(i+1,j,x+1)
            return ans % MOD

        return dfs(0,0,0)

