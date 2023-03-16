from typing import List

# 正序遍历的组合型回溯
# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         ans = []
#         path = []
#
#         # i < k - m(path的长)
#         def dfs(i:int):
#             # d = k - len(path)
#             # if i < d:
#             #     return
#
#             if len(path) == k:
#                 ans.append(path.copy())
#                 return
#
#             for j in range(i,n+1):
#                 if (n+1-i+len(path)<k):
#                     return
#                 path.append(j)
#                 dfs(j+1)
#                 path.pop()
#
#
#         dfs(1)
#
#         return ans

# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         ans = []
#         path = []
#         def dfs(start:int):
#
#             if len(path) == k:
#                 ans.append(path.copy())
#                 return
#
#             for j in range(start,0,-1):
#                 if k-len(path) > start:
#                     return
#                 path.append(j)
#                 dfs(j-1)
#                 path.pop()
#         dfs(n)
#         return ans

# 选或不选
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        ans = []
        path = []
        def dfs(i:int):
            d = k - len(path)
            if d == 0:
                ans.append(path.copy())
                return
            # 不选
            if d < i:
                dfs(i-1)

            path.append(i)
            dfs(i-1)
            path.pop()

        dfs(n)
        return ans

n = 4
k = 2
solution = Solution()
print(solution.combine(n,k))




