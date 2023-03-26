from collections import defaultdict, Counter
from typing import List


class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        haxi = defaultdict()
        n = len(nums)
        for i in range(0,n-1):
            if nums[i] + nums[i+1] in haxi.keys():
                return True

            else:
                haxi[nums[i] + nums[i + 1]] = 1

        return False

nums = [1,2,3,4,5]
solution = Solution()
print(solution.findSubarrays(nums))



