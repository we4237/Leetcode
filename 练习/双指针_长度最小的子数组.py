# 双指针

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = n+1
        s = 0
        left = 0
        # for right,x in enumerate(nums): #从右侧枚举少写一个判断条件
        #     s += x
        #     while s - nums[left] >= target:
        #         s -= nums[left]
        #         left += 1
        #     if s >= target:
        #         ans = min (ans,right-left+1)

        for right,x in enumerate(nums):
            s += x
            if s >= target:
                ans = min(ans,right-left+1)
                s -= nums[left]
                left += 1

        return ans if ans <= n else 0