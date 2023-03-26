from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l,r = 0,n-1
        while l < r:


            if nums[l] + nums[r] > target:
                r -= 1
            elif nums[l] + nums[r] < target:
                l += 1
            elif nums[l] + nums[r] == target:
                return [nums[l],nums[r]]
        return


nums = [2,7,11,15]
target = 9
solution = Solution()
print(solution.twoSum(nums,target))