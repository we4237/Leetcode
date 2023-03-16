from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def bisect(nums:List[int],target:int)->int:
            n = len(nums)
            left, right = -1, n
            while left + 1 < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid
                else:
                    right = mid

            return right

        start = bisect(nums,target)
        if start == len(nums) or nums[start] != target:
            return 0
        end = bisect(nums,target+1)
        return end-start

nums = [5,7,7,8,8,10]

target = 8
solution = Solution()
print(solution.search(nums,target))