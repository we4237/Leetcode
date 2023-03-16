# 直接遍历
# class Solution:
#     def maxScore(self, s: str) -> int:
#         mmax = max(s[:i].count('0')+s[i:].count('1') for i in range(1,len(s)))
#         return mmax

# 二次遍历
class Solution:
    def maxScore(self, s: str) -> int:
        ans = score = (s[0]=='0')+s[1:].count('1')
        for c in s[1:-1]:
            score += 1 if c == '0' else -1
            ans =max(ans,score)
        return ans


s = "011101"
solution = Solution()
# solution.maxScore(s)
print(solution.maxScore(s))