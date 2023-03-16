from collections import Counter, deque
from typing import List


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:

        def trans(s):
            cnts = Counter()
            for c in s:
                if c in target:
                    cnts[c] += 1
            return cnts

        availables = [c for st in stickers if (c := trans(st))] # :=赋值新符号
        queue = deque([(target, 0)])
        explored = {target}
        while queue:
            cur,step = queue.popleft()
            if not cur:
                return step
            for avl in availables:
                if cur[0]  in avl:
                    nxt = cur
                    for k,v in avl.items():
                        nxt = nxt.replace(k,'',v)
                    if nxt not in explored:
                        explored.add(nxt)
                        queue.append((nxt,step+1))
        return -1

stickers = ["with","example","science"]
target = "thehat"
solution = Solution()
print(solution.minStickers(stickers,target))


