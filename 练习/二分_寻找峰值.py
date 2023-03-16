from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        left,right = -1,n-1

        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid+1]:
                left = mid

            else:
                right = mid
        return right

nums = [1,2]
solution = Solution()
print(solution.findPeakElement(nums))

