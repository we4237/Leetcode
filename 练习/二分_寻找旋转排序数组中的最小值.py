from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left,right = -1,n-1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid
            else:
                right = mid

        return nums[right]

nums = [2,3,4,5,1]
solution = Solution()
print(
    solution.findMin(nums)
)