from cmath import inf
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        n = len(nums)
        ans = 0
        ji = 1
        left = 0

        for right,x in enumerate(nums):
            ji *= x
            while ji >= k:
                ji //= nums[left]
                left += 1

            ans += right - left + 1

        return ans

nums = [10,5,2,6]
k = 100
solution = Solution()
print(solution.numSubarrayProductLessThanK(nums,k))
