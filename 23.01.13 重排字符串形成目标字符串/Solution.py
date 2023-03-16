from collections import Counter
from math import inf


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        ans = inf
        temp = []
        for c in s:
            if c in target:
                temp.append(c)
        d = Counter(temp)
        for c,cnt in Counter(target).items():
            ans = min(ans,d[c] // cnt)
            if ans == 0:
                return 0
        return ans


s = "ilovecodingonleetcode"
target = "code"
solution = Solution()
print(solution.rearrangeCharacters(s,target))