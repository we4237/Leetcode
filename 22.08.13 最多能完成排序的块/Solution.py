from collections import Counter
from typing import List

#排序+哈希表


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        cnt = Counter()
        res = 0
        for x,y in zip(arr,sorted(arr)):
            cnt[x] += 1
            if cnt[x] == 0:
                del cnt[x]
            cnt[y] -= 1
            if cnt[y] == 0:
                del cnt[y]
            if len(cnt)==0:
                res+=1
        return res

arr = [2,1,3,4,4]
solution = Solution()
print(solution.maxChunksToSorted(arr))
