from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        ans,n = 0,len(nums)
        vis = [False]*n
        for i in range(n):
            cnt = 0
            while not vis[i]:
                vis[i] = True
                i = nums[i]
                cnt += 1
            ans =max(cnt,ans)
        return ans

A = [5,4,0,3,1,6,2]
solution = Solution()
print(solution.arrayNesting(A))
