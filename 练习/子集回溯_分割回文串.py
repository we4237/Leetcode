from typing import List

# 专注过程,选或不选
# class Solution:
#     def partition(self, s: str) -> List[List[str]]:
#         ans = []
#         path = []
#         n = len(s)
#
#         # start 表示当前这段回文子串的开始位置
#         def dfs(i: int, start: int) -> None:
#             if i == n:
#                 ans.append(path.copy())  # 固定答案
#                 return
#
#             # 不选 i 和 i+1 之间的逗号（i=n-1 时右边没有逗号）
#             if i < n - 1:
#                 dfs(i + 1, start)
#
#             # 选 i 和 i+1 之间的逗号
#             t = s[start: i + 1]
#
#             if t == t[::-1]:  # 判断是否回文
#                 path.append(t)
#                 dfs(i + 1, i + 1)
#                 path.pop()  # 恢复现场
#
#         dfs(0, 0)
#         return ans

# class Solution:
#     def partition(self, s: str) -> List[List[str]]:
#         ans = []
#         path = []
#         n = len(s)
#
#         # start 表示当前这段回文子串的开始位置
#         def dfs(i: int) -> None:
#
#             if i == n:
#                 ans.append(path.copy())  # 固定答案
#                 return
#
#             for j in range(i,n):
#                 t = s[i:j+1]
#                 if t == t[::-1]:  # 判断是否回文
#                     path.append(t)
#                     dfs(j + 1)
#                     path.pop()  # 恢复现场
#
#         dfs(0)
#         return ans

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        tmp = []

        # 转换为在字符串中间分割的问题
        def dfs(i:int,start:int):
            if i == n:
                ans.append(tmp.copy())
                return

            if i < n-1:
            # 不选
                dfs(i+1,start)

            # 选
            t = s[start:i+1]
            if t == t[::-1]:
                tmp.append(t)
                dfs(i+1,i+1)
                tmp.pop()

        dfs(0,0)
        return ans



s = "aab"
solution = Solution()
print(solution.partition(s))