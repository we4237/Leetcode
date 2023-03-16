from typing import List

# 2次二分
# class Solution:
#     def findMin(self,nums:List[int]):
#         n = len(nums)
#         left,right = -1,n-1
#         while left + 1 < right:
#             mid = (left + right) // 2
#             if nums[mid] > nums[-1]:
#                 left = mid
#             else:
#                 right = mid
#         return right
#
#     def search(self, nums: List[int], target: int) -> int:
#         if target not in nums:
#             return -1
#         i = self.findMin(nums)
#         n = len(nums)
#         if target <= nums[-1]:
#             left,right = i-1,n
#         else:
#             left,right = -1,i
#
#         while left + 1 < right:
#             mid = (left+right) // 2
#             if nums[mid] < target:
#                 left = mid
#             else:
#                 right = mid
#
#         return right

# 一次二分
class Solution:


    def search(self, nums: List[int], target: int) -> int:
        def is_blue(i: int) -> int:
            end = nums[-1]
            erfen_value = nums[i]
            if erfen_value > end:
                return target > end and erfen_value >= target
            else:
                return target > end or erfen_value >= target

        left, right = -1, len(nums)  # 开区间 (-1, n)
        while left + 1 < right:  # 开区间不为空
            mid = (left + right) // 2
            if is_blue(mid):  # 蓝色
                right = mid
            else:  # 红色
                left = mid
        return right if right < len(nums) and nums[right] == target else -1

nums = [3,1]
target = 3

solution = Solution()
print(
    solution.search(nums,target)
)