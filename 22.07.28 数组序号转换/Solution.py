from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = {v:i for i,v in enumerate(sorted(set(arr)),1)}
        return [ranks[v] for v in arr]

arr = [40,10,20,30]
solution = Solution()
print(solution.arrayRankTransform(arr))