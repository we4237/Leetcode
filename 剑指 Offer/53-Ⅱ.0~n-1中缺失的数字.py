from typing import List

# 哈希
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         s = set(nums)
#         for i in range(len(nums) + 1):
#             if i not in s:
#                 return i

# 二分
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        left,right = 0,n-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == mid:
                left = mid + 1
            else:
                right = mid - 1
        return left

nums = [0,1,2,3,4,5,6,7,9]
solution = Solution()
print(solution.missingNumber(nums))