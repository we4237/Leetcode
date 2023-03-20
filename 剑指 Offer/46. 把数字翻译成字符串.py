class Solution:
    def translateNum(self, num: int) -> int:
        # 用字符串相加代替数字
        s = str(num)
        a = b = 1
        for i in range(2,len(s)+1):
            tmp = s[i-2:i]
            c = a + b if '10' <= tmp <= '25' else a
            b = a
            a = c
        return a

num =  12258
solution = Solution()
print(solution.translateNum(num))
