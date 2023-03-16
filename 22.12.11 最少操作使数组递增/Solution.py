from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        for i in range(1,n):
            if nums[i - 1] >= nums[i]:
                d = nums[i-1]-nums[i]
                nums[i] += d+1
                cnt += d+1

        return cnt

nums = [1,5,2,4,1]
solution = Solution()
print(solution.minOperations(nums))