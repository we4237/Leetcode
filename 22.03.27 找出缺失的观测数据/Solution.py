from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        missingSum = mean*(n+len(rolls)) - sum(rolls)
        if not n <= missingSum <= n*6:
            return []
        quotient,remainder = divmod(missingSum,n)
        return [quotient + 1]*remainder+[quotient]*(n-remainder)

rolls = [1,5,6]
mean = 3
n = 4
solution = Solution()
print(solution.missingRolls(rolls,mean,n))