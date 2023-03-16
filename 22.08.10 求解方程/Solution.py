class Solution:
    def solveEquation(self, equation: str) -> str:
        factor = val = 0
        i , n , sign = 0 , len(equation) , 1
        while i < n:
            if equation[i] == '=':
                sign = -1
                i += 1
                continue
            s = sign
            if equation[i] == '+':
                i += 1
            elif equation[i]=='-':
                s = -s
                i += 1

            num , valid = 0,False
            while i<n and equation[i].isdigit():
                num = 10*num + int(equation[i])
                valid = True
                i += 1
            if i<n and equation[i]=='x':
                factor += s*num if valid else s # valid是否有效,如果valid无效则为变量
                i += 1
            else: #数值
                val += s*num

        if factor == 0:
            return 'No solution'if val else 'Infinite solutions'
        return f"x={-val // factor}"
