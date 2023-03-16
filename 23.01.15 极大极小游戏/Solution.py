from typing import List
import math

# class Solution:
#     def searchMin(self,nums: List[int]) -> List[int]:
    #     n = len(nums)
    #     small = [0 for _ in range(n//2)]
    #     for i in range(0,n//2):
    #         if i % 2 == 0:
    #             small[i] = min(nums[2 * i], nums[2 * i + 1])
    #     return small
    #
    # def searchMax(self, nums: List[int]) -> List[int]:
    #     n = len(nums)
    #     large = [0 for _ in range(n//2)]
    #     for i in range(0, n // 2):
    #         if i % 2 == 1:
    #             large[i] = max(nums[2 * i], nums[2 * i + 1])
    #     return large
    #
    # def minMaxGame(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     if n == 1:
    #         return nums[0]
    #     temp = []
    #     newnums = nums
    #     while n > 1:
    #         small = self.searchMin(newnums)
    #         large = self.searchMax(newnums)
    #         for i in range(0,n//2):
    #             if i % 2 == 0:
    #                 temp.append(small[i])
    #             else:
    #                 temp.append(large[i])
    #         newnums = temp
    #         n = len(temp)
    #         temp = []


        # return newnums[0]

class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        n = len(nums)
        while n > 1:
            n >>= 1
            for i in range(n):
                a, b = nums[i << 1], nums[i << 1 | 1]
                nums[i] = min(a, b) if i % 2 == 0 else max(a, b)
        return nums[0]




nums =[1,3,5,2,4,8,2,2]
solution = Solution()
print(solution.minMaxGame(nums))


