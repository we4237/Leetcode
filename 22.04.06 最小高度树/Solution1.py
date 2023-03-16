from collections import deque, defaultdict
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        res = []
        if n == 1:
            return [0]

        degree = [0]*n  # 记录每个节点的度
        map = defaultdict(list)  # 存储邻居节点
        #初始化每个节点和邻居:
        for edge in edges:
            degree[edge[0]]+=1
            degree[edge[1]]+=1
            map[edge[0]].append(edge[1])
            map[edge[1]].append(edge[0])

        #记录度为1的叶子节点
        queue = deque()
        for i in range(n):
            if degree[i]==1:
                queue.append(i)

        while queue:
            res = []
            size= len(queue)
            # 遍历度为1的叶子节点
            for i in range(size):
                cur = queue.pop()
                res.append(cur)
                neighbors = map[cur]
                for neighbor in neighbors:
                    # 将叶子节点的邻居节点度-1,若是新的叶子节点则入队
                    degree[neighbor] -= 1
                    if degree[neighbor]==1:
                        queue.appendleft(neighbor)

        return res



if __name__ =="__main__":
    n = 4
    edges = [[1, 0], [1, 2], [1, 3]]
    solution = Solution()
    print(solution.findMinHeightTrees(n,edges))