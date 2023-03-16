from typing import List


class Solution:
    def isInit(self,x:int,y:int,xyuan:int,yyuan:int,r:int) -> bool:
        if (x-xyuan) ** 2 + (y-yyuan) ** 2 <= r ** 2:
            return True
        else:
            False

    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = [0 for _ in range(len(queries))]
        for i, query in enumerate(queries):
            for point in points:

                if self.isInit(point[0],point[1],query[0],query[1],query[2]):
                    ans[i] += 1

        return ans

points = [[1,1],[2,2],[3,3],[4,4],[5,5]]
queries = [[1,2,2],[2,2,2],[4,3,2],[4,3,3]]

solution = Solution()
print(solution.countPoints(points,queries))
