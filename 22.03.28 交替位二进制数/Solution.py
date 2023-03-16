class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # prev = 2
        # while n:
        #     cur = n % 2
        #     if cur == prev:
        #         return False
        #     prev = cur
        #     n //= 2
        # return True
        a = n ^ (n >> 1)
        return a & (a + 1) == 0

n = 5
solution = Solution()
print(solution.hasAlternatingBits(n))
