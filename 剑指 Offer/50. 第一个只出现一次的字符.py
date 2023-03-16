from collections import defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> str:
        # if s == '':
        #     return ' '
        ans = []
        cnt = defaultdict(int)
        for x in s:
            if cnt[x] == 0:
                cnt[x] = 1
                ans.append(x)
            else:
                cnt[x] += 1
                if x in ans:
                    ans.remove(x)


        return ans[0] if ans else ' '

s = ""
solution = Solution()
print(solution.firstUniqChar(s))