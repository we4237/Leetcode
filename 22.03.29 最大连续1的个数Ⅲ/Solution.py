from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        def maxConsecutiveNum() -> int:
            ans,left,sum =0,0,0
            for right in range(len(nums)):
                sum += nums[right] != 1
                while sum > k:
                    sum -= nums[left] != 1
                    left += 1
                ans = max(ans,right-left+1)
            return ans
        return maxConsecutiveNum()

nums = [1,1,1,0,0,0,1,1,1,1,0]
K = 2
solution = Solution()
print(solution.longestOnes(nums,K))