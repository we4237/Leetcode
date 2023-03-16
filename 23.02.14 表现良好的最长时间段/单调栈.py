from typing import List

# 单调栈
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        s = [0] * (n + 1) # s[0]空数组的和
        st = [0]
        for j, h in enumerate(hours, 1):
            s[j] = s[j-1] + (1 if h > 8 else -1) # 前缀和,劳累为1,不劳累为-1
            if s[j] < s[st[-1]]:
                st.append(j) # 单调栈

        ans = 0
        for i in range(n,0,-1):
            while st and s[i]>s[st[-1]]:
                ans = max(ans,i-st.pop())
        return ans

hours = [9,9,6,0,6,6,9]
solution = Solution()
print(solution.longestWPI(hours))

