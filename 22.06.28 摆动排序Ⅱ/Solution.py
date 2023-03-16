from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        nums[::2],nums[1::2] = nums[:(len(nums)+1)//2][::-1],nums[(len(nums)+1)//2:][::-1]

nums = [1,5,1,1,6,4]
solution = Solution()
solution.wiggleSort(nums)
print(nums)