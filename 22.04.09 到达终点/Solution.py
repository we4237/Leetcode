class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx > sx and ty > sy and tx !=ty:
            if tx > ty :
                tx %= ty
            else:
                ty %= tx
        if tx == sx and ty == sy:
            return True
        elif tx == sx:
            return ty > sy and (ty-sy) % tx == 0
        elif ty == sy:
            return tx > sx and (tx-sx) % ty == 0
        else:
            return False

sx = 3
sy = 3
tx = 12
ty = 9
solution = Solution()
print(solution.reachingPoints(sx,sy,tx,ty))
