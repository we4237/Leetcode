from typing import List


class Solution:
    def minArray(self, nums: List[int]) -> int:
        n = len(nums)
        left,right = -1,n-1
        while left  < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1

        return nums[left]

nums = [3,1,3]
solution = Solution()
print(solution.minArray(nums))