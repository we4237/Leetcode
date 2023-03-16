from collections import deque
from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        s = set(bank)
        if end not in s:
            return -1

        d = deque([start])
        vis = {start:0}


        while d:
            cur = d.popleft()
            dist = vis[cur]
            for i,j in enumerate(cur):
                for c in "ACGT":
                    nxt = f"{cur[:i]}{c}{cur[i + 1:]}"
                    if nxt == end:
                        return dist + 1
                    if nxt in s and (nxt not in vis or vis[nxt] > dist + 1):
                        d.append(nxt)
                        vis[nxt] = dist + 1
        return -1

start = "AACCGGTT"
end = "AAACGGTA"
bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
solution = Solution()
print(solution.minMutation(start,end,bank))
