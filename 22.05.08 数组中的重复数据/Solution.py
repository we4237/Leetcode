from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for i, j in enumerate(nums):
            while j != i+1 and j != nums[j-1]:
                k = nums[i]-1
                nums[i],nums[k]=nums[k],nums[i]
                j = nums[i]
        print(nums)
        return [j for i,j in enumerate(nums) if i !=j-1]


nums = [4, 3, 2, 7, 8, 2, 3, 1]
solution = Solution()
print(solution.findDuplicates(nums))
