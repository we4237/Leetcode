from math import gcd


class Solution:
    def fractionAddition(self, expression: str) -> str:
        son,mother = 0,1
        i,n = 0, len(expression)
        while i < n:
            # 读取分子
            son_,sign = 0,1
            if expression[i] == '-' or expression[i] == '+':
                if expression[i]=='-':
                    sign = -1
                i += 1
            while i < n and expression[i].isdigit():
                son_ = son_*10 + int(expression[i])
                i += 1
            son_ = sign * son_
            i += 1

            # 读取分母
            mother_ = 0
            while i < n and expression[i].isdigit():
                mother_ = mother_*10 + int(expression[i])
                i += 1

            son = son_ * mother + mother_ * son
            mother *= mother_
        if son == 0:
            return "0/1"
        g = gcd(abs(son),mother)
        return f"{son//g}/{mother//g}"


expression = "-1/2+1/2+1/3"
solution = Solution()
print(solution.fractionAddition(expression))