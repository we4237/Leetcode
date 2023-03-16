from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        f,n,summ = 0 ,len(nums),sum(nums)
        for i,num in enumerate(nums):
            f += i * num
        res = f
        for i in range(n-1,0,-1): # 顺时针
            f = f + summ - n*nums[i]
            res = max(res,f)
        return res

nums = [4,3,2,6]
solution = Solution()
print(solution.maxRotateFunction(nums))