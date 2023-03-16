from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = costs[0]
        for i in range(1,len(costs)):
            dp = [min(dp[j-1],dp[j-2])+ c for j,c in enumerate(costs[i])]
        return min(dp)

costs = [[17,2,17],[16,16,5],[14,3,19]]
solution = Solution()
print(solution.minCost(costs))