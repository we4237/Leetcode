from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        path = []
        def dfs(i:int,sheng):
            if i == n:
                ans.append(path.copy())
                return
            for x in sheng:
                path.append(x)
                dfs(i+1,sheng-{x})
                path.pop()
        dfs(0,set(nums))
        return ans

nums = [1,2,3]
solution = Solution()
print(solution.permute(nums))