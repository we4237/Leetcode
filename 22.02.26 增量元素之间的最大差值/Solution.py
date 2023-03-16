from math import inf

from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n=len(nums)
        ans = -1
        premin = nums[0]

        for i in range(1,n):
            if nums[i] > premin:
                ans = max(ans,nums[i]-premin)
            else:
                premin = nums[i]
        return ans

class Solution1:
    def maximumDifference(self, nums: List[int]) -> int:
        m = inf
        ans = 0
        for num in nums:
            m = min(num,m)
            ans = max(ans,num-m)
        return ans if ans > 0 else -1

nums = [7,1,5,4]
solution = Solution()
print(solution.maximumDifference(nums))