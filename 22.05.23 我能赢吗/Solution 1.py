from functools import cache


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if (1 + maxChoosableInteger) * maxChoosableInteger // 2 < desiredTotal:
            return False
        @cache
        def dfs(sc, state):
            """ 当前分数，当前状态, 返回当前玩家能不能赢 """
            select = 2 << (maxChoosableInteger - 1)
            ad = maxChoosableInteger
            while select > 1:
                if (state & select) == 0:
                    # 分数超过则立刻胜利，或者对方不能赢那我就能赢
                    if sc + ad >= desiredTotal or not dfs(sc + ad, state | select):
                        return True
                select >>= 1
                ad -= 1
            return False
        return dfs(0, 0)

maxChoosableInteger = 10
desiredTotal = 11
solution = Solution()
print(solution.canIWin(maxChoosableInteger,desiredTotal))
