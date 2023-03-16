from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums)-2
        # i是[较大]与[较小]的分界线
        while i >= 0 and nums[i]>=nums[i+1]:
            i -= 1
        if i >= 0:
            j = len(nums)-1
            while j >= 0 and nums[i]>=nums[j]:
                j-=1
            nums[i],nums[j]=nums[j],nums[i]

        left ,right = i+1,len(nums)-1
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1

nums=[1,2,3]
solution = Solution()
print(solution.nextPermutation(nums))
