from collections import defaultdict
from typing import List


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        dic = defaultdict(set)
        for i,t in logs:
            dic[i].add(t)
        ans = [0]*k
        for v in dic.values():
            ans[len(v)-1] += 1
        return ans


logs = [[0,5],[1,2],[0,2],[0,5],[1,3]]
k = 5
solution = Solution()
print(solution.findingUsersActiveMinutes(logs,k))