from typing import List


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # 构建dislikes有向图
        g = [[] for _ in range(n)]
        for x, y in dislikes:
            a ,b = x - 1 , y - 1
            g[a].append(b)
            g[b].append(a)

        # 未染色的值为0
        color = [0] * n

        def dfs(x:int,se:int) -> bool:
            color[x] = se
            return all(color[y] != se # 每个点都被染色
                        and (color[y] or dfs(y,-se) )for y in g[x])


        return all(se or dfs(i,1) for i,se in enumerate(color))






n = 4
dislikes = [[1,2],[1,3],[2,4]]
solution = Solution()
solution.possibleBipartition(n,dislikes)
