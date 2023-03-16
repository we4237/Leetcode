from collections import deque
from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        # root = []
        # for i, j in enumerate(s):
        #     if j == c:
        #         root.append((i, 0))
        # # print(root)
        # res = [10004]*len(s)
        # def BFS(root):
        #     queue = deque()
        #     # 讲目标节点入队
        #     for r in root:
        #         queue.append(r)
        #     while queue:
        #         #取出节点
        #         node,length = queue.popleft()
        #         if res[node] == 10004:
        #             res[node]=length
        #             if node-1>=0:
        #                 queue.append((node-1,length+1))
        #             if node+1<len(s):
        #                 queue.append((node+1,length+1))
        # BFS(root)
        # return res
        n = len(s)
        res=[0]*n

        idx = -n
        for i,ch in enumerate(s):
            if ch == c:
                idx = i
            res[i]=i-idx

        idx = 2*n
        for i in range(n-1,-1,-1):
            if s[i] == c:
                idx = i
            res[i]=min(res[i],idx-i)
        return res


s = "loveleetcode"
c = "e"
solution = Solution()
print(solution.shortestToChar(s,c))