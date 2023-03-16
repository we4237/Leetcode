from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        # def signFunc(num:int)->int:
        #     if num > 0:
        #         return 1
        #     elif num < 0:
        #         return -1
        #     else:
        #         return 0
        #
        # res = 1
        # cnt = 1
        # for i,num in enumerate(nums):
        #     if signFunc(num) == 0:
        #         return 0
        #     else:
        #        cnt *= signFunc(num)
        #        # res *= abs(num)
        #
        # return cnt
        ans = 1
        for x in nums:
            if x==0:
                return 0
            elif x<0:
                ans *=-1
        return ans

nums = [-1,-2,-3,-4,3,2,1]
solution = Solution()
print(solution.arraySign(nums))