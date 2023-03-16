from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n-1
        ans = 0
        while left < right:

            h1,h2 = height[left],height[right]
            ans = max(ans, min(h1, h2) * (right - left))
            if h1 < h2:
                left += 1
            else:
                right -= 1



        return ans

height = [1,8,6,2,5,4,8,3,7]
solution = Solution()
print(solution.maxArea(height))