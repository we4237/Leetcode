from functools import cache

DIFFS = (0, 0, 1, -1, -1, 1, 1, -1, 0, 1)

class Solution:
    def rotatedDigits(self, n: int) -> int:
        s = str(n)
        @cache
        def f(i:int,hasdiff:bool,is_limit:bool) -> int:
            if i == len(s):
                return hasdiff
            res = 0
            up = int(s[i]) if is_limit else 9
            for d in range(0,up + 1 ):
                if DIFFS[d] != -1:
                    res += f(i+1,hasdiff or DIFFS[d],is_limit and d== up)
            return res
        return f(0,False,True)

n = 10
solution = Solution()
print(solution.rotatedDigits(n))