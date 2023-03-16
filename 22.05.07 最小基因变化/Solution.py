from collections import deque
from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        visitied = set([start,])
        q = [(start,0),]

        while q:
            tmp,cnt = q.pop(0)
            if tmp == end:
                return cnt
            for idx,x in enumerate(tmp):
                for y in 'ATCG':
                    if x == y: continue
                    val = tmp[:idx]+y+tmp[idx+1:]
                    if val in bank and val not in visitied:
                        visitied.add(val)
                        q.append((val,cnt+1))
        return -1




start = "AACCGGTT"
end = "AACCGGTA"
bank = ["AACCGGTA"]
solution = Solution()
print(solution.minMutation(start,end,bank))