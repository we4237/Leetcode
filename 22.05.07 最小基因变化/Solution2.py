##确定当前遍历到了哪一层
# level = 0
# while queue 不空：
#     size = queue.size()
#     while (size --) {
#         cur = queue.pop()
#         if cur 有效且未被访问过：
#             进行处理
#         for 节点 in cur的所有相邻节点：
#             if 该节点有效：
#                 queue.push(该节点)
#     }
#     level ++;
from collections import deque
from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        q = deque()
        q.append([start,0])  #level 0
        while q:
            tmp,step = q.popleft()
            if tmp == end:
                return step
            for i in range(len(tmp)):
                for x in "ACGT":
                    nxt = f"{tmp[:i]}{x}{tmp[i + 1:]}"
                    if nxt in bank and nxt!=tmp:
                        q.append((nxt,step+1))
                        bank.remove(nxt)

        return -1


start = "AACCGGTT"
end = "AACCGGTA"
bank = ["AACCGGTA"]
solution = Solution()
print(solution.minMutation(start, end, bank))