from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True) # 降序排列
        n = len(nums)
        for i in range(1, n+1):
            if nums[i-1] >= i and (i == n or nums[i] <i):
                return i
        return -1

nums = [3,5]
solution = Solution()
print(solution.specialArray(nums))