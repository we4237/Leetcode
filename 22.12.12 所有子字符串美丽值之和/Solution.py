from collections import defaultdict


class Solution:
    def beautySum(self, s: str) -> int:
        res = 0
        n = len(s)
        for i in range(n):
            dict = defaultdict(int)
            for c in s[i:n]:
                dict[c] +=1
                res += max(dict.values())-min(dict.values())

        return res

s = "aabcb"
solution = Solution()
print(solution.beautySum(s))