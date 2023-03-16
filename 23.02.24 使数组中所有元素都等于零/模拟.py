from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        x = 0
        cnt = 0
        while sum(nums) != 0:
            for num in nums:
                if num != 0:
                    x = num
                    break
            nums = [num-x for num in nums if num]
            cnt += 1
        return cnt

nums = [1,5,0,3,5]
solution = Solution()
print(solution.minimumOperations(nums)
)

