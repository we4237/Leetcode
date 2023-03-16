from typing import List, Counter


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        cnt = Counter[arr]
        for x in sorted(cnt,key=abs):
            if cnt[2*x]<cnt[x]:
                return  False
            cnt[2*x] -= cnt[x]
        return True
