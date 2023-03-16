from typing import List


# class Solution:
#     def partitionDisjoint(self, nums: List[int]) -> int:
#         n = len(nums)
#         minright = n * [0]
#         minright[-1] = nums[-1]
#
#         for i in range(n-2,0,-1):
#             minright[i]=min(minright[i+1],nums[i])
#
#         maxleft = n * [100000]
#         maxleft[0] = nums[0]
#         for i in range(1,n):
#             maxleft[i]=max(maxleft[i-1],nums[i])
#
#         for i in range(0,n):
#             if maxleft[i]<=minright[i+1]:
#                 return i+1


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        cur_max = left_max = nums[0]
        left_pos = 0
        for i in range(1,n-1):
            cur_max = max(cur_max,nums[i])
            if nums[i] < left_max:
                left_max,left_pos=cur_max,i
        return left_pos+1

nums=[5,0,3,8,6]
solution = Solution()
print(solution.partitionDisjoint(nums))
