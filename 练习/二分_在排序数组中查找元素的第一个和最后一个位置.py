# 二分搜索
from typing import List


# class Solution:
#     def erfen(self, nums: List[int], target: int) -> int:
#         l, r = 0, len(nums) - 1
#
#         while l <= r:
#             mid = (l + r) // 2
#             if nums[mid] < target:
#                 l = mid + 1
#             else:
#                 r = mid - 1
#         return l
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         start = self.erfen(nums,target)
#         if start == len(nums) or nums[start] != target:
#             return [-1,-1]
#         end = self.erfen(nums,target+1) - 1
#         return [start,end]

# 两端开区间
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def erfen(nums:List[int],target:int) -> int:
            n = len(nums)
            left,right = -1,n
            while left + 1 < right: #区间不为空
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid
                else:
                    right = mid

            return right

        start = erfen(nums,target)
        if start == len(nums) or nums[start] != target:
            return [-1,-1]
        # target+1 比它小的就是目标
        end = erfen(nums,target+1)-1
        return [start,end]

nums = [5,7,7,8,8,10]
target = 8
solution = Solution()
print(solution.searchRange(nums,target))
