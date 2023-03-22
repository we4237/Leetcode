from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        teams = sorted(zip(scores,ages))
        n = len(scores)
        dp = [0] * len(scores)
        ans = 0
        for i,(score,age) in enumerate(teams):
            for j in range(i):
                if age >= teams[j][1]:
                    dp[i] = max(dp[i],dp[j])

            dp[i] += score
            ans = max(ans,dp[i])
        return ans



scores = [4,5,6,5]
ages = [2,1,2,1]
solution = Solution()
print(solution.bestTeamScore(scores,ages))