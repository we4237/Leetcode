from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        tot,s = sum(nums),0
        for i, num in enumerate(nums):
            s += num
            if s>tot-s:
                return nums[:i+1]

nums = [4,3,10,9,8]
solution = Solution()
print(solution.minSubsequence(nums))