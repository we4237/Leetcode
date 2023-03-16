from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        # n = len(prices)
        # dp = [0 for _ in range(n)]
        # dp[0] = 0
        # for i in range(1,n):
        #     dp[i] = max(dp[i-1],prices[i]-min(prices[:i]))
        #
        # return max(dp)
        cost, profit = float("+inf"), 0
        for price in prices:
            cost = min(cost, price)
            profit = max(profit, price - cost)
        return profit

prices = [7,1,5,3,6,4]
solution = Solution()
print(solution.maxProfit(prices))
