from collections import defaultdict
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans = defaultdict(list)
        for i,num in enumerate(groupSizes):
            ans[num].append(i)
        res = []

        for k,v in ans.items():
            cnt = 0
            while cnt<len(v):
                res.append(v[cnt:cnt+k])
                cnt += k
        return res

groupSizes = [3,3,3,3,3,1,3]
solution = Solution()
print(solution.groupThePeople(groupSizes))