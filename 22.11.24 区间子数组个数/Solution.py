from typing import List


class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        res = 0
        last1 = last2 = -1
        for i,x in enumerate(nums):
            if left <= x <= right:
                last1 = i
            elif x > right:
                last2 = i
                last1 = -1

            if last1 != -1:
                res += last1 - last2
        return res

nums = [2,1,4,3]
left = 2
right = 3
solution = Solution()
print(solution.numSubarrayBoundedMax(nums,left,right))