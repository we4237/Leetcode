from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = 0
        prod,i = 1,0
        for j,num in enumerate(nums):
            prod *= num
            while i <= j and prod >=k:
                prod //= nums[i]
                i += 1
            ans +=  j - i + 1
        return ans