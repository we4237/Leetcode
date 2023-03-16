class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        # 动态规划
        dp = [[0]*4 for _ in range(n+1)]
        dp[0][3]=1
        for i in range(1,n+1):
            dp[i][0] = dp[i-1][3] % MOD #无
            dp[i][1] = (dp[i-1][2]+dp[i-1][0]) % MOD #上面一个
            dp[i][2] = (dp[i-1][1]+dp[i-1][0]) % MOD #下面一个
            dp[i][3] = (dp[i-1][3]+dp[i-1][2]+dp[i-1][1]+dp[i-1][0]) %MOD                #全部
        return dp[n][3]

solution = Solution()
n = 3
print(solution.numTilings(n))