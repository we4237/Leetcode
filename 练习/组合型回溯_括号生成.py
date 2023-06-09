from typing import List

# 回溯
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         m = 2*n
#         ans = []
#         path = [''] * m
#         def dfs(i:int,open:int):
#             if i == m:
#                 ans.append(''.join(path))
#                 return
#
#             # 添加左括号
#             if open < n:
#                 path[i] = '('
#                 dfs(i+1,open+1)
#
#             if i - open < open:
#                 path[i] = ')'
#                 dfs(i+1,open)
#
#         dfs(0,0)
#         return ans

# 动态规划
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        total_l = []
        total_l.append([None])
        total_l.append(['()'])

        for i in range(2,n+1):
            l = []
            for j in range(i):
                now_list1 = total_l[j]
                now_list2 = total_l[i-1-j]
                for k1 in now_list1:
                    for k2 in now_list2:
                        if k1 == None:
                            k1 = ""
                        if k2 == None:
                            k2 = ""
                        el = "("+k1+")"+k2
                        l.append(el)
            total_l.append(l)
        return total_l[n]


n = 3
solution = Solution()
print(solution.generateParenthesis(n))