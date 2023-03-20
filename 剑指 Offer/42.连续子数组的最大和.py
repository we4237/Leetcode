from typing import List

# 超时
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         n = len(nums)
#         ans = nums[0]
#         for i in range(n):
#             for j in range(i,n):
#                 ans = max(ans,sum(nums[i:j+1]))
#         return ans
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = [nums[x] for x in range(n)]

        for i in range(1, len(nums)):
            ans[i] += max(ans[i - 1], 0)
        return max(ans)




nums = [-2,1,-3,4,-1,2,1,-5,4]
solution = Solution()
print(solution.maxSubArray(nums))