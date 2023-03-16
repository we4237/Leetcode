class Solution:
    def maximumSwap(self, num: int) -> int:
        ans = num
        s = list(str(num))
        for i in range(len(s)):
            for j in range(len(s)):
                s[i],s[j] = s[j],s[i]
                ans = max(ans,int(''.join(s)))
                s[i],s[j] = s[j],s[i]
        return ans

num = 2736
solution = Solution()
print(solution.maximumSwap(num))
