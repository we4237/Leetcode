from collections import deque, defaultdict
from typing import List

# BFS优化
# class Solution:
#     def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
#         g = [defaultdict(list), defaultdict(list)]
#         for i, j in redEdges:
#             g[0][i].append(j)
#         for i, j in blueEdges:
#             g[1][i].append(j)
#
#         ans = [-1] * n
#         vis = set()
#         q = deque([(0, 0), (0, 1)]) #初始化队列
#         level = 0
#         while q:
#             for _ in range(len(q)):
#                 i, c = q.popleft()
#                 if ans[i] == -1:
#                     ans[i] = level
#                 vis.add((i, c))
#                 c ^= 1 #标签
#
#                 for j in g[c][i]:
#                     if (j, c) not in vis:
#                         q.append((j, c))
#
#             level += 1
#
#         return ans

# 题解BFS
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for x, y in redEdges:
            g[x].append((y, 0))
        for x, y in blueEdges:
            g[x].append((y, 1))

        dis = [-1] * n
        vis = {(0, 0), (0, 1)}
        q = [(0, 0), (0, 1)]
        level = 0

        while q:
            tmp = q
            q = []
            for x,color in tmp:
                if dis[x] == -1:
                    dis[x] = level
                for p in g[x]:
                    if p[1] != color and p not in vis:
                        vis.add(p)
                        q.append(p)
            level += 1
        return dis



n = 3
red_edges = [[0,1],[0,2]]
blue_edges = [[1,0]]
solution = Solution()
print(solution.shortestAlternatingPaths(n,red_edges,blue_edges))