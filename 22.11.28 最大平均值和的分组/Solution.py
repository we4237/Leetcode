from itertools import accumulate
from typing import List


class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        # n = len(nums)
        # prefix = list(accumulate(nums,initial = 0))
        # dp = [[0.0] * (k+1) for _ in range(n+1)]
        # for i in range(1, n + 1):
        #     dp[i][1] = prefix[i] / i
        # for j in range(2,k+1):
        #     for i in range(j,n+1):
        #         for x in range(j-1,i):
        #             dp[i][j] = max(dp[i][j],dp[x][j-1]+(prefix[i] - prefix[x])/(i-x))
        # return dp[n][k]

        n = len(nums)
        psum = [0]*(n+1)
        for i in range(1,n+1):
            psum[i] = psum[i-1]+nums[i-1]
        f = [[0] * (k+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,min(i,k)+1):
                if j == 1:
                    f[i][j] = psum[i]/i
                else:
                    for m in range(2,i+1):
                        f[i][j] = max(f[i][j],f[m-1][j-1] + (psum[i] - psum[m-1])/(i-m+1))
        return f[n][k]



nums = [9, 1, 2, 3, 9]
k = 3
solution = Solution()
print(solution.largestSumOfAverages(nums,k))
