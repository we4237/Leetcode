from typing import List

MAPPING = ["", "", "abc", "def", "ghi", "jkl","mno", "pqrs","tuv", "wxyz"]

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        ans = []
        tmp = [0 for _ in range(n)]

        if n == 0:
            return []

        # 回溯
        def dfs(i:int):
            # 设置边界条件
            if i == n:
                ans.append(''.join(tmp))
                return

            for c in MAPPING[int(digits[i])]:
                tmp[i] = c
                dfs(i+1)

        dfs(0)

        return ans

digits = "23"
solution = Solution()
print(solution.letterCombinations(digits))