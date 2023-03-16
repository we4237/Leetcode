from typing import List


# class Solution:
#     def trap(self, height: List[int]) -> int:
        # n = len(height)
        # pre_max = [0]*n
        # pre_max[0] = height[0]
        # for i in range(1,n):
        #     pre_max[i] = max(pre_max[i-1],height[i])
        #
        # suf_max = [0]*n
        # suf_max[-1] = height[-1]
        # for i in range(n-2,-1,-1):
        #     suf_max[i] = max(suf_max[i+1],height[i])
        #
        # ans = 0
        # for x,y,z in zip(pre_max,suf_max,height):
        #     ans += min(x,y)-z
        #
        # return ans

# 优化双指针
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n-1
        ans = 0
        pre_max = 0
        suf_max = 0
        while left < right:
            pre_max = max(pre_max,height[left])
            suf_max = max(suf_max,height[right])
            if pre_max < suf_max:
                ans += pre_max - height[left]
                left += 1
            else:
                ans += suf_max - height[right]
                right -= 1
        return ans




height = [0,1,0,2,1,0,1,3,2,1,2,1]
solution = Solution()
print(solution.trap(height))
