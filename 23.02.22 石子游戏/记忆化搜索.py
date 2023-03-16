# 回溯
from typing import List


# 回溯超时
# class Solution:
#     def stoneGameII(self, s: List[int]) -> int:
#         n = len(s)
#         for i in range(n-2,-1,-1):
#             s[i] += s[i+1]
#         @cache
#         def dfs(i:int,m:int):
#             if i + m * 2 >= n:
#                 return s[i]
#             return s[i] - min(dfs(i+x , max(m,x)) for x in range(1, m * 2 +1) )
#
#
#         return dfs(0,1)

piles = [2,7,9,4,4]
solution = Solution()
print(solution.stoneGameII(piles))