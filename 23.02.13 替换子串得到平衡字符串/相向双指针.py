from collections import Counter
from math import inf


# class Solution:
#     def balancedString(self, s: str) -> int:
#         n = len(s)
#         balence = n // 4
#         haxi = {'Q':0,'W':0,'E':0,'R':0,}
#         ans = 0
#
#         for y in s:
#             haxi[y] += 1
#
#
#         if all(haxi[x] == balence for x in "QWER"): # all的用法
#             return 0
#
#         left = 0
#         ans = inf
#         for right, c in enumerate(s):
#             haxi[c] -= 1
#             while all(haxi[x] <= balence for x in "QWER"):
#                 ans = min(ans,right-left+1)
#                 haxi[s[left]] += 1
#                 left += 1
#         return ans

class Solution:
    def balancedString(self, s: str) -> int:
        cnt,n = Counter(s),len(s)
        QWER = "QWER"
        ballence = n // 4
        left,res = 0,inf
        ans = inf
        if all(cnt[c] == ballence for c in QWER):
            return 0

        for right,c in enumerate(s):
            cnt[c] -= 1
            while all(cnt[x] <= ballence for x in QWER):
                ans = min(ans,right-left+1)
                cnt[s[left]] += 1
                left += 1
        return ans

s = "WWEQERQWQWWRWWERQWEQ"
solution = Solution()
print(solution.balancedString(s))

