from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(accounts[i]) for i in range(len(accounts)))

accounts = [[1,2,3],[3,2,1]]
solution = Solution()
print(solution.maximumWealth(accounts))