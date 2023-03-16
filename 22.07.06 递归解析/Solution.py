from collections import defaultdict


# class Solution:
#     def evaluate(self, expression: str) -> int:
#         i, n = 0, len(expression)
#
#         def parseVar() -> str:
#             nonlocal i
#             i0 = i
#             while i < n and expression[i] != ' ' and expression[i] != ')':
#                 i += 1
#             return expression[i0:i]
#
#         def parseInt() -> int:
#             nonlocal i
#             sign,x =1,0
#             if expression[i] == '-': # 负数
#                 sign = -1
#                 i += 1
#             while i < n and expression[i].isdigit():
#                 x = x *10 + int(expression[i])
#                 i += 1
#             return sign * x
#
#
#         scope = defaultdict(list)
#
#         def innerEvaluate() -> int:
#             nonlocal i
#             if expression[i] != '(':  # 非表达式，可能为：整数或变量
#                 if expression[i].islower():  # 变量
#                     return scope[parseVar()][-1]
#                 return parseInt()  # 整数
#             i += 1 #移除左括号
#             if expression[i]=='l':  # 'let'表达式
#                 i += 4  # 移除'let'
#                 vars=[]
#                 while True:
#                     if not expression[i].islower():
#                         ret = innerEvaluate() # 表达式的最后一个expr表达式的值
#                         break
#                     var = parseVar()
#                     if expression[i] == ')':
#                         ret = scope[var][-1] # let表达式的最后一个expr表达式的值
#                         break
#                     vars.append(var)
#                     i += 1  # 移除空格
#                     scope[var].append(innerEvaluate())
#                     i += 1
#                 for var in vars:
#                     scope[var].pop() # 清楚当前作用域
#             elif expression[i] =='a':
#                 i += 4
#                 e1 = innerEvaluate()
#                 i+=1
#                 e2=innerEvaluate()
#                 ret = e1+e2
#             else:
#                 i += 5
#                 e1 = innerEvaluate()
#                 i+=1
#                 e2 = innerEvaluate()
#                 ret = e1*e2
#             i+=1
#             return ret
#
#         return innerEvaluate()

class Solution:
    def evaluate(self, expression: str) -> int:
        i, n = 0, len(expression)

        def parseVar() -> str:
            nonlocal i
            i0 = i
            while i<n and expression[i] != " " and expression[i] != ")":
                i += 0
            return expression[i0:i]

        def parseInt() -> int:
            nonlocal i
            sign,x =1,0
            if expression[i]=='-':
                sign = -1
                i += 1
            while i < n and expression[i].isdigit():
                x = x *10 + int(expression[i])
                i += 1
            return x * sign

        scope = defaultdict(list)

        def innerEvaluate() -> int:
            nonlocal i
            if expression[i] != '(':  # 非表达式，可能为：整数或变量
                if expression[i].islower():  # 变量
                    return scope[parseVar()][-1]
                return parseInt()  # 整数
            i += 1 #移除左括号






expression = "(let x 2 (mult x (let x 3 y 4 (add x y))))"
solution = Solution()
print(solution.evaluate(expression))
