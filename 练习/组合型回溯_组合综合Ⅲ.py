from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        path = []
        def dfs(i:int,t:int):
            d = k - len(path)

            if t < 0 or t > (i + i - d + 1) * d // 2:
                return

            if d == 0:
                # if sum(path) == n:
                #     ans.append(path.copy())
                # return
                ans.append(path.copy())
                return
            # 不选
            if d < i:
                dfs(i - 1,t)

            # 选
            path.append(i)
            dfs(i - 1, t - i)
            path.pop()

        dfs(9,n)

        return ans

k = 3
n = 7
solution = Solution()
print(solution.combinationSum3(k,n))

