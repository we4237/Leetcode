from cmath import inf
from collections import Counter


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = inf

        n = len(blocks)

        for l in range(n-k+1):
            r = l + k - 1
            cnt = Counter(blocks[l:r+1])
            ans = min(ans,cnt['W'])

        return ans

blocks = "WBBWWBBWBW"
k = 7
solution = Solution()
print(solution.minimumRecolors(blocks,k))