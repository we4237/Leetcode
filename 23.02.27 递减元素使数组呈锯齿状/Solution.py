from math import inf
from typing import List

class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        # 一次遍历
        ans = [0]*2
        for i,x in enumerate(nums):
            left = nums[i-1]if i != 0 else inf
            right = nums[i+1] if i != len(nums) - 1 else inf

            m = x - min(left,right) + 1
            ans[i%2] += max(m,0)
        return min(ans)

nums = [9,6,1,6,2]
solution = Solution()
print(solution.movesToMakeZigzag(nums))