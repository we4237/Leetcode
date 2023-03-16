from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []

        def dfs(idx,n,cur):
            if idx == n:
                ans.append(cur)
                return
            dfs(idx + 1, n, cur + s[idx])
            if 'a' <= s[idx] <= 'z' or 'A' <= s[idx] <= 'Z':
                dfs(idx + 1,n,cur + s[idx].swapcase())

        dfs(0, len(s), '')
        return ans

s = "a1b2"
solution = Solution()
print(solution.letterCasePermutation(s))