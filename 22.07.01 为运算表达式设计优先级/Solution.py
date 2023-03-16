from functools import cache
from typing import List

ADDITION = -1
SUBTRACTION = -2
MULTIPLICATION = -3

# #动态规划 自下而上
# class Solution:
#     def diffWaysToCompute(self, expression: str) -> List[int]:
#         ops = []
#         i,n = 0,len(expression)
#         # 放入列表
#         while i < n :
#             if expression[i].isdigit():
#                 x = 0
#                 while i < n and expression[i].isdigit():
#                     x = x *10 +int(expression[i])
#                     i+=1
#                 ops.append(x)
#             else:
#                 if expression[i]=='+':
#                     ops.append(ADDITION)
#                 elif expression[i] == '-':
#                     ops.append(SUBTRACTION)
#                 else:
#                     ops.append(MULTIPLICATION)
#                 i += 1
#
#         n = len(ops)
#         dp = [[[]for _ in range(n)]for _ in range(n)] #n*n个列表
#         for i,x in enumerate(ops):
#             dp[i][i]=[x]
#
#         #从长度为3的子问题开始计算
#         for size in range(3,n+1):
#             # 右边界
#             for r in range(size-1,n,2):
#                 # 左边界
#                 l = r - size + 1
#                 # 符号
#                 for k in range(l+1,r,2):
#                     for x in dp[l][k-1]:
#                         for y in dp[k+1][r]:
#                             if ops[k]==ADDITION:
#                                 dp[l][r].append(x+y)
#                             elif ops[k]==SUBTRACTION:
#                                 dp[l][r].append(x-y)
#                             else:
#                                 dp[l][r].append(x*y)
#         return dp[0][-1]

#记忆化搜索 自上而下
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ops = []
        i,n = 0,len(expression)
        # 放入列表
        while i < n :
            if expression[i].isdigit():
                x = 0
                while i < n and expression[i].isdigit():
                    x = x *10 +int(expression[i])
                    i+=1
                ops.append(x)
            else:
                if expression[i]=='+':
                    ops.append(ADDITION)
                elif expression[i] == '-':
                    ops.append(SUBTRACTION)
                else:
                    ops.append(MULTIPLICATION)
                i += 1

        @cache
        def dfs(l:int,r:int)->List[int]:
            #设置终止条件
            if l == r:
                return [ops[l]]
            res = []
            for i in range(l,r,2):
                left=dfs(l,i)
                right=dfs(i+2,r)
                for x in left:
                    for y in right:
                        if ops[i+1]==ADDITION:
                            res.append(x+y)
                        elif ops[i+1]==SUBTRACTION:
                            res.append(x-y)
                        else:
                            res.append(x*y)
            return res

        return dfs(0,len(ops)-1)



expression = "2-1-1"
solution = Solution()
print(solution.diffWaysToCompute(expression))