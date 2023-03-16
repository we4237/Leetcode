from collections import defaultdict
from typing import List


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        dict = defaultdict(int)
        for v,w in items1:
            dict[v] = w
        for V,W in items2:
            dict[V] += W

        return sorted([a, b] for a, b in dict.items())


items1 = [[1,1],[4,5],[3,8]]
items2 = [[3,1],[1,5]]
solution = Solution()
print(solution.mergeSimilarItems(items1,items2))
