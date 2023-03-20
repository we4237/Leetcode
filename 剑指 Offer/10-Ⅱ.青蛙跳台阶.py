# class Solution:
#     def numWays(self, n: int) -> int:
#         MOD = 1000000007
#         if n == 0:
#             return 1
#         elif n == 1:
#             return 1
#         dp = [0 for _ in range(n)]
#         dp[0] = 1
#         dp[1] = 2
#         for i in range(2,n):
#             dp[i] = dp[i-1] + dp[i-2]
#
#         return dp[n-1] % MOD
class Solution:
    def numWays(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007



solution = Solution()
n = 7
print(solution.numWays(7))