from typing import List


# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         n = len(nums)
#         res = []
#         if (not nums or n<3):
#             return []
#         nums.sort()
#         for i in range(n):
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue
#             L = i+1
#             R = n-1
#             while (L<R):
#                 if (nums[i]+nums[L]+nums[R] == 0):
#                     res.append([nums[i],nums[L],nums[R]])
#                     while(L<R and nums[L]==nums[L+1]):
#                         L= L + 1
#                     while (L < R and nums[R] == nums[R - 1]):
#                         R = R - 1
#                     L = L + 1
#                     R = R - 1
#                 elif(nums[i]+nums[L]+nums[R]>0):
#                     R = R - 1
#                 else:
#                     L = L + 1
#
#         return res



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n-2):
            x = nums[i]
            if i > 0 and x == nums[i-1]:
                continue
            # 优化
            if x +nums[i]+nums[i+1]>0:
                break
            if x + nums[-2]+nums[-1]<0:
                continue
            j = i + 1
            k = n - 1
            while (j<k):
                s = x + nums[j] + nums[k]
                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    ans.append([x,nums[j],nums[k]])
                    j += 1
                    while j<k and nums[j] == nums[j-1]:
                        j += 1
                    k -= 1
                    while k>j and nums[k] == nums[k+1]:
                        k -= 1
        return ans


nums = [1,-1,-1,0]
solution = Solution()
print(solution.threeSum(nums))