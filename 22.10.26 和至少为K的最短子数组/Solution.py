from collections import deque
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        ans = len(nums)+1
        preSum = [0]
        #  计算前缀和
        for num in nums:
            preSum.append(preSum[-1]+num)
        q = deque()
        # 超时
        # for i in range(0,len(nums)+1):
        #     for j in range(i,len(nums)+1):
        #         while q and preSum[j]-preSum[i] >= k:
        #             ans = min(ans,j-q.popleft())
                   # 如果新加入的比pre[i]更大则还不如pre[i],直接弹出
        #         while q and preSum[q[-1]] >= preSum[i]:
        #             q.pop()
        #         q.append(i)
        # 优化
        for i, curSum in enumerate(preSum):
            while q and curSum - preSum[q[0]] >= k:
                ans = min(ans, i - q.popleft())
            while q and preSum[q[-1]] >= curSum:
                q.pop()
            q.append(i)

        return ans if ans < len(nums) + 1 else -1

nums = [1,2]
k = 4
solution=Solution()
print(solution.shortestSubarray(nums,k))


