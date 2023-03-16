from typing import List


class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        n = len(cuboids)
        for c in cuboids:
            c.sort()
        cuboids.sort()
        f = [0]*n
        for i,(_,l2,h2) in enumerate(cuboids):
            for j,(_,l1,h1) in enumerate(cuboids[:i]):# w1 < w2 恒成立
                if h1<=h2 and l1<=l2:
                    f[i] = max(f[i], f[j])  # cuboids[j] 可以堆在 cuboids[i] 上
            f[i] += h2

        return max(f)


cuboids = [[50, 45, 20], [95, 37, 53], [45, 23, 12]]
solution = Solution()
print(solution.maxHeight(cuboids))