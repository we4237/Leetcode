from typing import List
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n, ans= len(arr), 0
        minv, maxv = n, -1
        j = 0 # 划分块的左下表
        for i in range(n):
            minv = min(minv,arr[i])
            maxv = max(maxv,arr[i])
            if j == minv and i == maxv:
                ans += 1
                j = i+1
                minv, maxv = n, -1
        return ans




arr = [1,0,2,3,4]
solution  = Solution()
print(solution.maxChunksToSorted(arr))
