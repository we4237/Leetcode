from functools import cache


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        @cache
        def dfs(usedNumbers: int, currentTotal: int) -> bool:
            for i in range(maxChoosableInteger):
                if (usedNumbers >> i ) & 1 ==0:
                    if currentTotal + i + 1 >= desiredTotal or not dfs(usedNumbers|(1 << i),currentTotal + i + 1):
                        return True
            return False


        return (maxChoosableInteger+1)*maxChoosableInteger//2 > desiredTotal and dfs(0,0)

