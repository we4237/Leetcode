
import bisect


class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def zeta(n:int)->int:#计算阶乘后0的数量
            res = 0
            while n:
                n //=5
                res += n
            return res

        def nx(k:int)->int:
            return bisect.bisect_left(range(5 * k), k, key=zeta)

        return nx(k+1)-nx(k)

k = 0
solution = Solution()
print(solution.preimageSizeFZF(k))