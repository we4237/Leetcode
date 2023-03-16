from typing import List


# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         ans = []
#         n = len(nums)
#         path = []
#         def dfs(i):
#             if i == n:
#                 ans.append(path.copy())
#                 return
#
#             dfs(i+1)
#
#             path.append(nums[i])
#             dfs(i+1)
#             path.pop()
#
#         dfs(0)
#         return ans

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        path = []
        def dfs(i:int):
            if i == n:

                ans.append(path.copy())
                return
            # 不选
            dfs(i+1)

            # 选
            path.append(nums[i])
            dfs(i+1)

            # 回溯
            path.pop()

        dfs(0)
        return ans

nums = [1,2,3]
solution = Solution()
print(solution.subsets(nums))