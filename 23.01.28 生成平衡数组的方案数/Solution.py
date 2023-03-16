from typing import List

# 太暴力
# class Solution:
#     def waysToMakeFair(self, nums: List[int]) -> int:
#         res = 0
#
#         def calculate(nums: List[int]) -> bool:
#             sumJi,sumOu = 0,0
#             for i,x in enumerate(nums):
#                 if i % 2 == 1:
#                     sumJi += x
#                 else:
#                     sumOu += x
#
#             if sumJi == sumOu:
#                 return True
#             else:
#                 return False
#
#
#         for i in range(0,len(nums)):
#             temp = nums[:i]+nums[i+1:]
#             if calculate(temp):
#                 res += 1
#
#         return res


class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        res = ji1 = ou1 = ji2 = ou2 = 0
        for i,num in enumerate(nums):
            if i & 1:
                ji2 += num
            else:
                ou2 += num

        for i,num in enumerate(nums):
            if i & 1:
                ji2 -= num
            else:
                ou2 -= num

            if ji1 + ou2 == ji2 + ou1:
                res += 1
            if i & 1:
                ji1 += num
            else:
                ou1 += num
        return res

nums = [2,1,6,4]
solution = Solution()
print(solution.waysToMakeFair(nums))